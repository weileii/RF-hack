
from machine import Pin, SPI
import time

# Shared SPI bus
spi = SPI(
    0,
    baudrate=500000,
    polarity=0,
    phase=0,
    sck=Pin(18),
    mosi=Pin(19),
    miso=Pin(16)
)

# Chip select pins
nrf_csn = Pin(17, Pin.OUT, value=1)
cc_csn = Pin(21, Pin.OUT, value=1)

# nRF24L01 registers
NRF_CONFIG = 0x00
NRF_RF_CH = 0x05

# CC1101 registers
CC_PARTNUM = 0x30
CC_VERSION = 0x31
CC_IOCFG2 = 0x00


def nrf_read_register(register):
    nrf_csn.value(0)
    spi.write(bytes([register & 0x1F]))
    result = spi.read(1)
    nrf_csn.value(1)
    return result[0]


def nrf_write_register(register, value):
    nrf_csn.value(0)
    spi.write(bytes([0x20 | (register & 0x1F), value]))
    nrf_csn.value(1)


def cc_read_register(register):
    cc_csn.value(0)
    spi.write(bytes([register | 0x80]))
    result = spi.read(1)
    cc_csn.value(1)
    return result[0]


def cc_write_register(register, value):
    cc_csn.value(0)
    spi.write(bytes([register, value]))
    cc_csn.value(1)


def test_nrf24():
    print("\n--- nRF24L01 TEST ---")

    config = nrf_read_register(NRF_CONFIG)
    print("CONFIG:", hex(config))

    original = nrf_read_register(NRF_RF_CH)
    test_value = 42

    nrf_write_register(NRF_RF_CH, test_value)
    time.sleep_ms(5)

    result = nrf_read_register(NRF_RF_CH)

    # Restore original register value
    nrf_write_register(NRF_RF_CH, original)

    print("RF_CH:", result)

    if result == test_value:
        print("[PASS] nRF24L01 SPI communication")
        return True

    print("[FAIL] nRF24L01 SPI communication")
    return False


def test_cc1101():
    print("\n--- CC1101 TEST ---")

    partnum = cc_read_register(CC_PARTNUM)
    version = cc_read_register(CC_VERSION)

    print("PARTNUM:", hex(partnum))
    print("VERSION:", hex(version))

    original = cc_read_register(CC_IOCFG2)

    test_value = 0x29
    cc_write_register(CC_IOCFG2, test_value)
    time.sleep_ms(5)

    result = cc_read_register(CC_IOCFG2)

    # Restore original register value
    cc_write_register(CC_IOCFG2, original)

    print("IOCFG2:", hex(result))

    if result == test_value:
        print("[PASS] CC1101 SPI communication")
        return True

    print("[FAIL] CC1101 SPI communication")
    return False


print("================================")
print("       RF TOOLS WIRING TEST")
print("================================")

time.sleep_ms(500)

nrf_ok = test_nrf24()
cc_ok = test_cc1101()

print("\n========== SUMMARY ==========")
print("nRF24L01:", "PASS" if nrf_ok else "FAIL")
print("CC1101:", "PASS" if cc_ok else "FAIL")

if nrf_ok and cc_ok:
    print("\nALL TESTS PASSED!")
else:
    print("\nCHECK YOUR WIRING!")

