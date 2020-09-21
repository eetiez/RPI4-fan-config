# RPI4-fan-config

This repository contains files to configure a Raspberry Pi 4 fan. This work is based on files provided with [Argon ONE RPi4 case](https://www.argon40.com/argon-one-raspberry-pi-4-case.html).

## Prerequisite

I2C must be enable. For those running Archlinux ARM image, instructions are given on [this page](https://archlinuxarm.org/platforms/armv6/raspberry-pi).

## How to use it ?

Simply copy `fan.service` and `fan.py` at the right place and adjust permissions.

```bash
cp fan.service /lib/systemd/system/
chmod 644 /lib/systemd/system/fan.service
cp fan.py /usr/local/sbin/
chmod 755 /usr/local/sbin/fan.py
```