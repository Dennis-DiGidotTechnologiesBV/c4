## Release notes for DiGidot Controller Firmware v2.3.0 - Published on 16th of December 2021 ##

### New ###
* **PxLNet Node support**: Our very latest product release, the new DiGidot PxLNet Node is shipped with this version where the interface has been fully optimized for this variant.
* **GPIO output**: We've added a feature where you can set a GPIO output 0 volt or 12 volt. This GPIO output is located on analog channel 1 and is available if this channel isn't used in a trigger. On the PxLNet Node, there's a second GPIO output (open-drain type) available which is, just like GPIO output 1, four times present on the D-sub connector which makes a total of 8 GPIO outputs. 
* **Diagnostics**: Before this release, we already had some basic diagnostic information which could be found on the Monitor page. But now, we have much more: detailed RAM usage, processing time of each universe, Ethernet switch statistics, playback information, any many many more! Keep in mind this first version is primarily developed for mechanics which means there is little to no explanation about what every parameter means or what value is good of bad. But it allows us, as the developers, and mechanics, to help customers more effectively in case there are problems with the system.

### Improved ###
* Discover: If the PxLNet Node is low on usable memory, the interface will request less devices to discover so the discover process itself can be completed successfully.

### Changed ###
* Manual: The manual has been updated for the DiGidot PxLNet Node.
