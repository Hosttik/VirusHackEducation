import utils as ut
import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imsave
import sympy as sp
import networkx as nx
from copy import deepcopy
import random

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
    plt.savefig('images/math_task2.png')
    return {'text': text, 'answer': answer, 'image': 'math_task2.png'}

def task3():
    text = "Найдите площадь треугольника: "

    a = random.randint(4, 6)
    if a // 2 == 0:
        h = random.randint(2, 4)
    else:
        h = random.choice([2, 4])
    c = random.randint(1, a - 1)
    answer = a * h / 2

    fig, ax = plt.subplots()

    x = np.linspace(0, 7, 8)

    y0 = 0 * x[:a + 1]
    ax.plot(x[:a + 1], y0, 'b')
    y1 = (h / c) * x[:c + 1]
    ax.plot(x[:c + 1], y1, 'b')
    y2 = h - h / (a - c) * (x[c:a + 1] - c)
    ax.plot(x[c:a + 1], y2, 'b')

    ax.grid()
    plt.savefig('images/math_task3.png')
    # fig.canvas.draw()
    # img = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
    # img = img.reshape(fig.canvas.get_width_height()[::-1] + (3,))

    return {'text': text, 'answer': answer, 'image': 'math_task3.png'}

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

def task5():
    text = "Найдите корень уравнения: "

    funcs = ['x**(1/2)', 'x**(1/3)', '2**x', '3**x']

    x = sp.symbols('x')
    expr = random.choice(funcs)
    f = expr

    answer = 0
    result = 0
    while (result < 1 / 7 or result > 1000) or (answer < 0.5 or answer > 100):
        expr = sp.simplify(expr)
        if f not in ['x**(1/2)', 'x**(1/3)', 'ln(x)']:
            expr2 = expr.subs(x, random.randint(1, 5) * x + random.choice([-1, 1]) * random.randint(1, 7))
            answer = random.randint(2, 5)
            result = expr2.subs(x, answer)
            if result is list:
                result = result[0]
        else:
            expr2 = expr.subs(x, random.randint(1, 5) * x + random.randint(1, 7))
            if f == 'ln(x)':
                result = 2 ** random.randint(2, 10)
                expr3 = expr2 / sp.ln(2)
                answer = sp.solve(expr3 - result, x)[0]
            elif f == 'x**(1/2)':
                result = random.randint(2, 6)
                b = random.randint(1, result ** 2 - 2)
                a = result ** 2 - b
                d = 2
                print('a', a, 'b', b)
                dels = []
                while d <= a and len(dels) < 4:
                    if a % d == 0:
                        dels.append(d)
                    d += 1
                print('dels', dels)
                expr2 = expr.subs(x, random.choice(dels) * x + b)
                answer = sp.solve(expr2 - result)
            elif f == 'x**(1/3)':
                result = random.randint(2, 6)
                b = random.choice([-1, 1]) * random.randint(1, 7)
                a = result ** 3 - b
                d = 2
                dels = []
                while d <= a and len(dels) < 4:
                    if a % d == 0:
                        dels.append(d)
                    d += 1
                expr2 = expr.subs(x, random.choice(dels) * x + b)
                answer = sp.solve(expr2 - result)
            if type(answer) == list and len(answer) == 1:
                answer = answer[0]
    lat = sp.latex(expr2) + '= ' + sp.latex(result)
    fig, ax = plt.subplots()
    plt.text(0.1, 0.5, r"$%s$" % lat, fontsize=30)
    fig.canvas.draw()
    fig.patch.set_visible(False)
    ax.axis('off')
    fig.savefig('images/math_task5.png')
    img = imread('images/math_task5.png')[:, :, :3]
    img = ut.decrease_image(ut.crop_image(img))
    imsave('images/math_task5.png', img)
    return {'text': text, 'answer': answer, 'image': 'math_task5.png'}

def task6():
    angle = ut.get_random_int(10, 80)
    text = 'Треугольник <i>ABC</i> вписан в окружность с центром <i>O</i>. Угол <i>BAC</i> равен {}°. ' \
           'Найдите угол <i>BOC</i>. Ответ дайте в градусах.'.format(angle)
    answer = 2 * angle
    return {'text': text, 'answer': answer, 'image': None}

def task7():
    task = random.choice(['больше', 'меньше'])
    text = 'Перечислите все точки, в которых производная ' + task + ' нуля.'

    x = np.linspace(-5, 5, 200)
    y = random.choice([-1, 1]) * random.randint(1, 5) * x * np.sin(x) + random.choice([-1, 1]) * (
                random.randint(1, 10) + x) * np.cos(x)

    ks = list(random.sample(list(range(20, 180, 20)), 7))
    ks.sort()
    x_c = []
    y_c = []
    answer = []
    i = 0
    for k in ks:
        if abs(y[k] - y[k - 1]) > 0.1:
            y_c.append(y[k])
            x_c.append(x[k])
            i += 1
        if y[k] - y[k - 1] > 0.1 and task == 'больше':
            answer.append(chr(64 + i))
        elif y[k] - y[k - 1] < -0.1 and task == 'меньше':
            answer.append(chr(65 + i))

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(x, y)
    ax.scatter(x_c, y_c)
    for i, (xp, yp) in enumerate(zip(x_c, y_c)):
        plt.annotate(chr(65 + i), xy=(xp + 0.2, yp))
    ax.grid()
    fig.canvas.draw()
    fig.savefig('images/math_task7.png')

    return {'text': text, 'answer': answer, 'image': 'math_task7.png'}

