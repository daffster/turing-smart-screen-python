import pyadl
import psutil
import sys


import library.config as config
import library.lcd_comm as lcd

CONFIG_DATA = config.CONFIG_DATA


class CPU:
    @staticmethod
    def percentage():
        cpu_percentage = psutil.cpu_percent(interval=CONFIG_DATA['STATS']['CPU']['PERCENTAGE'].get("INTERVAL", None))
        # print(f"CPU Percentage: {cpu_percentage}")

        if CONFIG_DATA['STATS']['CPU']['PERCENTAGE']['TEXT'].get("SHOW", False):
            lcd.DisplayText(
                ser=config.lcd_comm,
                text=str(int(cpu_percentage)).zfill(3),
                x=CONFIG_DATA['STATS']['CPU']['PERCENTAGE']['TEXT'].get("X", 0),
                y=CONFIG_DATA['STATS']['CPU']['PERCENTAGE']['TEXT'].get("Y", 0),
                font=CONFIG_DATA['STATS']['CPU']['PERCENTAGE']['TEXT'].get("FONT", "roboto/Roboto-Regular.ttf"),
                font_size=CONFIG_DATA['STATS']['CPU']['PERCENTAGE']['TEXT'].get("FONT_SIZE", 10),
                font_color=CONFIG_DATA['STATS']['CPU']['PERCENTAGE']['TEXT'].get("FONT_COLOR", (0, 0, 0)),
                background_color=CONFIG_DATA['STATS']['CPU']['PERCENTAGE']['TEXT'].get("BACKGROUND_COLOR", (255, 255, 255)),
                background_image=CONFIG_DATA['STATS']['CPU']['PERCENTAGE']['TEXT'].get("BACKGROUND_IMAGE", None)
            )

        if CONFIG_DATA['STATS']['CPU']['PERCENTAGE']['GRAPH'].get("SHOW", False):
            lcd.DisplayProgressBar(
                ser=config.lcd_comm,
                x=CONFIG_DATA['STATS']['CPU']['PERCENTAGE']['GRAPH'].get("X", 0),
                y=CONFIG_DATA['STATS']['CPU']['PERCENTAGE']['GRAPH'].get("Y", 0),
                width=CONFIG_DATA['STATS']['CPU']['PERCENTAGE']['GRAPH'].get("WIDTH", 0),
                height=CONFIG_DATA['STATS']['CPU']['PERCENTAGE']['GRAPH'].get("HEIGHT", 0),
                value=int(cpu_percentage),
                min_value=CONFIG_DATA['STATS']['CPU']['PERCENTAGE']['GRAPH'].get("MIN_VALUE", 0),
                max_value=CONFIG_DATA['STATS']['CPU']['PERCENTAGE']['GRAPH'].get("MAX_VALUE", 100),
                bar_color=CONFIG_DATA['STATS']['CPU']['PERCENTAGE']['GRAPH'].get("BAR_COLOR", (0, 0, 0)),
                bar_outline=CONFIG_DATA['STATS']['CPU']['PERCENTAGE']['GRAPH'].get("BAR_OUTLINE", False),
                background_image=CONFIG_DATA['STATS']['CPU']['PERCENTAGE']['GRAPH'].get("BACKGROUND_IMAGE", None)
            )

    @staticmethod
    def frequency():
        cpu_freq = psutil.cpu_freq()

        if CONFIG_DATA['STATS']['CPU']['FREQUENCY']['TEXT'].get("SHOW", False):
            lcd.DisplayText(
                ser=config.lcd_comm,
                text=str(int(cpu_freq.current)),
                x=CONFIG_DATA['STATS']['CPU']['FREQUENCY']['TEXT'].get("X", 0),
                y=CONFIG_DATA['STATS']['CPU']['FREQUENCY']['TEXT'].get("Y", 0),
                font=CONFIG_DATA['STATS']['CPU']['FREQUENCY']['TEXT'].get("FONT", "roboto/Roboto-Regular.ttf"),
                font_size=CONFIG_DATA['STATS']['CPU']['FREQUENCY']['TEXT'].get("FONT_SIZE", 10),
                font_color=CONFIG_DATA['STATS']['CPU']['FREQUENCY']['TEXT'].get("FONT_COLOR", (0, 0, 0)),
                background_color=CONFIG_DATA['STATS']['CPU']['FREQUENCY']['TEXT'].get("BACKGROUND_COLOR", (255, 255, 255)),
                background_image=CONFIG_DATA['STATS']['CPU']['FREQUENCY']['TEXT'].get("BACKGROUND_IMAGE", None)
            )

    @staticmethod
    def load():
        cpu_load = psutil.getloadavg()
        # print(f"CPU Load: ({cpu_load[0]},{cpu_load[1]},{cpu_load[2]})")

        if CONFIG_DATA['STATS']['CPU']['LOAD']['ONE']['TEXT'].get("SHOW", False):
            lcd.DisplayText(
                ser=config.lcd_comm,
                text=f"{str(int(cpu_load[0]))}%",
                x=CONFIG_DATA['STATS']['CPU']['LOAD']['ONE']['TEXT'].get("X", 0),
                y=CONFIG_DATA['STATS']['CPU']['LOAD']['ONE']['TEXT'].get("Y", 0),
                font=CONFIG_DATA['STATS']['CPU']['LOAD']['ONE']['TEXT'].get("FONT", "roboto/Roboto-Regular.ttf"),
                font_size=CONFIG_DATA['STATS']['CPU']['LOAD']['ONE']['TEXT'].get("FONT_SIZE", 10),
                font_color=CONFIG_DATA['STATS']['CPU']['LOAD']['ONE']['TEXT'].get("FONT_COLOR", (0, 0, 0)),
                background_color=CONFIG_DATA['STATS']['CPU']['LOAD']['ONE']['TEXT'].get("BACKGROUND_COLOR", (255, 255, 255)),
                background_image=CONFIG_DATA['STATS']['CPU']['LOAD']['ONE']['TEXT'].get("BACKGROUND_IMAGE", None)
            )

        if CONFIG_DATA['STATS']['CPU']['LOAD']['FIVE']['TEXT'].get("SHOW", False):
            lcd.DisplayText(
                ser=config.lcd_comm,
                text=f"{str(int(cpu_load[1]))}%",
                x=CONFIG_DATA['STATS']['CPU']['LOAD']['FIVE']['TEXT'].get("X", 0),
                y=CONFIG_DATA['STATS']['CPU']['LOAD']['FIVE']['TEXT'].get("Y", 0),
                font=CONFIG_DATA['STATS']['CPU']['LOAD']['FIVE']['TEXT'].get("FONT", "roboto/Roboto-Regular.ttf"),
                font_size=CONFIG_DATA['STATS']['CPU']['LOAD']['FIVE']['TEXT'].get("FONT_SIZE", 10),
                font_color=CONFIG_DATA['STATS']['CPU']['LOAD']['FIVE']['TEXT'].get("FONT_COLOR", (0, 0, 0)),
                background_color=CONFIG_DATA['STATS']['CPU']['LOAD']['FIVE']['TEXT'].get("BACKGROUND_COLOR", (255, 255, 255)),
                background_image=CONFIG_DATA['STATS']['CPU']['LOAD']['FIVE']['TEXT'].get("BACKGROUND_IMAGE", None)
            )

        if CONFIG_DATA['STATS']['CPU']['LOAD']['FIFTEEN']['TEXT'].get("SHOW", False):
            lcd.DisplayText(
                ser=config.lcd_comm,
                text=f"{str(int(cpu_load[2]))}%",
                x=CONFIG_DATA['STATS']['CPU']['LOAD']['FIFTEEN']['TEXT'].get("X", 0),
                y=CONFIG_DATA['STATS']['CPU']['LOAD']['FIFTEEN']['TEXT'].get("Y", 0),
                font=CONFIG_DATA['STATS']['CPU']['LOAD']['FIFTEEN']['TEXT'].get("FONT", "roboto/Roboto-Regular.ttf"),
                font_size=CONFIG_DATA['STATS']['CPU']['LOAD']['FIFTEEN']['TEXT'].get("FONT_SIZE", 10),
                font_color=CONFIG_DATA['STATS']['CPU']['LOAD']['FIFTEEN']['TEXT'].get("FONT_COLOR", (0, 0, 0)),
                background_color=CONFIG_DATA['STATS']['CPU']['LOAD']['FIFTEEN']['TEXT'].get("BACKGROUND_COLOR", (255, 255, 255)),
                background_image=CONFIG_DATA['STATS']['CPU']['LOAD']['FIFTEEN']['TEXT'].get("BACKGROUND_IMAGE", None)
            )

    @staticmethod
    def temperature():
        print( sys.platform )
        if sys.platform=='win32':
            print('Windows - Using OpenHardwareMonitor web endpoint')
            import requests, json
            r = requests.get('http://172.27.160.1:8085/data.json')
            if r.status_code == 200:
                data=json.loads(r.text)
                if CONFIG_DATA['STATS']['CPU']['TEMPERATURE']['TEXT'].get("SHOW", False):
                    lcd.DisplayText(
                    ser=config.lcd_comm,
                    text=str(int(cpu_temp)),
                    x=CONFIG_DATA['STATS']['CPU']['TEMPERATURE']['TEXT'].get("X", 0),
                    y=CONFIG_DATA['STATS']['CPU']['TEMPERATURE']['TEXT'].get("Y", 0),
                    font=CONFIG_DATA['STATS']['CPU']['TEMPERATURE']['TEXT'].get("FONT", "roboto/Roboto-Regular.ttf"),
                    font_size=CONFIG_DATA['STATS']['CPU']['TEMPERATURE']['TEXT'].get("FONT_SIZE", 10),
                    font_color=CONFIG_DATA['STATS']['CPU']['TEMPERATURE']['TEXT'].get("FONT_COLOR", (0, 0, 0)),
                    background_color=CONFIG_DATA['STATS']['CPU']['TEMPERATURE']['TEXT'].get("BACKGROUND_COLOR", (255, 255, 255)),
                    background_image=CONFIG_DATA['STATS']['CPU']['TEMPERATURE']['TEXT'].get("BACKGROUND_IMAGE", None)
                )
        else:
            pass
        # TODO: Built in function for *nix in psutil, for Windows can use WMI or a third party library


