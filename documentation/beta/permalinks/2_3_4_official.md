## Release notes for DiGidot Controller Firmware v2.3.4 - Released on 16 of March 2022 ##

### Added ###
* LED IC: Current control for TM1814. You can now customize the current that's being sent out to the TM1814. You can customize it for each color in 64 individual steps.
* Scenes: When using the accounts feature, and a normal user account is created and logged in, switching between scenes now goes smoothly with a fade.
* IOconfig: DMX TTL can now have up to 4 universes instead of only one. Keep in mind the performance will drop significantly if using more than 2 universes.
* Time logging: Every 'set time' command from the API is now logged so it's possible to trace back any time drifting.
* Developer options: When 'Developer mode' is enabled, this will have the following effect: Animations will be removed (interface reload required) and controllers won't reboot automatically at the triggers page.
* Hotkeys: To setup the DiGidot controller faster, the following hotkeys have been added: SHIFT + R will restart the selected device(s), SHIFT + Left/right arrow will browse trough the device list and ESC will go back one page.

### Changed ###
* Device settings: When a manual time is entered in the controller, this time will be shown at the device page instead of showing a place holder text.
* Triggers: If you create a trigger, the default destination device, when using a single input device, will be a universal MAC-address (00:00:00:00:00:00) instead of using the exact device it's MAC-address so you can easily copy the trigger over to another device, without changing anything.
* Triggers: The restrictions in an action list (greyed out actions when choosing from the list) are now removed so you can freely assign actions.
* Logging: Reduce the maximum log file size from 10 to 5 Megabyte.

### Improved ###
* Getting started: Changed the timing of the requests that are being sent to the DiGidot Controller while ordering devices, is now much more reliable. 
* Record: The Record edit page on mobile now scales properly when switching from portrait to landscape and vice versa.
* Monitor: The table will now sort more responsive if you sorting on ping time, if you're using both PxLNet Node(s) and C4's.
* Highlight: The Highlight API now also accepts an array with values that can be used to highlight a selection of the output.
* UX general: in the File Editor, the scrollbar is now bigger in size so it's easier to use with a mouse. Also, the text render process has been optimized so the editor, and scrolling motion is much faster. 
* UX general: If you enter a wrong value into a input field, for example, a character into a number field, there will be a red underline to indicate the value is invalid and should be changed.
* UX general: Styling of the Record page is now more responsive on mobile devices.

### Fixed ###
* IOconfig: With DMX-TTL, you can now change the color order again if you've configured more than a single universe.
* IOconfig: With a PxLNet Node, 2 bugs have been resolved regarding autocomplete.
* IOconfig: DMX-Input is now ignored when you generate a scene. Also, the advanced settings of a DMX-Input can be saved again.
* IOconfig: When using Quick-Edit mode, the universe fields won't be changed automatically but remain untouched until you manually change it.
* Input watcher: Changing the device at the input watcher, now correctly shows the values of the device that's being selected.
* Input watcher: When using the same input universe multiple times, in the input watcher, this universe will only be shown once, instead of multiple times.
* Output watcher: Resolved some issues with the output watcher when using a 12 or 16 bit LED IC as a output.
* Monitor: On the monitor, the individual port highlight is now synchronized with the main 'Highlight' button.
* Record: When disabling triggers before recording, the triggers will stay disabled if you navigate to the 'Record settings'.
* Record settings: If you change the universe where the controller needs to record from, the universes displayed, will now be sorted based on it's number.
* Raw playback: The full area of the play button is now clickable instead of only the play icon itself.
* Playlist: If you want to play another playlist after a playlist is done, the list of playlist to choose from, is now correctly retrieved.
* Playerbar: When rapidly changing scenes, the Hue (color adjust) slider in the player bar will now have the correct position.
* Triggers: Playlist is now loaded correctly if using a linked trigger, when the action destination is 'Input Device'.
* Triggers: If you edit a DMX trigger after creating one, the input type won't switch to Art-Net anymore. Also, if you choose to trigger on DMX, and no DMX input has been created yet, it will be added to the Input/Output Configuration.
* Triggers: If you're using the linked trigger, in combination with a playlist, it now works as expected and won't endless re-trigger the active scene.
* Groups: Startup devices (show devices when the interface loads) will now function properly if you're using PxLNet Nodes.
* Groups: When changing a group, which also can change the unique id of the group, all the corresponding triggers and actions will be correctly updated with the new unique id.
* Backup & Restore: If a PxLNet Node with a SD-card is used with the feature 'Backup On SD-card', it will now correctly display a message in the interface if the configuration is loaded from the SD-card.
* Backup & Restore: Names of playlists, and the intensity of the status LED, are now correctly set when a backup is restored.
* License: For Live devices, the time and date will also be synced now. This prevents the expiration flag to be set too early, if an expiration date is present.
* Time & Date: Sometimes, a manual entered date wasn't applied. This has been fixed.