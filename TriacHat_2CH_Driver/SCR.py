#!/usr/bin/python
# -*- coding:utf-8 -*-

import logging
import time

import os
import sys
libdir = os.path.dirname(os.path.realpath(__file__))
if os.path.exists(libdir):
    sys.path.append(libdir)

import config

CH_EN=[0x57,0x68,0x02,0x00,0x00,0x00]


class SCR:
    def __init__(self, Baudrate = 115200, dev = "/dev/ttyS0", data_mode = 1, address=0x47):
        self.address = address
        self.data_mode = data_mode  #1 :uart   0: i2c
        self.Baudrate = Baudrate
        self.dev = dev
        self.com = config.config(Baudrate , dev , data_mode, address)
    
    def SendCommand(self, Data):
        if(self.data_mode == 1):
            #Data[6] = '\0'
            #self.com.UART_SendString(Data);
            self.com.UART_SendnByte(Data,6)
        if(self.data_mode == 0):    # 0: i2c
            self.com.I2C_SendWord(Data[2],(Data[3]) | (Data[4]<<8))
        time.sleep(0.01)
    
    def SET_Check_Digit(self, Data):
        return  ((((Data[0]^Data[1])^Data[2])^Data[3])^Data[4])
    def SetMode(self, Mode):
        ch=[0x57,0x68,0x01,0x00,0x00,0x00]
        ch[4] = Mode&0x01
        ch[5] = self.SET_Check_Digit(ch)
        self.SendCommand(ch)

    def ChannelEnable(self, Channel):
        if(Channel == 1):
            CH_EN[4] = 0x01|CH_EN[4]
            CH_EN[5] = self.SET_Check_Digit(CH_EN)
            self.SendCommand(CH_EN)
        elif(Channel == 2):
            CH_EN[4] = 0x02|CH_EN[4]
            CH_EN[5] = self.SET_Check_Digit(CH_EN)
            self.SendCommand(CH_EN)
    
    def ChannelDisable(self,Channel):
        if(Channel == 1):
            CH_EN[4] = 0xfe & CH_EN[4]
            CH_EN[5] = self.SET_Check_Digit(CH_EN)
            self.SendCommand(CH_EN)
        elif(Channel == 2):
            CH_EN[4] = 0xfd & CH_EN[4]
            CH_EN[5] = self.SET_Check_Digit(CH_EN)
            self.SendCommand(CH_EN)
        
    def VoltageRegulation(self, Channel,  Angle):
        Angle1=[0x57,0x68,0x03,0x00,0x00,0x00]
        Angle2=[0x57,0x68,0x04,0x00,0x00,0x00]
        if(Channel == 1):
            Angle1[4] = Angle
            Angle1[5] = self.SET_Check_Digit(Angle1)
            self.SendCommand(Angle1)
        elif(Channel == 2):
            Angle2[4] = Angle
            Angle2[5] = self.SET_Check_Digit(Angle2)
            self.SendCommand(Angle2)
        
    def GridFrequency(self, Hz):
        Frequency=[0x57,0x68,0x05,0x00,0x32,0x00]
        if(Hz == 50 or Hz ==60):
            Frequency[4] = Hz
            Frequency[5] = self.SET_Check_Digit(Frequency)
            self.SendCommand(Frequency)
        
    def Reset(self, Delay):
        ch=[0x57,0x68,0x06,0x00,0x00,0x00]
        ch[4] = Delay & 0xff
        ch[3] = Delay >> 8
        ch[5] = self.SET_Check_Digit(ch)
        self.SendCommand(ch)

        
    

