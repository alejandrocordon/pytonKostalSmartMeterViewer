#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  Purpose:
#           Query values from Kostal Smart Energy Meter
#
#  Based on the documentation provided by Kostal:
#  https://www.kostal-solar-electric.com/de-de/download/-/media/document-library-folder---kse/2019/05/09/13/57/ba_kostal_interface_ksem---201905.pdf
#
# Requires pymodbus
# Tested with:
#
# Please change the IP address of your Inverter (e.g. 192.168.1.99 and Port (default 1502) to suite your environment - see below)
#

import pymodbus
from pymodbus.client.sync import ModbusTcpClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pprint import pprint
import time
import sense_hat

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class kostal_em_query:
    def __init__(self):
        #Change the IP address and port to suite your environment:
        self.inverter_ip="192.168.1.97"
        self.inverter_port="502"
        #No more changes required beyond this point
        self.KostalRegister = []
        self.Adr0=[]
        self.Adr0=[0]
        self.Adr0.append("Active power+")
        self.Adr0.append("U32")
        self.Adr0.append(0)

        self.Adr2=[]
        self.Adr2=[2]
        self.Adr2.append("Active power-")
        self.Adr2.append("U32")
        self.Adr2.append(0)


    #-----------------------------------------
    # Routine to read a string from one address with 8 registers
    def ReadStr8(self,myadr_dec):
        r1=self.client.read_holding_registers(myadr_dec,8,unit=71)
        STRG8Register = BinaryPayloadDecoder.fromRegisters(r1.registers, byteorder=Endian.Big)
        result_STRG8Register =STRG8Register.decode_string(8)
        return(result_STRG8Register)
    #-----------------------------------------
    # Routine to read a Float from one address with 2 registers
    def ReadFloat(self,myadr_dec):
        r1=self.client.read_holding_registers(myadr_dec,2,unit=71)
        FloatRegister = BinaryPayloadDecoder.fromRegisters(r1.registers, byteorder=Endian.Big, wordorder=Endian.Big)
        result_FloatRegister =round(FloatRegister.decode_32bit_float(),2)
        return(result_FloatRegister)
    #-----------------------------------------
    # Routine to read a U16 from one address with 1 register
    def ReadU16_1(self,myadr_dec):
        r1=self.client.read_holding_registers(myadr_dec,1,unit=71)
        U16register = BinaryPayloadDecoder.fromRegisters(r1.registers, byteorder=Endian.Big, wordorder=Endian.Big)
        result_U16register = U16register.decode_16bit_uint()
        return(result_U16register)
    #-----------------------------------------
    # Routine to read a Int32 from one address with 1 register
    def ReadInt32(self,myadr_dec):
        r1=self.client.read_holding_registers(myadr_dec,2,unit=71)
        U32register = BinaryPayloadDecoder.fromRegisters(r1.registers, byteorder=Endian.Big, wordorder=Endian.Big)
        result_U32register = U32register.decode_32bit_int()
        return(result_U32register)
    #-----------------------------------------
	# Routine to read a UInt64 from one address with 1 register
    def ReadUInt64(self,myadr_dec):
        r1=self.client.read_holding_registers(myadr_dec,4,unit=71)
        U64register = BinaryPayloadDecoder.fromRegisters(r1.registers, byteorder=Endian.Big, wordorder=Endian.Big)
        result_U64register = U64register.decode_64bit_uint()
        return(result_U64register)
    #-----------------------------------------
    # Routine to read a U16 from one address with 2 registers
    def ReadU16_2(self,myadr_dec):
        r1=self.client.read_holding_registers(myadr_dec,2,unit=71)
        U16register = BinaryPayloadDecoder.fromRegisters(r1.registers, byteorder=Endian.Big, wordorder=Endian.Big)
        result_U16register = U16register.decode_16bit_uint()
        return(result_U16register)
    #-----------------------------------------
    # Routine to read a U32 from one address with 2 registers
    def ReadU32(self,myadr_dec):
        r1=self.client.read_holding_registers(myadr_dec,2,unit=71)
        #print ("r1 ", rl.registers)
        U32register = BinaryPayloadDecoder.fromRegisters(r1.registers, byteorder=Endian.Big, wordorder=Endian.Big)
        #print ("U32register is", U32register)
        #result_U32register = U32register.decode_32bit_float()
        result_U32register = U32register.decode_32bit_uint()
        return(result_U32register)
    #-----------------------------------------
    def ReadU32new(self,myadr_dec):
        print ("I am in ReadU32new with", myadr_dec)
        r1=self.client.read_holding_registers(myadr_dec,2,unit=71)
        U32register = BinaryPayloadDecoder.fromRegisters(r1.registers, byteorder=Endian.Big, wordorder=Endian.Big)
        result_U32register = U32register.decode_32bit_uint()
        return(result_U32register)
    #-----------------------------------------
    # Routine to read a U32 from one address with 2 registers
    def ReadS16(self,myadr_dec):
        r1=self.client.read_holding_registers(myadr_dec,1,unit=71)
        S16register = BinaryPayloadDecoder.fromRegisters(r1.registers, byteorder=Endian.Big, wordorder=Endian.Big)
        result_S16register = S16register.decode_16bit_uint()
        return(result_S16register)


    try:
        def run(self):

            self.client = ModbusTcpClient(self.inverter_ip,port=self.inverter_port)
            self.client.connect()

            # LONG List of reads...
            self.Adr0[3]=self.ReadU32(self.Adr0[0])*0.1
            self.Adr2[3]=self.ReadU32(self.Adr2[0])*0.1


            self.KostalRegister=[]
            self.KostalRegister.append(self.Adr0)
            self.KostalRegister.append(self.Adr2)

            self.client.close()


    except Exception as ex:
            print ("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            print ("XXX- Hit the following error :From subroutine kostal_em_query :", ex)
            print ("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
#-----------------------------



if __name__ == "__main__":
    sense = sense_hat.SenseHat()
    sense.set_rotation(90)
    sense.low_light = True

    green = (0, 255, 0)
    red = (255, 0, 0)
    black = (0, 0, 0)
    white = (255, 255, 255)
    yellow = (255, 204, 0)

    max_value = 3000 #watios



    while (True):
        try:
            Kostalvalues =[]
            Kostalquery = kostal_em_query()
            Kostalquery.run()
        except Exception as ex:
            print ("Issues querying Kostal Smart Energy Meter -ERROR :", ex)

        for elements in Kostalquery.KostalRegister:
            print (elements[1], elements[3])
        totalActivePower = round(Kostalquery.KostalRegister[0][3] - Kostalquery.KostalRegister[1][3])
        pixels_value = 64 * totalActivePower / max_value

        if totalActivePower > 0:
            pixels = [black if i < 64 - pixels_value else red for i in range(64)]
            sense.show_message(str(totalActivePower)+"W", text_colour=(255, 0, 0), back_colour=(0, 0, 0))
            print(bcolors.FAIL + str(totalActivePower)+"W" + bcolors.ENDC)
        elif totalActivePower == 0:
            pixels = [black for i in range(64)]
            sense.show_message(str(totalActivePower)+"W", text_colour=(255, 204, 0), back_colour=(0, 0, 0))
            print(bcolors.WARNING + str(totalActivePower)+"W" + bcolors.ENDC)
        else:
            pixels = [black if i < 64 - pixels_value else green for i in range(64)]
            sense.show_message(str(totalActivePower)+"W", text_colour=(0, 255, 0), back_colour=(0, 0, 0))
            print(bcolors.OKGREEN + str(totalActivePower)+"W" + bcolors.ENDC)

        time.sleep(0.5)
        pprint(pixels)
        sense.set_pixels(pixels)
        time.sleep(5)


