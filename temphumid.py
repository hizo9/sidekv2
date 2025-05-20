import adafruit_dht
import board
import time

def initialize_dht_sensor(pin=board.D18):
    return adafruit_dht.DHT22(pin)

def get_sensor_readings(dht_device):
    try:
        temperature_c = dht_device.temperature
        humidity = dht_device.humidity

        if temperature_c is not None and humidity is not None:
            temperature_f = (temperature_c * 9 / 5) + 32
            return {
                'temperature_c': temperature_c,
                'temperature_f': temperature_f,
                'humidity': humidity
            }
        else:
            return None

    except RuntimeError as error:
        print(f"RuntimeError: {error.args[0]}")
        return None
    except Exception as error:
        print(f"An unexpected error occurred: {error}")
        return None