# Template for communicating with a DiGidot C4 controller in Python
# Dennis Morren
# 11-03-2022

from urllib import request, parse
import json
import hmac
import hashlib
import binascii
import random

# User settings
# This is the C4 IP address 
setting_ip_address = "10.254.254.254"

# This is the number of seconds untill the HTTP request times out (for example, if the C4 is off)
setting_request_timeout = 5

# If you want to show the traffic between this computer and the C4, set this parameter to 'True'
setting_show_traffic = True

# User credentials. Default is admin for username and password. If using accounts, you can enter the username and password here.
setting_username = "admin"
setting_password = "admin"

# Program variables
# DONT CHANGE THIS
url = 'http://' + setting_ip_address + "/ajax.json"
nonce = ""

# Basic C4 Message structure
#
# SHA1-key    783fcfadd71c9c0e4938fa4b9010e621fb5fdfeb
# JSON        {"action":"authenticate","subaction":"check","mac_address":"00:00:00:00:00:00","auth":{"nonce":"c0f83233b2079e854b069dce0db0cedcf03fa773","user":"admin","session_id":475022,"sessionid":475022}}
# SHA256-key  09d61f1f929b63bd14ec1f5f7c89d8f268461823f9d386ab9ec6817ea3866280
#
# Communication with the C4 goes as follow
#
# 1. All the JSON data goes into a SHA256 hash with a HMAC key. This HMAC key is the SHA1 hash of the password of the current user
# 2. The SHA256-HMAC result is appended to the JSON data
# 3. The JSON data (which now also contains the SHA256-HMAC hash) now goes into a SHA1 hash.
# 4. The JSON data (which now contains the SHA1 + JSON + SHA256-HMAC) can now be sent to the C4

# Generate an session ID for the resot fo the communication
session_id = random.randrange(1, 999999)

# The SHA1 key is a simple SHA1 operation on the whole message. This message contains the json data and the SHA256 key after it
def CreateSHA1(message):
	hash_object = hashlib.sha1(str.encode(message))
	return hash_object.hexdigest()

def CreateSHA256HMAC(key, message):
	byte_key = key.encode();
	message = message.encode()
	return hmac.new(byte_key, message, hashlib.sha256).hexdigest()

def C4Request(request_json):

	global nonce
	sha256_signing = True

	# Add default MAC-address. Every C4 will respond to this MAC-address
	request_json["mac_address"] = "00:00:00:00:00:00"

	# For authenticating, we don't send the 'auth' object and don't use SHA256 signing
	if "subaction" in request_json:
		if request_json["subaction"] == "nonce":
			request_json["session_id"] = session_id
			sha256_signing = False
	
	if sha256_signing:
		request_json["auth"] = {"nonce": nonce, "user": setting_username, "session_id": session_id}

	# JSON to string conversion
	message = json.dumps(request_json)

	# Add SHA256-HMAC hash of the JSON message with as HMAC, the SHA1 hash of the password for the current user
	# This step is skipped if authentication is preformed
	if sha256_signing:
		sha256_hmac_key = hashlib.sha1(str.encode(setting_password))
		sha256_key = CreateSHA256HMAC(sha256_hmac_key.hexdigest(), message)
		message = message + sha256_key

	# Always add a SHA1 hash of JSON message (and the SHA256-HMAC if needed) and add that in front of the JSON data
	sha1_key = CreateSHA1(message);
	message = sha1_key + message

	if setting_show_traffic:
		print("Request:  ", message)

	# Send request
	req = request.Request(url, data=str.encode(message))
	response = request.urlopen(req, timeout=setting_request_timeout)

	# Wait for response and then convert it into a JSON object
	response = response.read()
	json_response = str(response, 'utf-8')
	json_response = json.loads(json_response)

	# Update nonce for next request
	if "nonce" in json_response:
		nonce = json_response['nonce']

	if setting_show_traffic:
		print("Response: ", json_response)

	return json_response;

def C4Authenticate():
	# Authenticate to the C4 with a username
	C4Request({"action": "authenticate", "subaction": "nonce"})
	C4Request({"action": "authenticate", "subaction": "check"})
	return

### Main program
C4Authenticate()

# Get information about the firmware
about_json = C4Request({"action": "about"})
print(about_json)

# Get the Performance stats from the C4
performance_json = C4Request({"action": "io_manager", "type": "io_config"})
print(performance_json)

