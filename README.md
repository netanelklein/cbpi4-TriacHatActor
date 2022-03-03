# Triac Hat Actor for CraftBeerPi 4

This is a plugin for using Waveshare's 2CH Triac Hat for controlling actors in CraftBeerPi 4. You can find the documentation for this device here: https://www.waveshare.com/wiki/2-CH_TRIAC_HAT

This device is used for voltage regulation using a triac and have two channels for different actors.

## Installation

You can install this package via Pypi.org using this command:

```bash
sudo pip3 install cbpi4-TriacHatActor
```

Alternatively you can download it using this command:

```bash
sudo pip3 install git+https://github.com/netanelklein/cbpi4-TriacHatActor.git
```

In order to do so you have to have Git installed on your system. You can do this simply by using the command:

```bash
sudo apt install git
```
### Activating plugin in CraftBeerPi

In order for the plugin to show up in your CraftBeerPi system, you have to activate the plugin using this command:
```bash
cbpi add cbpi4-TriacHatActor
```

### System configuration

You will have to enable the Interface that you want to use in raspi-config. in order to get there, use this command:
```bash
sudo raspi-config
```
 Then go to **Interface Options** and then to **Serial Port**. There you should choose **no** for *let login shell be accessible over serial* and **yes** for *Would you like the serial port hardware to be enabled?*

If you want to use the I2C interface, you should enable it from the **Interface Options** under **I2C**. I personally haven't tried to use the Triac Hat with I2C, so there may be bugs there.

## Parameters

* **Channel** - Choose which of the Triac Hat channels you want to assign to this actor.
* **Interface** - Choose between UART and I2C. Default is UART. Be aware that you must choose the same interface for all the actors that are connected to the Triac Hat.
* **Device Port** - Choose the serial port in which the triac is connected. Usually it's /dev/ttyS0 or /dev/ttySerial0, so choose this if you're not sure.
* **Frequency** - Your line frequency. 50 Hz is default as it is the most popular frequency around the world. In the US the frequency is 60 Hz.