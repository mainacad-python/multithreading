import time


class Iterator:
    def __init__(self, sequence):
        self._collection = sequence
        self._index = 0

    def __next__(self):
        print(f"In the iterator.. Index: {self._index}")
        if self._index < len(self._collection):
            element = self._collection[self._index]
            self._index += 1
            return element
        else:
            raise StopIteration

    def generator(self):
        while self._index < len(self._collection):
            yield self._collection[self._index]
            self._index += 1


    def __iter__(self):
        print("Calling __iter__()...")
        return self


# iterator = Iterator([1,2,4532,5,3412,2135,4535,354])
# for i in iterator.generator():
#     print(i)


def selector(*args):
    iterators = [iter(lst) for lst in args]
    while True:
        yield [next(lst, 0) for lst in iterators]
        
lst = [
    [1,2,3,4,5],
    [1,2,3],
    [1,4,56,7,8,9,0],
]

s = selector(*lst)
while True:
    print(next(s))


# def fibonacci():
#     prev, curr = 0, 1
#     while True:
#         yield curr
#         prev, curr = curr, curr + prev
#
#
# fibo = fibonacci()
# #
# # while True:
# #     next_el = next(fibo)
# #     print(next_el)
#
#
# def factorial():
#     prev, curr = 1, 1
#     while True:
#         prev, curr = prev * curr, curr + 1
#         yield prev
#
# def demo():
#     print("First ")
#     yield 1
#     print("Second")
#     yield
#     print("Third")
#     yield 3
#
# d = demo()
#
# #
# # fact = factorial()
# # while True:
# #     # time.sleep(1)
# #     print(next(fact))
