## Release Notes for DiGidot Controller Software v3.2 - Released on January 28, 2026 ##

##### General #####
This is version 3.2.0 of DCS and it's available for every DiGidot controller. The main focus of this release is stability. We've received a lot of valuable feedback on previous releases like v3.0.3 and v3.1. For us, it's important that at its core, the software is reliable and can be used in 24/7 operation mode. 

##### New #####
* **New LED IC's added**: We've added support for the following new LED IC's/protocols: CL28HH, SM16804, UCS2905, and WS2805 (5ch).


##### Added #####
* **Terminal 'Load Action'**: Added 'reset group id' to the 'Load action' list.
* **Backup & Restore: Remove startup files**: Added a 'Remove startup files' button to easily remove a backup that has been created with 'Backup on SD-card'.
* **My Devices: Firmware version**: You can now see the firmware version when devices are online in 'My Devices'.
* **Alerts**: You can now temporarily dismiss any alert shown in the interface by simply clicking on it to save space.
* **Rename in IOconfig**: You can now quickly edit the device name on the In-out configuration page by clicking on the name itself.
* **Fader groups**: Similar to organizing documents in folders, you can now create 'presets' on the 'Fader' page. This allows you to easily switch between different scenarios or edit them later.

##### Changed #####
* **Current Date & Time added to LOG file**: Each LOG item on the SD-card now includes the time and date when the specific event happened. 


##### Improved #####
* **5 channel IC compatibility**: The built-in content creation functionality when working with 5-channel LED ICs has been improved.
* **Password check**: When creating an account, the same restrictions now apply as when using the 'initial-setup' to create an account (1 uppercase, 1 lowercase, 1 number, and 1 symbol).
* **Accounts: Admin/User Switch**: The view when logging in as a user has been refined. An admin user can now easily switch to their account from the 3-dot menu.
* **Accounts: General**: Admins are now able to use and configure accounts again as before.
* **Connectivity: IP-address**: When no IP-addresses are configured for multiple devices, you're now informed that for best performance, you need to configure an IP-address for every device.

##### Fixed #####
* **High: WiFi Password**: You can now set a password again when creating a WiFi network.
* **High: Playlist**: The playlist now properly advances to the next scene when triggered with the 'Next command'.
* **Medium: Trigger: Speed slider action**: When creating a trigger for the 'Speed' action, the last position of the speed slider while dragging is now correctly updated and saved.
* **Medium: DST Europe**: Setting the daylight saving time to Europe is fixed.
* **Low: Deleting files**: Removing files in the File Browser that are not located in the root directory has been fixed.
* **Medium: Color palette**: While choosing a color from the color picker, the color palette (the left and right circles) now updates correctly.
* **Low: Time watcher**: When configuring a Time/Date input for triggers, you can now use the 'eye' icon to view the current time and date.
* **Medium: Analog watcher/calibrate**: Both the calibration and monitoring views for analog channels have been fine-tuned to be more intuitive and responsive.
* **Low: Playlists**: Deleting multiple playlists is now available again from the 'Playlist' page.
* **Low: Group triggering**: When editing a trigger with a group selected for the 'output' device, the interface previously showed 'All devices', giving the impression it wasn't saved properly. However, this was only a visual bug—the trigger was correctly executed on the group. The 'output' device selection now displays correctly when editing a trigger.
* **Low: Extended group**: The default 'Extended group' when mixing 'Live' and 'Extended' modes now correctly adds the appropriate devices to itself.
* **Low: RDM with DMX-TTL**: RDM is now able to send/receive properly when using higher bitrates than standard DMX.

