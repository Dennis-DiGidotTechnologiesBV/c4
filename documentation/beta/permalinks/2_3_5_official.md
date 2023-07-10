## Changelog for DiGidot Controller Firmware v2.3.5 - Built on 10 of July 2023 ##

### Added ###
* LED IC: TM1824

### Improved ###
* sACN: The DiGidot controller now checks the startcode byte of the sACN traffic and every packet will be discarded unless the startcode is 0.