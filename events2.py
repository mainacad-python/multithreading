from threading import Thread, Event
import logging
import time
import random

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(threadName)s - %(message)s")
logger = logging.getLogger(__name__)


events = [Event() for _ in range(4)]


def func_0():
    logger.info('Inside the func_0()')
    logger.info('Setting event-0...')
    time.sleep(2)
    events[0].set()
    logger.info('event-0 has been setted!...')


def func_1():
    logger.info('Inside the func_1()')
    logger.info('Waiting for the event-0...')
    events[0].wait()
    logger.info('event-0 has been set!')

    time_to_sleep = 5*random.random()

    logger.info(f'event-1 will be setted after {time_to_sleep} seconds..')
    time.sleep(time_to_sleep)
    events[1].set()
    logger.info('event-1 has been set!')


def func_2():
    logger.info('Inside the func_2()')
    logger.info('Waiting for the event-1 and event-3...')
    events[1].wait()
    events[3].wait()
    logger.info('event-1 and event-3 has been set!')


def func_3():
    logger.info('Inside the func_3()')
    logger.info('Waiting for the event-0...')
    events[0].wait()
    logger.info('event-0 has been set!')

    time_to_sleep = random.randint(2, 4)

    logger.info(f'event-3 will be setted after {time_to_sleep} seconds..')
    time.sleep(time_to_sleep)
    events[3].set()
    logger.info('event-3 has been set!')


t0 = Thread(target=func_0)
t1 = Thread(target=func_1)
t2 = Thread(target=func_2)
t3 = Thread(target=func_3)

t0.start()
t1.start()
t2.start()
t3.start()

t0.join()
t1.join()
t2.join()
t3.join()
