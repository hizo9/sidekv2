# Imports
import adafruit_dht
import board
import time
import sys

# Configs
dht_device = adafruit_dht.DHT22(board.D18)

# Codes
def read_dht22():
    try:
        temperature_c = dht_device.temperature
        humidity = dht_device.humidity

        if temperature_c is not None and humidity is not None:
            temperature_f = (temperature_c * 9 / 5) + 32
            return {
                'temp_c': temperature_c,
                'temp_f': temperature_f,
                'humidity': humidity
            }
        else:
            return None

    except RuntimeError as error:
        print(f"Sensor error: {error.args[0]}")
        return None
    except Exception as error:
        print(f"Unexpected error: {error}")
        return None

reading = read_dht22()
if reading:
    print(
        f"Temp: {reading['temp_c']:.1f}°C / {reading['temp_f']:.1f}°F | "
        f"Humidity: {reading['humidity']:.1f}%"
    )
else:
    print("Failed to read sensor. Try again.")