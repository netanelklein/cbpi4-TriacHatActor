
# -*- coding: utf-8 -*-
from cProfile import label
import os
from pickle import TRUE
from aiohttp import web
import logging
from unittest.mock import MagicMock, patch
import asyncio
import random
from cbpi.api import *
import serial.tools.list_ports as lp
from TriacHat_2CH_Driver import SCR

logger = logging.getLogger(__name__)

@parameters([Property.Select(label="Channel", options=[1,2], description="Select which channel you want to assign as this actor"),
             Property.Select(label="Interface", options=["UART", "I2C"], description="Select which interface your Triac Hat is using. (Deafult is UART)"),
             Property.Select(label="Device Port", options=[port.device for port in lp.comports(True)]),
             Property.Select(label="Frequency", options=[50, 60], description="Frequency in Hz (Deafult is 50Hz)")])
class TriacHat(CBPiActor):

    @action("Set Power", parameters=[Property.Number(label="Power", configurable=True, description="Power Setting [0-100]")])
    async def setpower(self, Power=100, **kwargs):
        logging.info(Power)
        self.power = int(Power)
        if self.power < 0:
            self.power = 0
        if self.power > 100:
            self.power = 100
        await self.set_power(self.power)
    
    # Initializing plugin variables
    async def on_start(self):
        self.power = None
        self.ch = int(self.props.get("Channel"))
        self.interface = 0 if self.props.get("Interface") == "I2C" else 1
        self.dev = self.props.get("Device Port")
        self.freq = self.props.get("Frequncy", 50)
        self.switch = SCR.SCR(dev=self.dev, data_mode=self.interface)
        self.switch.GridFrequency(self.freq)
        self.state = False

    async def on(self, power = None):
        if power is not None:
            self.power = power
        else:
            self.power = 100
        await self.set_power(self.power)
        logger.info("Triac Hat actor %s ON - Channel %s - Power %s" % (self.id, self.ch, self.power))
        self.state = True

    async def off(self):
        self.set_power(0)
        logger.info("Triac Hat actor %s OFF - Channel %s " % (self.id, self.ch))
        self.state = False
        
    async def set_power(self, power):
        self.power = power
        if self.state == True and power == 0:
            self.switch.ChannelDisable(self.ch)
        elif power > 0:
            if self.state == False:
                self.switch.ChannelEnable(self.ch)
            self.switch.VoltageRegulation(self.ch, round(power*1.79))   # Still need to check how exactly the angle works. assuming 0 is off and 179 is 100%
        await self.cbpi.actor.actor_update(self.id, power)
    
    def get_state(self):
        return self.state
    
    async def run(self):
        while (self.running) == True:
            await asyncio.sleep(1)


def setup(cbpi):
    cbpi.plugin.register("TriacHatActor", TriacHat)
    pass