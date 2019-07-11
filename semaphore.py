from threading import Thread, Semaphore
import logging
import time
import random

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(threadName)s - %(message)s")
logger = logging.getLogger(__name__)

smphr = Semaphore(2)

counter = 0


def inrease():
    global counter
    logger.info("Waiting for counter..")
    smphr.acquire()
    logger.info("Counter acquired..")
    tts = random.randint(1,5)
    logger.info(f"{tts}sec..")

    time.sleep(tts)
    counter += 1
    tts = random.randint(1, 5)
    logger.info(f"Releasing after {tts}sec..")
    time.sleep(tts)
    smphr.release()
    logger.info(f"Released!")


thrds = [Thread(target=inrease) for _ in range(4)]
for t in thrds:
    t.start()

for t in thrds:
    t.join()