class GPU:
    @staticmethod
    def stats():
        # Unlike the CPU, the GPU pulls in all the stats at once
        gpu_data = pyadl.ADLManager.getInstance().getDevices()

        core_clock_all = [item.getCurrentEngineClock() for item in gpu_data]
        core_clock = sum(core_clock_all) / len(core_clock_all)

        fan_total_all = [item.getCurrentFanSpeed(pyadl.ADL_DEVICE_FAN_SPEED_TYPE_PERCENTAGE) for item in gpu_data]
        fan_total = sum(fan_total_all) / len(fan_total_all)

        fan_percentage = fan_total

        load_all = [item.getCurrentUsage() for item in gpu_data]
        load = (sum(load_all) / len(load_all)) * 100

        temperature_all = [item.getCurrentTemperature() for item in gpu_data]
        temperature = sum(temperature_all) / len(temperature_all)

        if CONFIG_DATA['STATS']['GPU']['PERCENTAGE']['GRAPH'].get("SHOW", False):
            # print(f"GPU Load: {load}")
            lcd.DisplayProgressBar(
                ser=config.lcd_comm,
                x=CONFIG_DATA['STATS']['GPU']['PERCENTAGE']['GRAPH'].get("X", 0),
                y=CONFIG_DATA['STATS']['GPU']['PERCENTAGE']['GRAPH'].get("Y", 0),
                width=CONFIG_DATA['STATS']['GPU']['PERCENTAGE']['GRAPH'].get("WIDTH", 0),
                height=CONFIG_DATA['STATS']['GPU']['PERCENTAGE']['GRAPH'].get("HEIGHT", 0),
                value=int(load),
                min_value=CONFIG_DATA['STATS']['GPU']['PERCENTAGE']['GRAPH'].get("MIN_VALUE", 0),
                max_value=CONFIG_DATA['STATS']['GPU']['PERCENTAGE']['GRAPH'].get("MAX_VALUE", 100),
                bar_color=CONFIG_DATA['STATS']['GPU']['PERCENTAGE']['GRAPH'].get("BAR_COLOR", (0, 0, 0)),
                bar_outline=CONFIG_DATA['STATS']['GPU']['PERCENTAGE']['GRAPH'].get("BAR_OUTLINE", False),
                background_image=CONFIG_DATA['STATS']['GPU']['PERCENTAGE']['GRAPH'].get("BACKGROUND_IMAGE", None)
            )

        if CONFIG_DATA['STATS']['GPU']['FAN']['GRAPH'].get("SHOW", False):
            # print(f"GPU Fan: {load}")
            lcd.DisplayProgressBar(
                ser=config.lcd_comm,
                x=CONFIG_DATA['STATS']['GPU']['FAN']['GRAPH'].get("X", 0),
                y=CONFIG_DATA['STATS']['GPU']['FAN']['GRAPH'].get("Y", 0),
                width=CONFIG_DATA['STATS']['GPU']['FAN']['GRAPH'].get("WIDTH", 0),
                height=CONFIG_DATA['STATS']['GPU']['FAN']['GRAPH'].get("HEIGHT", 0),
                value=int(fan_percentage),
                min_value=CONFIG_DATA['STATS']['GPU']['FAN']['GRAPH'].get("MIN_VALUE", 0),
                max_value=CONFIG_DATA['STATS']['GPU']['FAN']['GRAPH'].get("MAX_VALUE", 100),
                bar_color=CONFIG_DATA['STATS']['GPU']['FAN']['GRAPH'].get("BAR_COLOR", (0, 0, 0)),
                bar_outline=CONFIG_DATA['STATS']['GPU']['FAN']['GRAPH'].get("BAR_OUTLINE", False),
                background_image=CONFIG_DATA['STATS']['GPU']['FAN']['GRAPH'].get("BACKGROUND_IMAGE", None)
            )

        if CONFIG_DATA['STATS']['GPU']['TEMPERATURE']['TEXT'].get("SHOW", False):
            lcd.DisplayText(
                ser=config.lcd_comm,
                text=f"{str(int(temperature))}* c",
                x=CONFIG_DATA['STATS']['GPU']['TEMPERATURE']['TEXT'].get("X", 0),
                y=CONFIG_DATA['STATS']['GPU']['TEMPERATURE']['TEXT'].get("Y", 0),
                font=CONFIG_DATA['STATS']['GPU']['TEMPERATURE']['TEXT'].get("FONT", "roboto/Roboto-Regular.ttf"),
                font_size=CONFIG_DATA['STATS']['GPU']['TEMPERATURE']['TEXT'].get("FONT_SIZE", 10),
                font_color=CONFIG_DATA['STATS']['GPU']['TEMPERATURE']['TEXT'].get("FONT_COLOR", (0, 0, 0)),
                background_color=CONFIG_DATA['STATS']['GPU']['TEMPERATURE']['TEXT'].get("BACKGROUND_COLOR", (255, 255, 255)),
                background_image=CONFIG_DATA['STATS']['GPU']['TEMPERATURE']['TEXT'].get("BACKGROUND_IMAGE", None)
            )