def task8():
    h = ut.get_random_int(10, 30)
    text = 'В первом цилиндрическом сосуде уровень жидкости достигает {} см. Эту жидкость перелили во' \
           ' второй цилиндрический сосуд, диаметр основания которого в 2 раза больше диаметра основания' \
           ' первого. На какой высоте будет находиться уровень жидкости во втором сосуде? Ответ дайте в ' \
           'сантиметрах'.format(h)
    answer = 4 * h
    return {'text': text, 'answer': answer, 'image': None}

def task9():
    text = "Найдите значение выражения: "

    p = random.randint(2, 8)
    den_a = random.randint(3, 9)
    num_a = random.randint(1, den_a - 1)
    pq_e = random.randint(2, 5)
    res_num = random.randint(2, 5)

    q = p ** pq_e
    den_b = pq_e * den_a
    num_b = (res_num * den_a - num_a)
    answer = p ** res_num

    expr2 = r'p^{\frac{num_a}{den_a}}\cdotq^{\frac{num_b}{den_b}}'
    expr2 = expr2.replace('p', str(p))
    expr2 = expr2.replace('num_a',str(num_a))
    expr2 = expr2.replace('den_a',str(den_a))
    expr2 = expr2.replace('q', str(q))
    expr2 = expr2.replace('num_b', str(num_b))
    expr2 = expr2.replace('den_b', str(den_b))

    fig, ax = plt.subplots()
    plt.text(0, 0.6, r"$%s$" % expr2, fontsize=30)
    fig.canvas.draw()
    fig.patch.set_visible(False)
    ax.axis('off')
    fig.savefig('images/math_task9.png')
    img = imread('images/math_task9.png')[:, :, :3]
    img = ut.decrease_image(ut.crop_image(img))
    imsave('images/math_task9.png', img)

    # fig.canvas.draw()
    # img = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
    # img = img.reshape(fig.canvas.get_width_height()[::-1] + (3,))

    return {'text': text, 'answer': answer, 'image': 'math_task9.png'}

def task10():
    freq = ut.get_random_int(700, 800)
    speed = ut.get_random_int(2, 10)
    text = 'Локатор батискафа, равномерно погружающегося вертикально вниз, испускает ультразвуковой сигнал ' \
           'частотой {} МГц. Приёмник регистрирует частоту сигнала, отражённого от дна океана. Скорость погружения' \
           ' батискафа (в м/с) и частоты связаны соотношением (см. формулу). В приведенной формуле <i>c</i>=1500 м/с — скорость звука в воде,' \
           ' f0 — частота испускаемого сигнала  (в МГц), f — частота отражённого сигнала (в МГц). Найдите частоту' \
           ' отражённого сигнала (в МГц), если батискаф погружается со скоростью {} м/с. Ответ округлите до целых.'.format(freq, speed)
    answer = round(freq * (1500 + speed) / (1500 - speed))
    return {'text': text, 'answer': answer, 'image': 'batiskaf.png'}

def task11():
    v1 = random.randint(60, 90)
    den_b = random.randint(2, 4)
    v2 = abs(v1 - 60 / den_b)
    dv_sign = random.choice([-1, 1])
    if den_b == 2:
        dt = random.choice([12, 24, 30, 48])
    else:
        dt = random.choice([15, 30, 45])
    answer = (v1 + dv_sign * v2) * dt / 60

    if dv_sign == -1:
        text = "Автомобиль, движущийся с постоянной скоростью {} км/ч по прямому шоссе, обгоняет другой автомобиль, движущийся в ту же сторону с постоянной скоростью {} км/ч. Каким будет расстояние (в километрах) между этими автомобилями через {} минут после обгона? ".format(
            v1, v2, dt)
    else:
        text = "Два автомобиля движутся по прямому шоссе в противоположных направлениях с постоянными скоростьями {} км/ч и {} км/ч. На сколько увеличится расстояние (в километрах) между ними через {} минут? ".format(
            v1, v2, dt)
    text += "Ответ округлите до второго знака после запятой."
    return {'text': text, 'answer': answer, 'image': None}

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

    ut.save_sympy_as_image(int_f, filename='images/math_task12.png')
    img = imread('images/math_task12.png')
    img = ut.add_equal_y(img)
    imsave('images/math_task12.png', ut.decrease_image(img))

    if ut.get_random(0, 1) <= 0.5:
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
    return {'text': text, 'answer': answer, 'image': 'math_task12.png'}