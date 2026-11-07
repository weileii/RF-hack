# RF-hack
A Raspberry Pi Pico W-based RF monitoring tool featuring CC1101 433 MHz and nRF24L01 modules, with RSSI analysis and real-time Waterfall visualization.
# RF Tools — Raspberry Pi Pico W

 monitoring project based on the Raspberry Pi Pico W, CC1101 433 MHz module, and nRF24L01.

The project features a web-based interface inspired by portable RF diagnostic tools. Its main purpose is passive radio activity monitoring, RSSI measurements, and real-time waterfall visualization.

## Hardware

- Raspberry Pi Pico W (RP2040)
- CC1101 433 MHz module
- nRF24L01 module
- Jumper wires
- Optional 10–47 µF capacitor for the nRF24L01

## Wiring

### nRF24L01

| nRF24L01 | Raspberry Pi Pico W    |
| -------- | ---------------------- |
| VCC      | 3V3 (physical pin 36)  |
| GND      | GND (physical pin 23)  |
| CE       | GP20 (physical pin 26) |
| CSN      | GP17 (physical pin 22) |
| SCK      | GP18 (physical pin 24) |
| MOSI     | GP19 (physical pin 25) |
| MISO     | GP16 (physical pin 21) |
| IRQ      | Not connected          |

### CC1101 433 MHz

| CC1101 | Raspberry Pi Pico W    |
| ------ | ---------------------- |
| VCC    | 3V3 (physical pin 36)  |
| GND    | GND (physical pin 23)  |
| GDO0   | GP22 (physical pin 29) |
| CSN    | GP21 (physical pin 27) |
| SCK    | GP18 (physical pin 24) |
| MOSI   | GP19 (physical pin 25) |
| MISO   | GP16 (physical pin 21) |
| GDO2   | Not connected          |

### Shared SPI Bus

Both modules share these SPI connections:

- SCK: GP18
- MOSI: GP19
- MISO: GP16

Each module uses a separate CSN pin.

**Important:** Both modules must be powered with 3.3 V. Do not connect them directly to 5 V.

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

weieli
