# Smart-Parking-Using-IOT

# Smart Parking System using IoT

This project implements a smart parking system using Internet of Things (IoT) technology. It utilizes Raspberry Pi, Ubidots, and GPIO sensors to monitor and update the occupancy status of parking slots in real-time.

## Table of Contents

- [Introduction](#introduction)
- [Hardware Requirements](#hardware-requirements)
- [Software Requirements](#software-requirements)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)

## Introduction

The Smart Parking System project aims to provide real-time information about the availability of parking slots. This system helps users easily find vacant parking slots, thereby reducing the time spent searching for parking and optimizing the utilization of parking spaces.

## Hardware Requirements

- Raspberry Pi (any model with GPIO pins)
- Two GPIO sensors
- Jumper wires
- Breadboard (optional)

## Software Requirements

- Python 3
- RPi.GPIO library
- Ubidots library

## Setup and Installation

1. **Install Python 3:** Ensure you have Python 3 installed on your Raspberry Pi.
2. **Install RPi.GPIO library:** 
   ```bash
   sudo apt-get install python3-rpi.gpio
   ```
3. **Install Ubidots library:** 
   ```bash
   pip install ubidots
   ```
4. **Connect the GPIO sensors:**
   - Connect the first sensor to GPIO pin 13.
   - Connect the second sensor to GPIO pin 19.

## Usage

1. **Run the code:** Save the provided code in a Python file (e.g., `smart_parking.py`) and execute it.
   ```bash
   python3 smart_parking.py
   ```
2. The system will continuously monitor the parking slots and print the status of each slot (Engaged/Vacant) in the console.
3. The status of each slot is also updated in real-time on the Ubidots cloud platform.

This code monitors the status of two parking slots using GPIO sensors connected to a Raspberry Pi. It updates the status in real-time both in the console and on the Ubidots cloud platform.

