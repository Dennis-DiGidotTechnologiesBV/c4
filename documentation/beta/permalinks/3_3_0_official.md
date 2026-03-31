## Release notes for DiGidot Controller Software v3.3.0 - Published on 4 of March 2026 ##

##### New #####
* **Fixture Library**: Experience a new way of configuring outputs for your project. We've collaborated with several manufacturers to allow selecting fixtures instead of individual LED ICs.
* **Triggers: Stop fade**: You can now configure a trigger to not only start a scene with a fade, but also stop it with a fade.
* **LED IC: SM15055e**: Added support for the SM15055e LED IC.
* **Colorpicker**: Added two additional options for selecting colors when generating a scene.

##### Improved #####
* **Triggers: Time & Date display**: Trigger time and date are now shown more clearly, including trailing zeros where needed.

##### Fixed #####
* **High: Firmware alignment**: Improved firmware alignment to prevent freezes during operation.

* **Medium: DMX Programmer**: Programming in DMX512 mode is working correctly again.
* **Medium: IOconfig**: Global settings now behave as expected.
* **Medium: DMX Programmer**: Duplicate channels are now correctly configured.
* **Medium: DST**: Selecting daylight saving time for Europe or USA now works properly.
* **Low: Developer**: Device model ID can now be cleared successfully again.

* **Low: Backup & Restore**: Fixed an issue where the DHCP server field was not set correctly after restoring a backup.
* **Low: IOconfig**: The value 'max_time_until_resend' is now saved correctly.