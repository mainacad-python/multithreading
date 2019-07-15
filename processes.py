# import multiprocessing as mp
from multiprocessing import Process, Value, Barrier
import logging
import random

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(PID)s - %(message)s")
logger = logging.getLogger(__name__)


def increment(value, value2, barrier):
    with value.get_lock():
        value.value += 1 + value2.value
        print(f"value increased: {value.value}")
    barrier.wait()


if __name__ == '__main__':
    num = 10

    val = Value("i", 0, lock=True)
    val2 = Value('i', 10)
    barrier = Barrier(num + 1)
    processes = [Process(target=increment, args=(val, val2, barrier)) for _ in range(num)]
    for p in processes:
        p.start()

    barrier.wait()

    print(val.value)

    for p in processes:
        p.join()
