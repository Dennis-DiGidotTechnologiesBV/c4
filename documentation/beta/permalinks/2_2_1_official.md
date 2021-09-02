## Download v2.2.1 ##
[Click here](https://github.com/Dennis-DiGidotTechnologiesBV/c4/releases/download/v2.2.1-production/C-4_2021-09-02_1354.c4u)


## Changelog for DiGidot C4 Firmware v2.2.1 - Released on 2 September 2021 ##

### Changed ###
* IOconfig: 'Art-Net redirect' is now called 'Art-Net out'.
* Recording: By default, the interface now records every configured universe of every selected device regardless if the universe is receiving a signal. You can always change the universe to record on from the 'Record Settings' page. These changes will be kept until the interface is reloaded or opened from a different device.

### Improved ###
* General: All input fields with the type 'number' will now immediately display an error even if the input fields doesn't have focus. 
* Backup: The estimated time for creating a backup will now take all devices it's content into account.
* Playlist: If a playlist is repeated one or multiple times, this will be visible when selecting the playlist as an action on the trigger page.
* IOconfig: The port limiter page is completely rewritten to be more responsive to user input. Also, multiple info and warning messages have been added: if you want to discard any changes, change the current selected device(s) or you have a Art-Net out configured.
* Mobile: Improved the scaling of text and buttons on various places for small screens (resolution of 1280 x 720 and smaller).
* Recording: The status on the record page now shows the text 'Show FPS' instead of '0 FPS' if one or multiple devices of the selected ones has a FPS of 0.

### Fixed ###
* High - IOconfig: When you're using sACN as input protocol and open the advanced settings, the protocol won't be switched back to Art-Net anymore.
* Medium - App: On iOS 14, the display height will now be calculated correctly. Before this, sometimes, the playerbar was displayed off screen.
* Medium - Scenes: An issue has fixed that what caused by fast switching between scenes.
* Medium - Triggers: If you have configured a HTTP trigger and perform a re-discover, the trigger page will now load correctly if you try to edit the HTTP trigger.
* Medium - Triggers: A linked UDP/OSC trigger can now be edited again after creating it.
* Medium - Triggers: When using a time period trigger, the option to trigger on 'Single time' will be fired correctly.
* Medium - Cache: A pull-to-refresh action on the scenes, playlist and trigger page, will now check the cached version of the items against the items on the devices and indicates other open interfaces that somethings has changed if the cached and current items aren't the same.
* Medium - DMX: Port DMX2 (active on output D3 and D4) works again if that's the only DMX output configured.
* Medium - Groups: If the internal battery is low, removed or doesn't make contact, group names will be correctly deleted on a power cycle so it's possible to re-configure groups again.
* Medium - WiFi: Switching from AP to client and vice versa, and switching from DHCP to Static IP, on the WiFi page will now correctly update all controls and text.
* Medium - WiFi: If you press the 'save' button after you've configured the WiFi to connect as client, the password will not be reset anymore.
* Low - General: When you lost the connection to a device, if you click the 'cancel' button, it will properly clear the message queue regardless if the previous message has been successfully sent.
* Low - General: Sorting devices on the network and IOconfig page, based on the 'devices order', is functional again.
* Low - Ticket: On iOS, the support ticket page will now be fully shown.
* Low - IOconfig: When switching from sACN to Art-Net, the universe number will now be checked if it isn't higher than 32767 which is the highest number possible for an Art-Net universe.
* Low - IOconfig: When changing the input protocol in quick-edit mode, the IO configuration now stay's in edit mode instead of directly saving it to the devices.
* Low - IOconfig: When the same input universe is added multiple times on a single device, the IP-address filter parameter will now be correctly set for that universe.
* Low - IOconfig: Changing between RGB / RGBW LED IC's will now correctly update the fallback parameters on the global settings page.
* Low - IOconfig: If you have multiple devices, and one or more, but not all of them, have a SD-card error, the interface will now correctly load the content (playlists / scenes / triggers) of the devices that don't have an error on their SD-card.
* Low - Scenes: When you don't have a IOconfig configured on a single device, the 'generate scene' page will now show an error.
* Low - Scenes: If you have devices where some of those don't have an SD-cards present, the other devices which do have an SD-card will now be correctly loaded.
* Low - Playlist: The scene list will now be refreshed when you try to add a scene to a playlist after you've recorded something.
* Low - Triggers: On the analog calibration and the watcher views, when switching to a different device, the page will now be updated correctly to the selected device.
* Low - Triggers: The 'Save and Clone' functionality now also works after the trigger is already created.
* Low - Triggers: On the linked trigger page, is now possible to use the input watcher if you're working with sACN.
* Low - Triggers: A duration (delay) value of a 0-10 volt analog trigger is now correctly updated after the trigger has been saved.
* Low - Triggers: Triggers that use the 0-10 volt range will now trigger correctly on the given value based on the 'offset' and 'length' parameter.
* Low - Triggers: Linked triggers that are linked to start a specific scene in a playlist won't start the first scene anymore if the value is 100%.
* Low - Triggers: Saving Art-Net triggers to record a scene now works again.
* Low - File Browser: The text 'folder is empty' will now disappear after uploading a file to that folder.
* Low - API: If an unknown Unique ID is sent for testing outputs, the device will no longer crash.
* Low - Getting Started: When 'Previous Step' was clicked on the configure channels page (step 3) the interface will now correctly re-configure the temporary input and output configuration when using the 'highlight' method while ordering devices.
