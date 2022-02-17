
# -*- coding: utf-8 -*-
from cProfile import label
from msilib.schema import Property
import os
from pickle import TRUE
from aiohttp import web
import logging
from unittest.mock import MagicMock, patch
import asyncio
import random
from cbpi.api import *
import serial.tools.list_ports as lp

logger = logging.getLogger(__name__)

mode = GPIO.getmode()
if (mode == None):
    GPIO.setmode(GPIO.BCM)

@parameters([Property.Select(label="Channel", options=[1,2]),
             Property.Select(label="Interface", options=["UART", "I2C"], description="Select which interface your Triac Hat is using. (Deafult is UART)"),
             Property.Select(label="Device Port", options=[port.device for port in lp.comports(True)])])
class TriacHat(CBPiActor):

    @action("Set Power", parameters=Property.Number(label="Power", configurable=True, description="Power Setting [0-100]"))
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
        self.interface = 0 if (self.props.get("Interface")) == "I2C" else 1
        self.dev = self.props.get("Device Port")
        self.state = False

    async def on(self, power = None):
        if power is not None:
            self.power = power
        else:
            self.power = 100
        await self.set_power(self.power)
        logger.info("Triac Hat actor %s ON - Channel %s " % (self.id, self.ch))
        self.state = True

    async def off(self):
        self.set_power(0)
        logger.info("Triac Hat actor %s OFF - Channel %s " % (self.id, self.ch))
        self.state = False
        
    async def set_power(self, power):
        pass
    
    def get_state(self):
        return self.state
    
    async def run(self):
        while (self.running) == True:
            await asyncio.sleep(1)


def setup(cbpi):
    cbpi.plugin.register("TriacHatActor", TriacHat)
    pass