class Memory:
    @staticmethod
    def stats():
        swap_percent = psutil.swap_memory().percent

        if CONFIG_DATA['STATS']['MEMORY']['SWAP']['GRAPH'].get("SHOW", False):
            lcd.DisplayProgressBar(
                ser=config.lcd_comm,
                x=CONFIG_DATA['STATS']['MEMORY']['SWAP']['GRAPH'].get("X", 0),
                y=CONFIG_DATA['STATS']['MEMORY']['SWAP']['GRAPH'].get("Y", 0),
                width=CONFIG_DATA['STATS']['MEMORY']['SWAP']['GRAPH'].get("WIDTH", 0),
                height=CONFIG_DATA['STATS']['MEMORY']['SWAP']['GRAPH'].get("HEIGHT", 0),
                value=int(swap_percent),
                min_value=CONFIG_DATA['STATS']['MEMORY']['SWAP']['GRAPH'].get("MIN_VALUE", 0),
                max_value=CONFIG_DATA['STATS']['MEMORY']['SWAP']['GRAPH'].get("MAX_VALUE", 100),
                bar_color=CONFIG_DATA['STATS']['MEMORY']['SWAP']['GRAPH'].get("BAR_COLOR", (0, 0, 0)),
                bar_outline=CONFIG_DATA['STATS']['MEMORY']['SWAP']['GRAPH'].get("BAR_OUTLINE", False),
                background_image=CONFIG_DATA['STATS']['MEMORY']['SWAP']['GRAPH'].get("BACKGROUND_IMAGE", None)
            )

        virtual_percent = psutil.virtual_memory().percent

        if CONFIG_DATA['STATS']['MEMORY']['VIRTUAL']['GRAPH'].get("SHOW", False):
            lcd.DisplayProgressBar(
                ser=config.lcd_comm,
                x=CONFIG_DATA['STATS']['MEMORY']['VIRTUAL']['GRAPH'].get("X", 0),
                y=CONFIG_DATA['STATS']['MEMORY']['VIRTUAL']['GRAPH'].get("Y", 0),
                width=CONFIG_DATA['STATS']['MEMORY']['VIRTUAL']['GRAPH'].get("WIDTH", 0),
                height=CONFIG_DATA['STATS']['MEMORY']['VIRTUAL']['GRAPH'].get("HEIGHT", 0),
                value=int(virtual_percent),
                min_value=CONFIG_DATA['STATS']['MEMORY']['VIRTUAL']['GRAPH'].get("MIN_VALUE", 0),
                max_value=CONFIG_DATA['STATS']['MEMORY']['VIRTUAL']['GRAPH'].get("MAX_VALUE", 100),
                bar_color=CONFIG_DATA['STATS']['MEMORY']['VIRTUAL']['GRAPH'].get("BAR_COLOR", (0, 0, 0)),
                bar_outline=CONFIG_DATA['STATS']['MEMORY']['VIRTUAL']['GRAPH'].get("BAR_OUTLINE", False),
                background_image=CONFIG_DATA['STATS']['MEMORY']['VIRTUAL']['GRAPH'].get("BACKGROUND_IMAGE", None)
            )

