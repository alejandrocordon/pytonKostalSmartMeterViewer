# pytonKostalSmartMeterViewer-

If you have a Kostal Smart Metter you can have a ticket to check the Power origin and the quantity of ha Kostal Smart meter.
Normally this is used when you have a solar power supply and the energy net power supply. 

If the installation is using the energy net power supply it will be shown as color red and an amount of points from 0 to max_power value.
If the power comes from the solar pannels it will be shown on green. 

You need: 
Get sense hat
Get Raspberry Pi 


1. Install sense hat

sudo apt update
sudo apt install senese-hat
sudo reboot

2. Install   dependecies

pip3 install pymodbus

3. Put it on  /home/'user'/    directory

python3 main.py

![Game Process](https://github.com/sodapop/pytonKostalSmartMeterViewer-/blob/master/funcionamiento.gif)
![Kostal Smart Metter](https://github.com/sodapop/pytonKostalSmartMeterViewer-/blob/master/vatimetro.jpg.jpg)
