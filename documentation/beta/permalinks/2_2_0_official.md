## Download Link (available until next beta or release) ##
[Download v2.2.0](http://update.digidot.eu/v2019_1/c4/firmware/v2_0/beta_files/C-4_2021-05-20_2351.c4u)

## Release Notes for DiGidot C4 Firmware v2.2.0 - Published on 20 of May 2021 ##

### New ###
* **sACN**: (Streaming ACN) We added a new input protocol which is used more and more in popular lighting consoles: sACN! We support the multicast version, which is the default. This include  priorities and synchronization universes.
* **RDM**: (Remote Device Management): We now have support for RDM devices with DMX! We can get and set the most common commands like  device name  device type, highlighting the device, the number of channels it's using and the start address.
* **Input/Output Quick edit**: When switching to the Quick edit mode on the In/Out configuration page, the interface will no longer send every change, like: add, change, or remove a universe. Instead, you can modify anything on any device on any port and it won't be applied immediately to the devices so it's very fast. When you're done with the configuration, you can press 'Save' and everything that you configured, will be sent at once to the devices.
* **Full Group support**: Partially, it was already in the interface but now groups are fully supported on all pages. For Playback of scenes, playlists, updating the firmware, triggering and recording!
* **Send feedback to us**: If you have a question, encountered a bug or maybe have a feature request, there is now a new form where you can contact us directly within the interface! Go to 'Support' -> 'Feedback' and let us know.
* **Advanced backup and restore functionality**: It's now possible to backup your scenes and playlists from the SD-card. While this could take a while, it can be convenient if the device is physically unreachable and the speed isn't that important. In addition you can save the current settings (IOconfig, network and accounts) on the SD-card to a special start-up folder so all these settings are applied everytime you power-up the C4 regardless of what changes you make in the current configuration.
* **Play multiple scenes at once**: It's now possible for the play and stop action of a scene, to specify a layer number. This way, scenes can still be played in the background while other scenes take priority.
* **For testing only**: The new experimental scene generator can now be tested from the 'Create Scenes' page if you have 'developer mode' enabled. You do need to have an internet connection to use it.

### Added ###
* UX: On the monitor page, the FPS is now divided into 2 categories: Input and Output FPS. The Input FPS can be Art-Net, sACN or a Scene. The Output FPS is always standalone and shows the actual refresh time on the output.
* Time: A device can now show the uptime in milliseconds since power up.
* UX: It's now possible t  name a backup.
* UX: On the record page, it now shows the FPS information for every device and a warning if it's too low.
* UX: If you have selected one device from the 'select device' at the top, when reopening this pop-up, it will scroll down to this device. 
* UX: When using DMX TTL, an info message shows up about adding multiple universes on one port. If you use DMX TTL to convert it to DMX, you can only have one universe but if you're using DMX TTL to control a LED-string directly, you can have multiple universes on one port
* UX: When you're creating a backup, an ETA will be calculated to give an indication how long the backup process will take.
* UX: On the 'Triggers' -> 'HTTP/UDP/OSC' menu option in the top right corner, it will show available HTTP-GET commands for each scene and playlist to integrate in your system.
* UX: You can now set an 'Alpha' value for the scene and playlist 'play' trigger. 
* UX: (Extended only) On the debug page, we've added an option called "API logging" which logs every single API request from the UX to the device and saves it on the SD-card in the LOG file. 

### Changed ###
* UX: On many places where you can input a time value, the single input field (which was in milliseconds most of the time) has been replaced with a time control (Hours:Minutes:Seconds:Milliseconds) so from now on, you can quickly confirm if a specific time is set or if a new time value needs to be configured.
* UX: On the global settings page of the Input/Output configuration, if you have a Art-Net redirect configured, you now have the option to apply the global settings only on regular inputs and keep the Art-Net redirect(s) untouched.
* UX: On the homepage, there's a new option with 'Support' where the manual can be found. On this page, you can also find the new 'Feedback' and 'FAQ' pages. Keep in mind that these two options require an internet connection where the manual can still be viewed offline.
* Users: A user can no longer highlight a device output an  can't delete playlists anymore.
* UDP: Regular UDP triggers will no longer send "0.000" in it's message, only it's keyword starting with '!' and ending with '#'. Existing UDP triggers, before this update, will still use the zero value in it's message unless it's changed.
* Manual: The manual has been updated with all the new features in this version like RDM, sACN, playback on different layers and many more.
* UX: On the Input/Output configuration page, the 'Art-Net redirects' option is renamed to 'Art-Net out'. This i  to make it more clear that Art-Net can be send standalone, for example; If you have multiple DiGidot C4 Live devices and want to control them with a single DiGidot C4 Extended.

### Improved ###
* Triggers: The 'Next' and 'Previous' commands for playback, works only with a playlist. The trigger description has been updated with this information.
* UX: You can now have multiple time inputs in a single trigger.
* UX: On the monitor page, next to 'Latency from Ethernet', it will show the latency from the Wi-Fi depending on how you are connected with your C4.
* UX: If the interface is loading with a different port than 80, it will use the port specified in the address bar to communicate with the C4.
* UX: The network page now reacts better when devices are connected after the page has been loaded.
* UX: In all popover menus, a mouse hover color is added so you can see which option you're going to choose.
* UX: The style of the knobs in the sliders for 'Color Adjust / HSV' and Saturation modifications, have been changed so it's always visible regardless of the background color. 
* UX: The action layout of 'Color Adjust/HSV' when using a trigger has been modified to make it clearer which color the scene is going to be.
* UX: If you're trying to connect the Ethernet and WiFi of the C4 in the same network, you will get an info message as this may result in connection dropouts.
* UX: All groups can now be removed from the 3 dots menu.
* UX: The info message about the settings that they're loaded from the SD-card, is now streamlined across all pages.
* UX: Refinement in the styling of the RDM page, the Record page, and the dark theme in general.
* UX: When configuring a trigger that needs to preform an action on a different device, the UX now properly checks which scenes and playlists are present on the target device(s).
* WiFi: Both the Firmware and the UX have improved the process of checking the credentials and connecting as a client (also including the DHCP Lease process) to an existing WiFi network. 
* Backup/Restore: If you've configured a WiFi password, for either Accesspoint or Client mode, it will be stored encrypted in a backup file, and can also be restored from a backup file.
* FPS: The C4 now reports the incoming FPS from only the active inputs (Art-Net/sACN).
* Input/Output: The API commands to get the input and output data is now more efficient and only gives the whole input/output back when the watcher is active
* UX: A lot of information text has been rewritten to make it clearer. 
* UX: After you've recorded a scene, the crossfade slider now has more precise control and you can set the fade value manually with a text field.
* UX: With triggers, if you have a brightness or alpha slider as a option, it now has 20 steps to make it more easy to select values like 5%, 10%, 15% etc.
* UX: When creating a playlist, the fade time will be saved as a simple number 
* UX: When playing different scenes on different devices, the playerbar now saves which scene is playing so if you press the 'stop' and 'play' button after each other, it will resume where it left off.
* UX: Time Period and cron has been updated with new controls and are more stable.

### Fixed ###
* Time: The calculated sunset/sunrise time for some countries are corrected.
* UX: When combining a C4 Live and Extended, triggers are now correctly loaded from the Extended only.
* UX: On the network page, the sorting method by order and by IP-address, as well as the functionality sorting ascending or descending, is now working correctly.
* UX: When updating multiple C4 controllers, the correct update file will be selected, so no more 'Update empty file' message will appear.
* UX: If you're very fast with selecting a device while the home page is still loading, it won't generate an error anymore.
* UX: For an analog trigger, the event 'between dimmer values' works again.
* UX: Highlighting a port on the device will now have the proper number of channels on that port.
* UX: Action lists can now be triggered again with HTTP (get and post) requests.
* UX: The Trigger watcher now gives proper feedback when a trigger uses more than 1 input.
* UX: The playback speed value on the advanced settings of a scene is correct now.
* UX: The time of the recording now stays in place and no longer wiggles. 
* UX: When switching from devices on the record page, the inputs will check if there's a signal incoming, will properly update.
* UX: Alert will be shown once again when trying to create a HTTP/UDP/OSC trigger while the protocol itself is disabled in the settings.
* UX: On the Output Limiter page, the global limiter is now properly linked to the individual limiters of the device.
* UX: When using the Backup or Restore feature, the items to select will now be correctly updated if both Live and Extended devices are selected
* UX: If a scene is recorded and you want to change the universes of the scene, the edit page will now show the correct matching universes.
* UX: Gamma correction is now disabled for Art-Net redirects by default.
* UX: Scenes will now be correctly loaded when a 'User' has logged in.
* UX: A linked trigger will now correctly be shown in the 'Trigger Watcher'
* UX: When editing groups, the page will now be refreshed each time after you've edited one or muliltiple groups.
* And many other small fixes & improvements!

