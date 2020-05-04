import utils as ut
import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imsave
import sympy as sp
import networkx as nx
from copy import deepcopy

def task2():
    return task2_v1()

def task2_v1():
    length = ut.get_random_int(14, 18)
    city = ut.set_case(ut.get_random_city(), 'loct').capitalize()
    t_start, t_end = ut.get_random_interval_from_month(length)
    month = ut.set_case(ut.get_random_month(), 'gent')
    year = ut.get_random_year()

    minval = ut.get_random_int(0, 1)
    maxval = ut.get_random_int(5, 7)
    x = np.arange(t_start, t_end + 1)
    y = (maxval - minval) * np.random.random(len(x)) + minval
    mask = np.random.random(len(x)) <= 0.7
    y[mask] = np.round(y[mask])
    y[mask] += (np.random.random(np.sum(mask)) <= 0.5) * 0.5
    index = 5
    while not mask[index]:
        index = ut.get_random_int(0, len(x) - 1)
    answer = x[index]
    text = 'На рисунке жирными точками показано суточное количество осадков, ' \
            'выпадавших в {} с {} по {} {} {} г. По горизонтали указаны числа ' \
            'месяца; по вертикали — количество осадков, выпавших  в соответствующий день, в ' \
            'миллиметрах. Для наглядности жирные точки  на рисунке соединены линией. Определите по ' \
            'рисунку, какого числа в {} впервые выпало ровно {} миллиметра ' \
            'осадков'.format(city, t_start, t_end, month, year, city, y[index])

    plt.figure(figsize=(12, 6))
    plt.plot(x, y, '-o')
    plt.xticks(x)
    plt.yticks(np.arange(minval, np.max(y) + 1, 0.5))
    plt.grid()
    plt.savefig('temp/temp.png')
    img = imread('temp/temp.png')
    return {'text': text, 'answer': answer, 'image': img}

def task4():
    funcs = [task4_v1, task4_v2]
    task = ut.get_random_from_list(funcs)
    return task()

def task4_v1():
    n = ut.get_random_from_list([10, 20, 25, 40])
    text = 'В сборнике билетов по биологии всего {} билетов. Только в двух билетах встречается вопрос ' \
           'о грибах. На экзамене выпускнику достаётся один случайно выбранный билет из этого сборника. ' \
           'Найдите вероятность того, что в этом билете будет вопрос о грибах'.format(n)
    answer = 2 / n
    return {'text': text, 'answer': answer, 'image': None}

def task4_v2():
    p1 = round(0.1 * ut.get_random_from_list(range(1, 8)), 2)
    p2 = p1
    while p2 <= p1:
        p2 = round(0.1 * ut.get_random_from_list(range(1, 10)), 2)
    text = 'Вероятность того, что мотор холодильника прослужит более 1 года, равна {}, а вероятность ' \
           'того, что он прослужит более 2 лет, равна {}. Какова вероятность того, что мотор прослужит ' \
           'более 1 года, но не более 2 лет?'.format(p1, p2)
    answer = round(p2 - p1, 2)
    return {'text': text, 'answer': answer, 'image': None}

def task6():
    angle = ut.get_random_int(10, 80)
    text = 'Треугольник <i>ABC</i> вписан в окружность с центром <i>O</i>. Угол <i>BAC</i> равен {}°. ' \
           'Найдите угол <i>BOC</i>. Ответ дайте в градусах.'.format(angle)
    answer = 2 * angle
    return {'text': text, 'answer': answer, 'image': None}

def task8():
    h = ut.get_random_int(10, 30)
    text = 'В первом цилиндрическом сосуде уровень жидкости достигает {} см. Эту жидкость перелили во' \
           ' второй цилиндрический сосуд, диаметр основания которого в 2 раза больше диаметра основания' \
           ' первого. На какой высоте будет находиться уровень жидкости во втором сосуде? Ответ дайте в ' \
           'сантиметрах'.format(h)
    answer = 4 * h
    return {'text': text, 'answer': answer, 'image': None}

