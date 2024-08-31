# генераторы - это функции
# python -i file.py - запустит в интерактивном режиме python

def gen(s):
    for i in s:
        yield i


g = gen('abcdef')


def gen1(n):
    for i in n:
        yield i


def gen2(n):
    for i in range(n):
        yield i


g1 = gen1('tr')
g2 = gen2(2)

tasks = [g1, g2]

while tasks:
    task = tasks.pop(0)

    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        pass
