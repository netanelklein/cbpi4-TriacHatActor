# Triac Hat Actor for CraftBeerPi 4

This is a plugin for using Waveshare's 2CH Triac Hat for controlling actors in CraftBeerPi 4. You can find the documentation for this device here: https://www.waveshare.com/wiki/2-CH_TRIAC_HAT

This device is used for voltage regulation using a triac and have two channels for different actors.

## Installation

As of right now this plugin is not availble via pypi. You can download it using this command in the command line:

`sudo pip3 install git+https://github.com/netanelklein/cbpi4-TriacHatActor.git`

In order to do so you have to have Git installed on your system. You can do this simply using the command:

`sudo apt install git`

You will have to enable the Interface that you want to use in reaspi-config. in order to get there, simply type `sudo raspi-config` in the command line. Then go to **Interface Options** and then to **Serial Port**. There you should choose **no** for *let login shell be accessible over serial* and **yes** for *Would you like the serial port hardware to be enabled?*.

If you want to use the I2C interface, you should enable it from the **Interface Options** under **I2C**. I personally haven't tried to use the Triac Hat with I2C, so there may be bugs there.

## parameters

* **Channel** - Choose which of the Triac Hat channels you want to assign to this actor.
* **Interface** - Choose between UART and I2C. Default is UART. Be aware that you must choose the same interface for all the actors that are connected to the Triac Hat.
* **Device Port** - Choose the serial port in which the triac is connected. Usually it's /dev/ttyS0 or /dev/ttySerial0, so choose this if you're not sure.
* **Frequency** - Your electricity frequency. 50 Hz is defauld as it is the most popular frequency around the world. In the US the frequency is 60 Hz.