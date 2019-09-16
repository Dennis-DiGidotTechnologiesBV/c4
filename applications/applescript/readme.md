# Applescript Keynote Demo (Only for Applescript V1, not for V2)#

## Overview ##
This is an application written for the DiGidot C4 LED which can be used in combination with the Apple app 'Keynote' for presentations to trigger HTTP-GET triggers. 
The DiGidot C4 Extended is an Art-Net and DMX to SPI pixel controller that allows you to generate, record and trigger scenes and playlists. Countless triggering options can be configured in the built in user interface. A DiGidot C4 network may consist multiple devices that can control huge amount of control channels/universes. All controllers will start synchronized playback when triggered from Keynote.

The main goal of this script is to trigger an event every time a new slide is presented.
You can for example match light effect colors to the colors used in your Keynote slides. You can also trigger brightness, speed and other special content to create an impressive slideshow presentation.


## Requirements ##
* An Apple computer with Keynote installed
* At least one DiGidot C4 Extended (https://digidot.eu/c4/digidot-c4-extended/)

## Usage ##
To make use of this script, first record some scenes on your DiGidot C4. This can be done by generating scenes from the built in web interface or recording scenes from Art-Net or DMX. 
Then, make sure your HTTP-Get triggers are enabled:

* Go to the DiGidot C4 interface (via the app or the IP-address of the device)
* Click on 'Triggers' 
* Click on the 3 dots in the top right and choose 'HTTP/UDP/OSC'
* Enable HTTP Triggers by moving the toggle switch next to it blue and click 'Save'

The next step is to create triggers. Each trigger can be a simple 'play scene' trigger, named after the scene name. 

The final but most important step is to create a Keynote presentation. Enable the "Show Presenter Notes" view, under the top left "view" icon in Keynote. 
To activate a trigger you only need to enter a '#' followed by the trigger name in the presenter notes field. Example: #blue_scene

When you've finished creating your slides with '#' trigger commands, you can download the 'keynote.scpt' by clicking the file and then choose "Download".
After opening the file, you can choose between two ways of using it: the simple or advanced way;

* The simple way is only allowing to edit everything between "Start of parameters" and "End of parameters". 
* The advanced way allows you to change the entire script and fine-tune it to your personal needs. We discourage the last option when you're not comfortable with programming. 

To start the magic, press the 'Play' button at the top of the script. You can stop it by pressing the 'Stop' button. When the script is started, the Keynote presentation will be opened in full screen presentation mode and you can use your presentation as usual. Please note that you need to make sure that the correct presentation is already openend and the desired starting slide selected.

## Important to know ##
* It's best to place the '#' with the trigger name at the end of all presenter notes.
* Don't use spaces for the trigger name
* The script is full of checks for possible errors. To view these before running the script, click the button below in the script window that looks like a sheet of paper. Then click on "Messages". Now when running the script, the status of the program will be shown there.
* Please make sure that the computer that runs the Keynote presentation has a wired or wireless network connection with the DiGidot C4(network)

## Contribute ##
One of the reasons for us publishing this on github, is to inspire our DiGidot, offering extra powerful tools to be used with our products and to allow users to contribute to this code. 
There are 2 files: 'keynote.scpt' and 'keynote_raw.txt'. We recommend to start with the .scpt file for developing and when it's done, copy all the text content to the 'keynote_raw.txt' for reviewing. In the future, there could be a better method to this. 

Have fun programming!

Your DiGidot team
