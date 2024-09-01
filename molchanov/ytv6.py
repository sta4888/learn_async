# coroutines
# запускаем в интерактивном режиме python -i ytv6.py
# g = average()
# g.send(5)
# try:
#     g.throw(StopIteration)
# except StopIteration as e:
#     print('Average', e.value)
###########################################
# def coroutine(func):
#     def inner(*args, **kwargs):
#         g = func(*args, **kwargs)
#         g.send(None)
#         return g
#
#     return inner
#
#
# def subgen():
#     message = yield
#     print(f"Subgen recived {message}")
#
#
# class BlaBlaException(Exception):
#     pass
#
#
# @coroutine
# def average():
#     count = 0
#     summ = 0
#     average = None
#
#     while True:
#         try:
#             x = yield average
#         except StopIteration:
#             print('Done')
#             break
#         except BlaBlaException:
#             print('_______________')
#             break
#         else:
#             count += 1
#             summ += x
#             average = round(summ / count, 2)
#
#     return average
###########################################
# делигирующий генератора
def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return inner


class BlaBlaException(Exception):
    pass


def subgen():
    while True:
        try:
            message = yield
        except StopIteration:
            print('Ку-Ку !!!')
            break
        else:
            print("___________", message)

    return "Returned from subgen()"

@coroutine
def delegator(g):
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except BlaBlaException as e:
    #         g.throw(e)
    result = yield from g
    print(result)




