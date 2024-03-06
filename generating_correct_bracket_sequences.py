# Generating correct bracket sequences
# https://habr.com/ru/companies/yandex/articles/449890/#:~:text=%D0%97%D0%B0%D0%B4%D0%B0%D1%87%D0%B0%20D.%20%D0%93%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F%20%D1%81%D0%BA%D0%BE%D0%B1%D0%BE%D1%87%D0%BD%D1%8B%D1%85%20%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B5%D0%B9

# Правильные скобочные последовательности
# https://neerc.ifmo.ru/wiki/index.php?title=%D0%9F%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5_%D1%81%D0%BA%D0%BE%D0%B1%D0%BE%D1%87%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8

# 𝚊𝚗𝚜 — строка, в которой мы считаем ответ
# 𝚌𝚘𝚞𝚗𝚝𝚎𝚛_𝚘𝚙𝚎𝚗 — количество открывающих скобок в данный момент
# 𝚌𝚘𝚞𝚗𝚝𝚎𝚛_𝚌𝚕𝚘𝚜𝚎 — количество закрывающих скобок в данный момент

def gen(n: int, counter_open: int, counter_close: int, ans: str):
    if counter_open + counter_close == 2 * n:
        print(ans)
        return
    if counter_open < n:
        # print('counter_open', counter_open, 'counter_close', counter_close, 'ans', ans)
        gen(n, counter_open + 1, counter_close, ans + '(')
    if counter_open > counter_close:
        # print('counter_open', counter_open, 'counter_close', counter_close, 'ans', ans)
        gen(n, counter_open, counter_close + 1, ans + ')')

import time
t = time.time()
gen(4, 0, 0, "")
print(time.time()-t, len(res))

# short Response (1)
# (((())))
# ((()()))
# ((())())
# ((()))()
# (()(()))
# (()()())
# (()())()
# (())(())
# (())()()
# ()((()))
# ()(()())
# ()(())()
# ()()(())
# ()()()()
# 0.00063323974609375 14

# detailed Response (2)
# >>> gen(4, 0, 0, "")
# counter_open 0 counter_close 0 ans 
# counter_open 1 counter_close 0 ans (
# counter_open 2 counter_close 0 ans ((
# counter_open 3 counter_close 0 ans (((
# counter_open 4 counter_close 0 ans ((((
# counter_open 4 counter_close 1 ans (((()
# counter_open 4 counter_close 2 ans (((())
# counter_open 4 counter_close 3 ans (((()))
# (((())))
# counter_open 3 counter_close 0 ans (((
# counter_open 3 counter_close 1 ans ((()
# counter_open 4 counter_close 1 ans ((()(
# counter_open 4 counter_close 2 ans ((()()
# counter_open 4 counter_close 3 ans ((()())
# ((()()))
# counter_open 3 counter_close 1 ans ((()
# counter_open 3 counter_close 2 ans ((())
# counter_open 4 counter_close 2 ans ((())(
# counter_open 4 counter_close 3 ans ((())()
# ((())())
# counter_open 3 counter_close 2 ans ((())
# counter_open 3 counter_close 3 ans ((()))
# counter_open 4 counter_close 3 ans ((()))(
# ((()))()
# counter_open 2 counter_close 0 ans ((
# counter_open 2 counter_close 1 ans (()
# counter_open 3 counter_close 1 ans (()(
# counter_open 4 counter_close 1 ans (()((
# counter_open 4 counter_close 2 ans (()(()
# counter_open 4 counter_close 3 ans (()(())
# (()(()))
# counter_open 3 counter_close 1 ans (()(
# counter_open 3 counter_close 2 ans (()()
# counter_open 4 counter_close 2 ans (()()(
# counter_open 4 counter_close 3 ans (()()()
# (()()())
# counter_open 3 counter_close 2 ans (()()
# counter_open 3 counter_close 3 ans (()())
# counter_open 4 counter_close 3 ans (()())(
# (()())()
# counter_open 2 counter_close 1 ans (()
# counter_open 2 counter_close 2 ans (())
# counter_open 3 counter_close 2 ans (())(
# counter_open 4 counter_close 2 ans (())((
# counter_open 4 counter_close 3 ans (())(()
# (())(())
# counter_open 3 counter_close 2 ans (())(
# counter_open 3 counter_close 3 ans (())()
# counter_open 4 counter_close 3 ans (())()(
# (())()()
# counter_open 1 counter_close 0 ans (
# counter_open 1 counter_close 1 ans ()
# counter_open 2 counter_close 1 ans ()(
# counter_open 3 counter_close 1 ans ()((
# counter_open 4 counter_close 1 ans ()(((
# counter_open 4 counter_close 2 ans ()((()
# counter_open 4 counter_close 3 ans ()((())
# ()((()))
# counter_open 3 counter_close 1 ans ()((
# counter_open 3 counter_close 2 ans ()(()
# counter_open 4 counter_close 2 ans ()(()(
# counter_open 4 counter_close 3 ans ()(()()
# ()(()())
# counter_open 3 counter_close 2 ans ()(()
# counter_open 3 counter_close 3 ans ()(())
# counter_open 4 counter_close 3 ans ()(())(
# ()(())()
# counter_open 2 counter_close 1 ans ()(
# counter_open 2 counter_close 2 ans ()()
# counter_open 3 counter_close 2 ans ()()(
# counter_open 4 counter_close 2 ans ()()((
# counter_open 4 counter_close 3 ans ()()(()
# ()()(())
# counter_open 3 counter_close 2 ans ()()(
# counter_open 3 counter_close 3 ans ()()()
# counter_open 4 counter_close 3 ans ()()()(
# ()()()()
