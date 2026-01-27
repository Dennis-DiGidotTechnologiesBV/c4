## Release notes for DiGidot Controller Software v3.2 - Released on 27 of January 2026 ##

##### General #####
This is version 3.2.0 of DCS and its available for every DiGidot controller out there. It's main focus is stability: We've gained a lot of feedback on previous releases like v3.0.3 and v3.1. For us, its important that, at its core, the software is reliable and can be used in a 24/7 operation mode. 

##### New #####
* **New LED IC's added**: We've added support for the following new LED IC's/protcols: CL28HH, SM16804, UCS2905. Also, the WS2805 (5ch) 


##### Added #####
* **Terminal 'Load Action'**:  Added 'reset group id' to the 'Load action' list.
* **Backup & Restore: Remove startup files**: Added a 'Remove startup files' button to easily remove a backup that has been created with 'Backup on SD-card'
* **My Devices: Firmware version**: You can now see the version of the firmware, when devices are online in 'My Devices'.
* **Alerts**: If you want to temporary dismiss any alert shown in the interface, to save space for example, you can just click on it.
* **Rename in IOconfig**: You can now quickly edit the name of the device, on the In-out configuration page. Just click on the name itself and it will rename the device.
* **Fader groups**: Similair to a folder with documents, you can now have 'presets' on the 'Fader' page. This will allow you to switch easily between certain scenario's or edit them later.

##### Changed #####
* **Current Date & Time added to LOG file**: Each LOG item on the SD-card, will now include the time & date, when the specific event happend. 


##### Improved #####
* **5 channel IC compatibility**: The built-incontent creation part, when working with a LED IC that has 5 channels is improved.
* **Password check**: If you create an account afterwards, now the same resrictions apply, like when you use the 'initial-setup' to create an account (1 uppercase, 1 lower-case, 1 number and 1 symbol)
* **Accounts: Admin/User Switch**: The view, when logging in as a user, is has been refined. An admin user can now easily switch to its account from the 3-dot menu.
* **Accounts: General**: Admins are able to use and configure accounts again, like before.


##### Fixed #####
* **Medium:Trigger: Speed slider action**: When you create a trigger, for the action 'Speed', the last postion of the speed slider, while dragging is correctly updated and saved.
* **Low: Deleting files**: Removing files in the File Browser, which are not located in the root directory, is fixed.
* **Medium: Color pallet**: While chosing a color from the color picker, the color pallette (the left and right circles) now update correctly again.
* **Low: Time watcher**:  If you're configuring a Time/Date input, at tiggers, you can use the 'eye' icon to watch the current time and date again.
* **Medium: Analog wachter/calibrate**: Both views, of calibrating and watching the analog channels, have been fine-tuned to be more intuitive and responsive.
* **Low: Playlists**: Deleting of multiple playlist is available again from the 'Playlist' page.
* **Low: Group triggering**: If you've selected a group for the 'output' device of the trigger, when editing afterwards, it was showing 'All devices' and gave the intention it wasnt been saved properly. However, this was only a visual bug: the trigger was executed on teh group itself. Now the 'output' device is correctly updated when editing a trigger.
* **Low: Extended group**: The default 'Extended group', when mixing 'Live' and 'Extended' now adds the correct devices to itself.

