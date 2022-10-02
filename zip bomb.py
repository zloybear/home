import os
import random
r = random.randint(1,100)
def cozdat():
    for i in range(r):
        print(os.mkdir('F:\хлам3\yeban'+str(i)))
def ydalit():
    for i in range(100):
        print(os.rmdir('F:\хлам3\yeban'+str(i)))

cozdat()
