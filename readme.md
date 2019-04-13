# BLE Scanner in Python

A basic scanner to pick up data from Bluetooth Low Energy (BLE) devices.

It uses the pygatt libary to simplify operating the bluetooth adapter.

This version is set up sepcifically to handle data from multiple Jinou JO-0628 BLE temperature/humidity sensors.

Eventually the data will get pushed somewhere, but for now it just prints to console.

## Values captured:
* Device name
* Battery level
* Temperature
* Humidity

## gattools commands relevant to Jinou JO-0628

```bash
gatttool -b <device ID> --char-read -u 0x2a19
49 #hex battery %
gatttool -b <device ID> --char-read -u 0xaa21
001406002701  #temp+humitidty!
gatttool -b <device ID> --char-read -u 0xaa22
01  #sampling enabled
gatttool -b <device ID> --char-read -u 0x0023
ff  #sample rate in 100ths of a second
```
