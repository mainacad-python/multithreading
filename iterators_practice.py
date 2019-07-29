import time
from string import ascii_uppercase


def id_creator():
    def numbers():
        num = 0
        while num < 1000:
            yield num
            num += 1

    def chars():
        for ch1 in ascii_uppercase:
            for ch2 in ascii_uppercase:
                yield f"{ch1}{ch2}"

    for chrs in chars():
        for n in numbers():
            yield f"{chrs}{n:03}"


for i in id_creator():
    print(i)
    # time.sleep(0.5)