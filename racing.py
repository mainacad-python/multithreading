from threading import Thread, Barrier
import logging
import time
import random

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(threadName)s - %(message)s")
logger = logging.getLogger(__name__)


barrier = Barrier(11)

finished_cars = []


class Racer(Thread):
    def __init__(self):
        super().__init__()
        self.timer = random.randint(3, 7)

    def run(self) -> None:
        logger.info("Started!")
        time.sleep(self.timer)
        logger.info('Finished')
        finished_cars.append(f'{self.name}')
        barrier.wait()


racers = [Racer() for _ in range(10)]
for racer in racers:
    racer.start()

barrier.wait()
print("Result:")
for r in finished_cars:
    print(r)