class Disk:
    @staticmethod
    def stats():
        percent = psutil.disk_usage("/").percent

        if CONFIG_DATA['STATS']['DISK']['GRAPH'].get("SHOW", False):
            lcd.DisplayProgressBar(
                ser=config.lcd_comm,
                x=CONFIG_DATA['STATS']['DISK']['GRAPH'].get("X", 0),
                y=CONFIG_DATA['STATS']['DISK']['GRAPH'].get("Y", 0),
                width=CONFIG_DATA['STATS']['DISK']['GRAPH'].get("WIDTH", 0),
                height=CONFIG_DATA['STATS']['DISK']['GRAPH'].get("HEIGHT", 0),
                value=int(percent),
                min_value=CONFIG_DATA['STATS']['DISK']['GRAPH'].get("MIN_VALUE", 0),
                max_value=CONFIG_DATA['STATS']['DISK']['GRAPH'].get("MAX_VALUE", 100),
                bar_color=CONFIG_DATA['STATS']['DISK']['GRAPH'].get("BAR_COLOR", (0, 0, 0)),
                bar_outline=CONFIG_DATA['STATS']['DISK']['GRAPH'].get("BAR_OUTLINE", False),
                background_image=CONFIG_DATA['STATS']['DISK']['GRAPH'].get("BACKGROUND_IMAGE", None)
            )
