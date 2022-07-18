import sched
import threading
import time
from datetime import timedelta
from functools import wraps

import library.config as config
import library.stats as stats

CONFIG_DATA = config.CONFIG_DATA


def async_job(threadname=None):
    """ wrapper to handle asynchronous threads """

    def decorator(func):
        """ Decorator to extend async_func """

        @wraps(func)
        def async_func(*args, **kwargs):
            """ create an asynchronous function to wrap around our thread """
            func_hl = threading.Thread(target=func, name=threadname, args=args, kwargs=kwargs)
            func_hl.start()
            return func_hl

        return async_func

    return decorator


def schedule(interval):
    """ wrapper to schedule asynchronous threads """

    def decorator(func):
        """ Decorator to extend periodic """

        def periodic(scheduler, periodic_interval, action, actionargs=()):
            """ Wrap the scheduler with our periodic interval """
            scheduler.enter(periodic_interval, 1, periodic,
                            (scheduler, periodic_interval, action, actionargs))
            action(*actionargs)

        @wraps(func)
        def wrap(
                *args,
                **kwargs
        ):
            """ Wrapper to create our schedule and run it at the appropriate time """
            scheduler = sched.scheduler(time.time, time.sleep)
            periodic(scheduler, interval, func)
            scheduler.run()

        return wrap

    return decorator


@async_job("CPU_Percentage")
@schedule(timedelta(seconds=CONFIG_DATA['STATS']['CPU']['PERCENTAGE'].get("INTERVAL", None)).total_seconds())
def CPUPercentage():
    """ Refresh the CPU Percentage """
    # print("Refresh CPU Percentage")
    stats.CPU.percentage()


@async_job("CPU_Frequency")
@schedule(timedelta(seconds=CONFIG_DATA['STATS']['CPU']['FREQUENCY'].get("INTERVAL", None)).total_seconds())
def CPUFrequency():
    """ Refresh the CPU Frequency """
    # print("Refresh CPU Frequency")
    stats.CPU.frequency()


@async_job("CPU_Load")
@schedule(timedelta(seconds=CONFIG_DATA['STATS']['CPU']['LOAD'].get("INTERVAL", None)).total_seconds())
def CPULoad():
    """ Refresh the CPU Load """
    # print("Refresh CPU Load")
    stats.CPU.load()

@async_job("CPU_Temp")
@schedule(timedelta(seconds=CONFIG_DATA['STATS']['CPU']['TEMPERATURE'].get("INTERVAL", None)).total_seconds())
def CPUTemp():
    """ Refresh the CPU Temp """
    # print("Refresh CPU Temp")
    stats.CPU.temperature()

@async_job("GPU_Stats")
@schedule(timedelta(seconds=CONFIG_DATA['STATS']['GPU'].get("INTERVAL", None)).total_seconds())
def GPUStats():
    """ Refresh the GPU Stats """
    # print("Refresh GPU Stats")
    stats.GPU.stats()


@async_job("Memory_Stats")
@schedule(timedelta(seconds=CONFIG_DATA['STATS']['MEMORY'].get("INTERVAL", None)).total_seconds())
def MemoryStats():
    # print("Refresh memory stats")
    stats.Memory.stats()


@async_job("Disk_Stats")
@schedule(timedelta(seconds=CONFIG_DATA['STATS']['DISK'].get("INTERVAL", None)).total_seconds())
def DiskStats():
    # print("Refresh disk stats")
    stats.Disk.stats()


@async_job("Queue_Handler")
@schedule(timedelta(milliseconds=1).total_seconds())
def QueueHandler():
    f, args = config.update_queue.get()
    if f:
        f(*args)