def task10():
    freq = ut.get_random_int(700, 800)
    speed = ut.get_random_int(2, 10)
    text = 'Локатор батискафа, равномерно погружающегося вертикально вниз, испускает ультразвуковой сигнал ' \
           'частотой {} МГц. Приёмник регистрирует частоту сигнала, отражённого от дна океана. Скорость погружения' \
           ' батискафа (в м/с) и частоты связаны соотношением (см. формулу). В приведенной формуле <i>c</i>=1500 м/с — скорость звука в воде,' \
           ' f0 — частота испускаемого сигнала  (в МГц), f — частота отражённого сигнала (в МГц). Найдите частоту' \
           ' отражённого сигнала (в МГц), если батискаф погружается со скоростью {} м/с. Ответ округлите до целых.'.format(freq, speed)
    answer = round(freq * (1500 + speed) / (1500 - speed))
    img = imread('images/batiskaf.png')
    return {'text': text, 'answer': answer, 'image': img}

def task12():
    g = nx.DiGraph()
    g.add_nodes_from(['base', 'exp', 'const_plus', 'const_mul', 'sin', 'cos', 'pow', 'turn'])
    g.add_edges_from([('base', 'exp'), ('base', 'const_plus'), ('base', 'const_mul'), ('base', 'sin'), ('base', 'cos'), ('base', 'pow'), ('base', 'turn')])
    g.add_edges_from([('exp', 'turn'), ('exp', 'pow')])
    g.add_edges_from([('const_plus', 'exp'), ('const_plus', 'sin'), ('const_plus', 'cos'), ('const_plus', 'pow'), ('const_plus', 'turn')])
    g.add_edges_from([('const_mul', 'exp'), ('const_mul', 'sin'), ('const_mul', 'cos'), ('const_mul', 'pow'), ('const_mul', 'turn'), ('const_mul', 'const_plus')])
    # g.add_edges_from([('sin', 'pow')])
    # g.add_edges_from([('cos', 'pow')])
    g.add_edges_from([('turn', 'pow')])
    path = ut.random_walk(g, 3)

    x = sp.symbols('x')
    f = x
    for p in path:
        if p == 'exp':
            f = sp.exp(f)
        elif p == 'const_plus':
            c = 0
            while c == 0:
                c = ut.get_random_int(-10, 10)
            f = f + c
        elif p == 'const_mul':
            c = 0
            while c == 0 or c == 1:
                c = ut.get_random_int(-10, 10)
            f = f * c
        elif p == 'sin':
            f = sp.sin(f)
        elif p == 'cos':
            f = sp.cos(f)
        elif p == 'pow':
            n = ut.get_random_int(2, 4)
            f = f ** n
        elif p == 'turn':
            f = 1 / f

    int_f = sp.integrate(f)

    extremum = ut.get_random_int(-10, 10)
    g = deepcopy(f)
    g = g.subs('x', extremum)
    int_f = int_f - g * x

    c = 0
    while c == 0:
        c = ut.get_random_int(-10, 10)

    int_f = int_f + c

    ut.save_sympy_as_image(int_f)
    img = imread('temp/temp.png')
    img = ut.add_equal_y(img)
    imsave('temp/temp.png', img)

    if ut.get_random(0, 1) <= 0.5:
        print('!!!!')
        a = ut.get_random_int(-5, -1) + extremum
        b = ut.get_random_int(1, 5) + extremum
        answer = round(sp.N(int_f.subs('x', extremum)), 2)
    else:
        a = extremum + ut.get_random_int(1, 5)
        b = a + ut.get_random_int(1, 5)
        fa = round(sp.N(int_f.subs('x', a)), 2)
        fb = round(sp.N(int_f.subs('x', b)), 2)
        answer = min(fa, fb)

    text = 'Найдите наименьшее значение функции на отрезке [{}, {}]. Ответ округлите до десятых.'.format(a, b)
    return {'text': text, 'answer': answer, 'image': img}

    # f = ut.get_random_func()
    #
    # df = diff(f)
    # ut.save_sympy_as_image(df)
    # img = imread('temp/temp.png')
    # img = ut.add_equal_y(img)
    #
    # a, b = 0, 10
    # zeros = solveset(df, domain=Interval(a, b))
    # # zeros = [z.evalf() for z in zeros]
    # print(zeros)
    # # result = Min(df.subs('x', a), df.subs('x', b), *[df.subs('x', i) for i in zeros])
    # # print(result)
    # quit()
    # h = ut.get_random_int(10, 30)
    # text = 'Найдите наименьшее значение функции на отрезке [{}, {}]'
    # answer = 4 * h
    # return {'text': text, 'answer': answer, 'image': None}