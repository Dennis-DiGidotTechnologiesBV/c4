<div align="center">

  <h3 align="center">FTP (File Transfer Protocol)</h3>
</div>

## About this firmware 
This firmware adds FTP to the DiGidot Controller. After you've installed this, you can get a free FTP client (like FileZilla) to transfer from/to an SD-card. The main reason to 
for using this, is that it's much much faster than the interface can download or upload files. Especially if you have large (and many) scenes, this can save a lot of time.

## So how fast is it?
We've done some testing on a scene that is 10mb. These are the results:

* Upload (from your computer to the DiGidot controller)
* Download (from the DiGidot controller to your computer)

**With the App / interface**

Upload: 3:21
Download: 1:46

**With FTP**

Upload: 25 sec
Download: 26 sec

Upload = **8 times faster**
Download = **4 times faster**

## Usage


* Install the custom firmware. After that, the FTP server will be active right away.
* To Download files, you just need a FTP-Client like _FileZilla_ .
* Force the FTP-Client to work in 'binary' transfer mode. In FileZilla, this is done by going to the menubar -> Edit -> Settings -> FTP: File Types -> Choose _Binary_
* In FileZilla, you configure a new connection with "insecure FTP" to the IP-address of the DiGidot controller just like this:
<img src="https://i.imgur.com/DmEkM3R.png.jpg">

* When connecting for the first time, a warning may pop-up about it's using a insecure connection. This is no problem as long as the network you're on, is local and not conencted to the internet
* Now you can download files by dragging them from the right window to the left one.
<img src="https://i.imgur.com/IT2h1Nk.png">

## Changelog
10-03-2022: First version
15-03-2023: Updated firmware base to 2.3.4
