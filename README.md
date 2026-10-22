# IPOD-HALFLIFE
A simple working iPod

**Overview**

This project was completed for the Hack Club's first week of Half Life. It also includes the materials for week 2, the enclosure. The first part is a PCB. The PCB is powered by an ESP-32 and uses a PCM5011 chip to turn mono audio into high-quality stereo audio. It includes an OLED screen to display songs and menus for navigation. It outputs via a normal 3.5mm audio jack, and it also outputs via Bluetooth (wireless headphones or earbuds). It can accept a microSD for storage and uses USB-C to charge and program the ESP. It features 5 individual buttons in a standard menu navigation layout to perform a variety of actions.

This PCB was designed in EasyEDA STD for Windows. It features many components that are listed below

**Components**
* ESP32-PICO-MINI-02-N8R2 (Microcontroller)
* 10μF Capacitor **x8** (Basic Component)
* 100nF Capacitor **x5** (Basic Component)
* 10μF Capacitor (Basic Component)
* Red LED and Green LED (Basic Component)
* 5.1KΩ Resistor **x2** (Basic Component)
* 100Ω Resistor **x2** (Basic Component)
* 47Ω Resistor (Basic Component)
* 10KΩ Resistor **x11** (Basic Component)
* BUTTON-4X3X2.5 **x7** (Input)
* 100SP1T1B1M1QEH (Input)
* PCM5102APWR (Audio Control)
* PJ-320A-4P DIP (Output)
* TP4056-MS (Battery Control)
* XC6220B331MR-MS (Battery Control)
* HC-TYPE-C-16P-026W (Power Input)
* HS20HS072RX (Display)
* HX TF PUSH (Storage)
* 2KΩ Resistor (Basic Component)

The total materials list with everything is in the BOM

<img width="339" height="366" alt="PCB_PCB_halflife01_2026-10-09-color" src="https://github.com/user-attachments/assets/dba164ca-e9d2-48d8-a56a-68c64bf8eb0a" />
<img width="339" height="366" alt="PCB_PCB_halflife01_2026-10-09" src="https://github.com/user-attachments/assets/0864c6fa-d8d2-4dfc-81b1-bbe35fe212aa" />
<img width="1169" height="827" alt="Schematic_halflife01_2026-10-09" src="https://github.com/user-attachments/assets/500480ec-1689-4467-b3ef-8960f40071a7" />

