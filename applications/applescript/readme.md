# Applescript Keynote Demo #

## Overview ##
This is an application written for the DiGIdot C4 which can be used in combination with the free app 'Keynote' for presentations to trigger HTTP-GET triggers. The main goal with this script is to trigger an event everytime when a new slide is presented.

## Requirements ##
* Keynote
* DiGidot C4 Extended

## Usage ##
To make use of the script, first record some scenes on your C4. This can be done by generating from the interface or recording scenes from Art-Net. Then, make sure your HTTP-Get triggers are enabled:

* Go to the interface of the C4 (via the app or the IP-address of the device)
* Click on 'Triggers' 
* Click in the top right the 3 dots and choose 'HTTP/UDP/OSC'
* Enable HTTP Triggers by making the toggle next to it blue and click 'Save'

The next step is to make all the triggers. Each trigger can be a simple 'play scene' with as the name of the trigger, the scene name.

Finally but the most important step, is to create a Keynote presentation. You must also enable the "Show Presenter Notes" view which can be done in Keynote top left icon above the text "view". Now you can call a trigger in the presenter notes by adding a '#' and then the trigger name. Example: #blue_scene.

When you're done with creating slides, you can download the 'keynote.scpt' by clicking the file and then choose "Download".

After opening the file, you could choose between two ways of using it: the simple or advanced way.

The simple way is only editing everything between "Start of parameters" and "End of parameters". The advanced way is well, you could change the whole script and fine-tune it with your needs. I would't do that if your not really comfortable with programming. To start the magic, press the 'Play' button at the top of the script. You can stop it by using the 'Stop' button.

## Important to know ##
* It's best to place the '#' with the trigger name after it as the very last item in the presenter notes.
* Don't use spaces for the trigger name
* The script is full of checks for possible errors. To see these, before running the script, click the button below in the script window that looks like a sheet of paper. Then click on "Messages". Now when running the script, the status of the program will be print there.

## Contribute ##
One of the reasons of this on github is to let users contribute to the existing code. There are 2 files: 'keynote.scpt' and 'keynote_raw.txt'. It's best to first work with the .scpt file for developing and when it's done, copy all the text content to the 'keynote_raw.txt' for reviewing. In the future, there could be a better method to this. 
