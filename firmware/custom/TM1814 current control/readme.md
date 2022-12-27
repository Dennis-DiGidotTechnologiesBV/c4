<div align="center">

  <h3 align="center">TM1814 Current Control</h3>
</div>

## About this firmware 
This firmware can limit the output current if you're using the TM1814 LED IC. This LED IC has 64 steps to limit the current of the individual colors (RGBW). There is a custom interface to config the current limiter and also to save the values and apply at startup of the DiGidot Controller.

**This firmware is tested and suitable for a 24/7 operation**

## Difference

#### With 1 universe
Regular FW: 40 FPS / Custom FW: 100 FPS


## Installation

* Install the custom firmware. 
* Select the TM1814 as the output protocol.
* Allow HTTP-Get triggers by going to the interface of the DiGidot controller -> Triggers -> In the top-right -> 3 dots -> HTTP/UDP/OSC 
* Enable the HTTP-Get toggle


## Usage

To actually change the current, you type in the IP-address of the DiGidot controller and then add /tm1814_current/index.html

user_interface_tm1814_current_control.png

 [![User interface TM1814 current control](https://github.com/Dennis-DiGidotTechnologiesBV/c4/blob/master/firmware/custom/TM1814%20current%20control/user_interface_tm1814_current_control.png)](https://github.com/Dennis-DiGidotTechnologiesBV/c4/blob/master/firmware/custom/TM1814%20current%20control/user_interface_tm1814_current_control.png)


## Changelog
21-12-2022: Third version (version 1 and 2 are for internal use)
