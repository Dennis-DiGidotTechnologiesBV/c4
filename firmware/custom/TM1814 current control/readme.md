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
* Factory-Reset the DiGidot controller.
* Select the TM1814 as the output protocol.
* Allow HTTP-Get triggers by going to the interface of the DiGidot controller -> Triggers -> In the top-right -> 3 dots -> HTTP/UDP/OSC 
* Enable the HTTP-Get toggle

Keep in mind that by default, all the current values are 0 and the output will be disabled untill you access the TM1814 user interface page. Continue readingto do that.

## Usage

To actually change the current, you type in the IP-address of the DiGidot controller and then add '/tm1814_current/index.html' to the url. So for example, if the IP-address of the DiGidot controller is 10.254.254.254 then the full URL would be 'http://10.254.254.254/tm1814_current/index.html' .

 [![User interface TM1814 current control](https://github.com/Dennis-DiGidotTechnologiesBV/c4/blob/master/firmware/custom/TM1814%20current%20control/user_interface_tm1814_current_control.png)](https://github.com/Dennis-DiGidotTechnologiesBV/c4/blob/master/firmware/custom/TM1814%20current%20control/user_interface_tm1814_current_control.png)

There are 4 sliders where you can control between 0 and 63. If you want to have these value persist after a power cycle, press the 'Save values to flash memory'. The values will be saved untill you delete the IOconfiguration again! You can also retrieve the actual current values by clicking the 'Get current values'.

## Actual current values

The value that you can set for the current (0-63) is not the actual current you set in mA for the LED IC. For that, we've done some tests on the OneEightyOne LED Strip 31520 (or 3152001) and we measured each step, how it effects the actual current of the LED IC. The results are stored in the excel sheet that's listed in this folder.

## Changelog
21-12-2022: Third version (version 1 and 2 are for internal use)
