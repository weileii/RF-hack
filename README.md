# RF Tools — Raspberry Pi Pico W

![MicroPython](https://img.shields.io/badge/MicroPython-1.20%2B-blue?style=flat-square&logo=micropython)
![Raspberry Pi Pico W](https://img.shields.io/badge/Hardware-Raspberry%20Pi%20Pico%20W-red?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green.svg)

An experimental RF monitoring project based on the Raspberry Pi Pico W, CC1101 433 MHz module, and nRF24L01.

The project features a web-based interface inspired by portable RF diagnostic tools. Its main purpose is passive radio activity monitoring, RSSI measurements, and real-time waterfall visualization.

## Hardware

- Raspberry Pi Pico W (RP2040)
- CC1101 433 MHz module
- nRF24L01 module
- Jumper wires
- Optional 10–47 µF capacitor for the nRF24L01

## Features

### 1. Spectrum

- RSSI measurements using the CC1101.
- RPD measurements using the nRF24L01.
- Radio activity visualization.
- Waterfall display.
- Adjustable measurement interval and channel step.

### 2. Raw Monitor

- Passive signal activity monitoring.
- Measurement visualization.
- No replay of captured transmissions.

### 3. Sensor Monitor

- Monitoring of compatible, user-owned 433 MHz sensors.
- Display of decoded sensor readings when their protocol is supported.

### 4. Manual

- Manual measurement parameter selection.
- Scan range configuration within hardware capabilities.
- Adjustable measurement duration.

## Waterfall Visualization

The Waterfall display visualizes radio energy measurements over time.

- Horizontal axis: channels or frequencies.
- Vertical axis: successive measurements over time.
- Color: detected signal energy level.

**Hardware limitations:**

The CC1101 and nRF24L01 are not full SDR receivers. The CC1101 provides RSSI measurements, while the nRF24L01 has a basic RPD energy detector.

Therefore, the Waterfall is an approximate visualization of radio activity, not a professional spectrum analyzer.

## Software

The project uses:

- MicroPython
- Raspberry Pi Pico W
- SPI
- Wi-Fi
- Web interface

## Project Structure

```text
RF-Tools/
├── README.md
├── main.py
├── config.py
├── nrf24.py
├── cc1101.py
├── waterfall.py
├── webserver.py
└── www/
    ├── index.html
    ├── style.css
    └── app.js
```

## Safety and Intended Use

This project is intended for educational purposes, passive RF measurements, and diagnostics of devices owned by the user.

It is not designed for jamming communications, bypassing security systems, controlling devices without authorization, or replaying access-control signals.

Always follow local radio regulations and privacy requirements.

## Development Status

- [x] nRF24L01 SPI communication test
- [x] CC1101 SPI communication test
- [ ] nRF24L01 measurement driver
- [ ] CC1101 RSSI measurement driver
- [ ] Waterfall data generator
- [ ] Web interface
- [ ] Hardware integration

## Author
weilei

# RF Tools — Wiring & Hardware Test

This directory contains the wiring guide and hardware communication test for the Raspberry Pi Pico W with the CC1101 433 MHz and nRF24L01 modules.

## Hardware

- Raspberry Pi Pico W (RP2040)
- CC1101 433 MHz module
- nRF24L01 module
- Jumper wires
- Optional 10–47 µF capacitor for nRF24L01

## Wiring

### nRF24L01

| nRF24L01 | Raspberry Pi Pico W |
|---|---|
| VCC | 3V3 — physical pin 36 |
| GND | GND — physical pin 23 |
| CE | GP20 — physical pin 26 |
| CSN | GP17 — physical pin 22 |
| SCK | GP18 — physical pin 24 |
| MOSI | GP19 — physical pin 25 |
| MISO | GP16 — physical pin 21 |
| IRQ | Not connected |

### CC1101 433 MHz

| CC1101 | Raspberry Pi Pico W |
|---|---|
| VCC | 3V3 — physical pin 36 |
| GND | GND — physical pin 23 |
| GDO0 | GP22 — physical pin 29 |
| CSN | GP21 — physical pin 27 |
| SCK | GP18 — physical pin 24 |
| MOSI | GP19 — physical pin 25 |
| MISO | GP16 — physical pin 21 |
| GDO2 | Not connected |

### Shared SPI Connections

Both modules share the same SPI bus:

- SCK: GP18
- MOSI: GP19
- MISO: GP16

Each module has a separate CSN pin.

**Important:** Use 3.3 V power. Do not connect the modules directly to 5 V.

## Running the Test

### Requirements

- Raspberry Pi Pico W
- MicroPython installed on the Pico
- Python and `mpremote` installed on your computer
- Both RF modules connected according to the wiring tables

### Step 1 — Connect the Pico

Connect the Pico W to your computer using USB.

### Step 2 — Upload the test

From the root of the repository, run:

```bash
mpremote connect /dev/ttyACM0 fs cp wiring-test/wiring_test.py :main.py
```

### Step 3 — Run the test

```bash
mpremote connect /dev/ttyACM0 reset
```

Open the serial console:

```bash
mpremote connect /dev/ttyACM0 repl
```

### Step 4 — Check the results

The test checks whether the Pico can communicate with both modules over SPI.

Expected results:

- nRF24L01 CONFIG register: `0x08`
- nRF24L01 RF_CH register: successful write/readback
- CC1101 PARTNUM: `0x0F`
- CC1101 VERSION: `0x0F`
- CC1101 IOCFG2: successful write/readback

### Troubleshooting

If a test fails:

1. Check the 3.3 V and GND connections.
2. Check the shared SPI wiring.
3. Check that each module has the correct CSN pin.
4. Check the USB connection.
5. Make sure no other program is using `/dev/ttyACM0`.

On Linux, if permission is denied, add your user to the `dialout` group and log in again.

## What This Test Does

This is a basic hardware communication test. It verifies SPI register access.

It does **not** test wireless transmission, reception, signal range, or antenna performance.

## Safety

This test only performs local register read/write operations. It does not transmit RF signals or replay remote-control codes.


![Schemat układu](assets/rfhh.jpg)

