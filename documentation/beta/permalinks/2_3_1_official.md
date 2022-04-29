## Release notes for DiGidot C4 Firmware v2.3.1 - Published on XX XXX 2022 ##

### New ###
* LED IC TM1934
* Loading device data parallel: With the release of the PxLNet Node, we saw the need to improve our total loading time, especially when you connect multiple devices to each other. The load time is the time it takes to get all the Input/Output/ Network configuration, scenes, triggers etc. from all devices. With this improvement, the load time is dramatically reduced, if all devices have their own IP-address. Till now, if you have 20 devices, and each device required 5 seconds to load, the total loading time would be 100 seconds.
With this update, the total time will be reduced to the loading time of about 1 device, which is 5 seconds. Basically, the device that takes the longest time to load, it will roughly take that amount of time, to load the data of all devices, regardless of the total number of devices. 

### Improved ###
* Art-Net performance: If the input/output configuration only contains Art-Net universes to listen on, sACN will now be completely disabled  instead of going to stand-by mode. This way, if only Art-Net is being used on the DiGidot controller, but in the same network, sACN is used for something else, a negative effect on performance is prevented.
* Memory allocation: If the DiGidot controller needs to allocate some memory, for example, when creating a trigger, the function that is responsible for actually checking if the requested memory is available, wasn't working properly and returned no error. This way, the function that requested memory, asserted that the memory was available but in reality, it wasn't. This could let to some random crashes (red/white status LED) that weren't traceable for anybody. This has been resolved now.
* JSON file parsing: The DiGidot controller now actively shows an error (red light on the controller and create an error log entry) if any JSON file (trigger/ configuration etc.) failed to read correctly.
* FPS monitor: Both the input and output FPS counter are rewritten and now shows much more accurate numbers on the Monitor and Diagnosic page.
* UX: The network page has been completely rewritten so a lot of (small) UX bugs have been fixed with this.
* UX: On the Device page, while retrieving the actual time, the Daylight Saving Time (DST) parameter will also be shown.
* UX: The layout on the Network page has some fine adjustments done.
* UX: The process of automatically add/change/remove an IOelement because an IO trigger listen on an different universe is now more robust.
* UX: Dark theme in general has gotten a few tweaks on various pages.

### Changed ###
* General: Product name references 'PxLNode' changed to 'PxLNet Node'.
* Recording: Number of unique input universes is going up from 14 to 16 universes
* Recording: The alert with 'FPS too low' (shown when the average input FPS, before recording, is below 50) has changed from a warning (yellow background) to a note (blue background. The note just indicates to the user, that the recording could be more smooth, if you increase the input FPS. But this is not always possible or required.
* UX: At the trigger page, when creating or editing a trigger, the number of (sub)devices is now correctly calculated, taking the bays into account.

### Fixed ###
* (High) Getting Started: Now works again if you don't have a DiGidot C4 Extended in your network.
* (Medium) Output API call: When requesting output data from a particular port, the DiGidot Controller doesn't crash anymore if the 'offset' parameter is larger than the 'length' parameter.
* (Medium) Highlight: When highlighting a output port, then 10 minutes after the highlight has been stopped, the output performance was dramatically decreased. This has been resolved.
* (Medium) License: Fixed some bugs, and prevent an interface reload loop, if a temporary license is active.
* (Medium) sACN: Streaming ACN now works correctly when synchronisation is enabled.
* (Low) Scene Generator (Beta): The preview function works again.
* (Low) WiFi: When switching the WiFi mode from Access Point to Client, it now returns the correct error 'password incorrect' instead of 'busy' or 'unknown'.
* (Medium) UX: Interface can be used again from a Firefox browser.
* (Low) UX: The interface now correctly checks  if DiGidot controllers have different accounts on them and gives the option to add the missing ones of delete them.
* (Low) UX: Reloading the Quick-Edit, when changes are made, won't give an 'unsaved' message anymore.
* (Low) Accounts: When you try to restore an account with a password of 3 characters or less, it won't fail anymore.
* (Medium) UX: On the trigger page, the current OSC and UDP settings are now correctly shown.
* (Medium) UX: If only the a single PxLNet Node is present, the update functionality now works again.
* (Low) RDM: The DiGidot controller could crash in some circumstances when a RDM parameter is parsed. This has been solved.
* (Low) UX: On the Input/output config page, you can once again, divide a DMX output of 512 channels into multiple universes.
* (Low) UX: Cloning a trigger works again.
