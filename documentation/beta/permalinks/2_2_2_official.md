## Release notes for DiGidot C4 Firmware v2.2.2 - Published on 27 December 2021 ##

### Added ###
* Analog infotext: Added some extra information regarding open and closed circuit definition at the 'event' setting.
* Triggers: There is now a third category for trigger on which type of controller the action should be executed: 'On input controller'. This will write a universal MAC-address in the file so the trigger itself can easily be copied over to different controllers without any changes.
* Triggers: When going to the record page, there's a button added which can temporarily disable all triggers (except triggers that control the recording) so they won't affect the recording in any way. When leaving the record page, or restarting the controller, all triggers will be re-enabled again. 
* Triggers: When using UDP or OSC triggers, if the controller is configured in WiFi client mode, the given IP-address will be displayed.

### Changed ###
* Analog calibrate: The pop-up menu of 'Analog calibrate' will now, by default, select a single controller instead of 'All devices'.
* Triggers: When creating a trigger, the default output controller was 'All devices' which gave a side effect of always broadcasting the action of the trigger, even if there's only a single controller on the network. Now, when creating a trigger, when only a single controller is selected, the action will be executed on that controller only. And if the trigger is configured on multiple controllers (e.g. a group), the action will only be performed on the controller itself. Notice that the default 'output controller(s)' is changed but you can change it any destination you want.
* IOconfig: On a sACN item, the IP-address filter is removed because the controller only supports the default distribution of sACN (which is multicast) and with this, an IP-address filter has no effect.
* OSC: The controller supports OSC as a float (comma) value, or as a integer value. It's important that, for float values, the controller expects a value between 0.0 and 1.0 and for integers, it expects a value between 0 and 100. The description on the linked trigger page has been updated with this information.
* Triggers: A playlist trigger will now show the playlist name itself instead of all the scene names form that playlist.

### Improved ###
* Caching: The caching of the configuration, the scenes and the triggers in the interface, will now correctly be cleared and reset if a SD-card format or a factory-reset is performed.
* Getting started: After the step of assigning the order for each controller, the wizard will use the controller(s) it's IP-address to communicate directly instead of proxying it trough the master. This results in a much faster process time when configuring the Input/Output configuration.
* Getting started: When clicking the 'Getting started' button, several warning prompts are being added to make you more aware of the fact the complete IOconfig will be removed if you make any changes in the process.
* IOconfig: The API will now return correct error messages when deleting temporary configuration items. Also, these items are now correctly removed from the controller.
* IOconfig: Added more usable RAM-memory due to the way the Input/Output configuration is saved, and loaded at startup from Flash to RAM. This improves the stability of the controller if you're working with a lot of universes (> 16) or a lot of triggers (> 25).
* Monitor: At the monitor page, requesting status messages now always goes directly to the controller instead of redirecting it via the master controller.
* Playlist page: When changing some parameters of a playlist, the page itself will be refreshed correctly to reflect the new changes.
* Quick Edit: Improved error messages when an invalid value is entered into an input field.
* Record page: If you quickly navigate to the record page and then back to the home page, the interface will no longer continue polling the fps from the controllers.
* Record page: After you've record something, and while saving a record, the progress bar of the interface is now more linear because it now checks the controller which takes the longest time to progress or save.
* Scene page: When recording a new scene, it will show up at the bottom of the scene list page even if there are already scenes recorded where the order has changed from.
* Scene page: If you already ordered some scenes, these will now be always on top in the scene list. New scenes (generated or recorded) will always be added at the bottom of the list.
* Scene page: When editing a scene, there will now be an error message shown if you try to save a playing configuration which is invalid with the current Input/Output configuration.
* Triggers: When creating a trigger on a controller where the action must be executed on a group, and the controller where the trigger occurred, isn't part of that group, it will now be broadcasted on the network to fire on controllers that are part of the group.
* Triggers: For IOTriggers (Art-Net/sACN and DMX), the interface will now check, when editing the IOconfig or editing the IO triggers itself, if the final IOconfig is still correctly configured to make the IOtrigger actually work.
* UX: When opening the RDM page, the interface now properly checks if the controller it's running on, is in portrait or landscape, and the layout will adjusted on that.

### Fixed ###
* Medium (Analog calibrate): The 'analog calibrate' settings are now correctly saved/retrieved from the controller.
* Medium (Android): In some cases, when using an Android device, it could happen that the playerbar was very small and almost impossible to expand. This has been fixed now.
* Medium (DMX trigger): The DMX trigger saving and parsing process has been rewritten to make sure that the trigger will keep working even if the Input/Output configuration changes in the future. If this happens, extra messages will be shown to inform you about possible side effects when changing the configuration.
* Medium (General): Restart controllers now works again on controllers with a live license.
* Medium (IOconfig): If you changed the fallback color to black (value 0 for all channels), the item was correctly saved but the interface showed that red (255,0,0) was configured which was incorrect.
* Medium (Tickets): Ticket form it's URL is now accessible again. Also, the URL itself is dynamic now so if, in the future, the URL to the ticket form is changed, we can update that server side.
* Medium (Time triggers): When using a Safari web browser on a device (iMac, Macbook, iPhone, iPad etc.), the time trigger will now be correctly created again.
* Low (Accounts): If you try to change the username of an account, it's new name is now correctly displayed after, changing it on the account page, and also if you want to change the password of that account.
* Low (Backup/Restore): Triggers with the action 'previous -or- next in playlist' will now be properly restored from a back-up.
* Low (Backup/Restore): A backup operation will now continue even if there's a controller who's missing it's SD-card. This controller will be skipped.
* Low (Dark theme): Some buttons showed the wrong 'hover' color when a mouse pointer was on it. This has been corrected.
* Low (IOconfig): End channel was off by 1 (e.g. shown 513 instead of 512).
* Low (IOconfig): When you're in Quick-Edit mode, it will no longer disable the 'Save' button after you've saved on a single controller only.
* Low (Quick edit): When using the quick-edit mode, changing a DMX input now works correctly. Also, in the firmware, a hardfault is prevented when you're trying to remove a DMX input while it's still linked to another object.
* Low (Record triggers): Trigger settings are now correctly updated if you change the controller(s) from the top bar.
* Low (Record triggers): When using the 'save' command, the controller will no longer generate a fault when creating a new scene file.
* Low (Scenes): The scene list is now automatically refreshed after a record has been made.
* Low (Triggers): When saving a trigger with, on the input, a group of controllers, it will now be shown correctly at the trigger overview page.
* Low (WiFi): When using the 'Auto Channel' mode on the WiFi when it's in Access Point mode (which is the default), this mode is now properly activated.
