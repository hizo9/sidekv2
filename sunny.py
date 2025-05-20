# Imports
import smbus
import time

# Configs
bus = smbus.SMBus(1)
I2C_ADDRESS = 0x23

# sunny.py
POWER_ON = 0x01
RESET = 0x07
CONTINUOUS_HIGH_RES_MODE_1 = 0x10

def read_light():
    bus.write_byte(I2C_ADDRESS, POWER_ON)
    bus.write_byte(I2C_ADDRESS, RESET)
    bus.write_byte(I2C_ADDRESS, CONTINUOUS_HIGH_RES_MODE_1)
    time.sleep(0.15)  # wait ~120ms
    
    # read 2 bytes (msg + lsb)
    data = bus.read_i2c_block_data(I2C_ADDRESS, 0x00, 2)
    raw_value = (data[0] << 8) | data[1]
    lux = raw_value / 1.2  # convert to lux
    return lux