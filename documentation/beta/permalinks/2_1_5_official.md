## Download Link ##
[Download v2.1.5 Official](http://update.digidot.eu/v2019_1/c4/firmware/v2_0/files/C-4_2020-12-23_1024.c4u)

## Release notes for DiGidot C4 Firmware v2.1.5 - Released on 23 December 2020 ##

##### Added #####
* LED IC: Support for GS8206.
* LED IC: Support for LPD1101.
* LED IC: Support for UCS1909.
* LED IC: Support for UCS2909.
* Status LED: The onboard status LED now has 4 options for brightness: 0%, 10%, 25% and 100%.
* UI: It's now possible to add multiple universes on a DMX output. Keep in mind that the total number of channels on that output is still 512.
* UI: After a recording, the UI verifys the record of all connected devices and shows a message if is a significant number of skippend frames. 
* UI: Global settings toggle for 'Smart DHCP Server' and 'Subnetmask' (for ethernet).
* UI: The filebower upload and download is now fully compatible with Android and iOS.
* Art-Net redirect: The destination address can be specified for a Art-Net redirect. By default, it will broadcast the universe on the whole network. It's recommended to specify an IP-address to significantly reduce the network load.
* UI: When creating a UDP or OSC trigger, the default receiving port can be found the text description (port 6454 for UDP and 8000 for OSC).
* Time: It's now possible from the interface to enable or disabled Daylight Saving Time (DST). The DST implementation is based on Europe.

##### Changed #####
* Manual: A new version of the manual is included with will contains all changes since v2.1.4 .
* Mobile: The 'Download' and 'Upload' button is removed from the file browser menu due to incompatibility reasons. It is possible to download and upload files from an iOS or Android device if you're accessing the interface with a browser.
* UI: We changed our advice regarding the maxium number of scenes in a playlist form 20 to 50 due to optimalisation of the playlist file.
* UI: The playerbar when opened now has the icons on top of the sliders to prevent accidental long press when dragging the slider.
* UI: By default, the time won't be retrieved every 3 seconds at the device page. To enable this, click the 3 dots in the top-right corner on de device page and select "Show device time"..
* UI: Device order number can now be changed after using the "Getting Started".
* UI: Just like a scene, prevent a user from deleting a playlist when it's currently playing.
* UI: The license request to the register server has a higher timeout (100 instead of 15 seconds) for locations with many devices in a single network and/or with a low bandwidth. 

##### Improved #####
* Triggers: Counter trigger compatibility.
* Update: On the FWupdate page, the default upload speed is almost 2 times faster.
* SDcard: In some rare cases, it could happen that, when you insert a SDcard into a DiGidot C4 Extended, "No SDcard" is returned as a error. If you're sure that the SDcard is inserted correctly into the C4, you can go to the web interace -> Settings -> Interface -> Enable developer mode. Then go back to Settings -> Debug Environment -> Force SDcard communication. This way, the card detect pin is bypassed.
* UI: On the device page, the interface will no longer send request to the C4 in the background when the window is not active anymore.
* UI: Informativer error feedback messages on the file browser page.
* UI: The whole UI now has a design which is more consistent across different pages.
* UI: Text description on the trigger page, when using type 'analog' or 'button' is also more consistent.
* UI: Text is now selectable on many pages so you can copy/paste things easily.
* UI: Removed unnecessary 'status' requests when  the WiFi tab on network page is active.
* UI: Text description of Time Period option while using a time trigger.
* UI: On the accounts page, there have been several improvements regarding: clicking actions of overlaying buttons, change the cursor icon when hovering over buttons, and prevent editing accounts when the current user doesn't have enough rights to edit them.
* UI: When saving a trigger, the interface will now re-fetch all triggers from the device and then re-adds the trigger to that. Because of this extra check, any changes from the moment the interface is loaded, until the trigger is actual saved, won't be lost anymore. 
* UI: When loading the interface, all assets of the interface are now checked for integrity and a reload button will be shown to notify the user something went wrong.
* UI: Various improvements in the dark theme.
* UI: When using the Safari browser on a iOS device, you can now download and upload files with the file browser. On all mobile platforms including iOS, and in the app, only uploading files is supported. For downloading files, you need to use a desktop/laptop.
* UI: Improved error handling and stability when using the interface on a high number of devices (over 20).
* UI: If a scene can't be played, an error will be shown.

##### Fixed #####
* HSV: The current H, S and V values are now correctly returned again if you send a HSV Offset command.
* Triggers: When using an analog or button trigger, no more missfires will occur.
* Scenes: Scenes will now always start playing from the first frame instead of the second frame.
* DMX IN: When a LEDstrip is connected to the C4 and the Input/output configuration is set to DMX Input, the C4 will no longer crash.
* LED IC: SM16704 is now configurable again.
* Triggers: The C4 no longer needs a restart after UDP or OSC triggers are enabled.
* Triggers: With HSV actions, the hue, saturation and brightness parameter will now have the correct value.
* Scenes: When using a long fadetime as a transition, when a stop command is sent, the C4 will now immediately stops playing all scenes instead of waiting for the fadetime to finish.
* Record: When using a crossfade effect after a scene has been recorded, the last frame is not longer a ghost frame with random data.
* Record: The second frame of the record will now be recorded at the right time.
* UI: Recordings longer than 1 hour will now save correctly.
* UI: When changing the Input/output to a different LED IC, the interface now properly reacts to tthe new situation depending on what's configured on the other ports of the device.
* UI: DMX can now be used again in the "Getting started".
* UI: Generating a colorscroll with multiple devices when using a RGBW LED IC now generates correctly.
* UI: API URL for HTTP-get has been corrected.
* UI: Autocomplete now works correctly when the start universe is non zero.
* UI: When using segments, the color order data will be respected again.
* UI: On the getting started page, the calculator is now correct when using more than 1 device.
* UI: On the Update page, the changelog text is now fully visible again.
* UI: When playing the first scene on the scene page, the previous command now properly goes to the last scene from the list.
* UI: A Playlist will now play normally if the device hasn't setup an IP-address yet.
* UI: If any device has a expired license, the interface won't be stuck in a reload loop anymore.
* UI: Scenes in a playlist, and colors from the generated color scroll can be dragged around again.
* UI: When giving a recorded scene a name, the length of the name will be checked now (min 2 and max 32 characters).
* UI: When DST is enabled, the sunset/sunrise is now correct and won't offset any longer by an hour. 
