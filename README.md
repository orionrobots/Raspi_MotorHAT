# Raspi_MotorHAT

My enhancements on the MotorHAT Code.

## MotorHAT

The MotorHAT - also known as "Full Function Stepper Controller" is a Raspberry Pi hat that seems to be commonly available on the internet. The device uses the PCA9685 16 channel servo or I2C to PWM driver chip. 

The hat is a very handy one, with a lot of the functions of the AdaFruit stepper hat:

* Control 4 DC motors or 2 Stepper motors.
* Control 4 servo motors.
* Cutouts for access to CSI camera interface and DSI display interface.
* Motor power inputs.

But with some different features:

* I2c breakout.
* IR input.
* GPIO through connector - you can stack these, just watch the i2C address.
* Fully assembled - no soldering needed.
* Does NOT come with the handy prototyping area on the Adafruit HAT.

## Using this library

Prerequisites:

    sudo apt-get install python3-smbus i2c-tools
    
Install the library on the Raspberry Pi with:
  
    pip install git+https://github.com/orionrobots/Raspi_MotorHAT
  
To use a DC motor connected to M1:

    from Raspi_MotorHAT import Raspi_MotorHAT
    mh = Raspi_MotorHAT(addr=0x6f)
    motor = mh.getMotor(1)
  
To set its speed:

    motor.setSpeed(150)
  
To set it's direction:

    motor.run(Raspi_MotorHAT.FORWARD)
  
Directions are FORWARD, BACKWARD and RELEASE. Speed is a positive integer and varies from 0 to 255.

Using a servo motor connected to channel 1, see the example under https://github.com/orionrobots/Raspi_MotorHAT/blob/master/Raspi_MotorHAT/ServoTest.py.

## Why it exists and accrediting Adafruit

Finding sample code, a library and documentation has proven to be tricky. I am summarising and enhancing what I've found here. I claim no personal license or ownership. The original code was found at https://sourceforge.net/projects/u-geek/files/HATs/Raspi_MotorHAT/.

The code appears to be derivative from the Adafruit Stepper hat code, with some changes in naming and I2C addresses, so I've also made this an MIT licensed repo. Here is their license in full:

> Adafruit Python Library for DC + Stepper Motor HAT
> Python library for interfacing with the Adafruit Motor HAT for Raspberry Pi to control DC motors with speed control and Stepper motors with single, double, interleave and microstepping.
>
> Designed specifically to work with the Adafruit Motor Hat
>
> ----> https://www.adafruit.com/product/2348
>
> Adafruit invests time and resources providing this open source code, please support Adafruit and open-source hardware by purchasing products from Adafruit!
>
> Written by Limor Fried for Adafruit Industries. MIT license, all text above must be included in any redistribution
>

## What I am adding

* Making the code browsable, not just a tarball somewhere.
* Adding python package setup files - you can install this.

## Roadmap

* I plan to try make it Py2/3 Polyglot. This code is Python 2 only.
