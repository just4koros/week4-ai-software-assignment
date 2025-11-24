# benchmark.py
import random, string, timeit
from ai_suggested import sort_dicts_ai
from manual_impl import sort_dicts_manual

def gen(n=10000):
    keys = ['k' + str(i) for i in range(5)]
    out = []
    for _ in range(n):
        d = {}
        for k in keys:
            if random.random() > 0.3:
                d[k] = random.randint(0, 100000)
        out.append(d)
    return out

lst = gen(20000)
t1 = timeit.timeit(lambda: sort_dicts_ai(lst, 'k1'), number=10)
t2 = timeit.timeit(lambda: sort_dicts_manual(lst, 'k1'), number=10)
print("AI version time:", t1)
print("Manual version time:", t2)
