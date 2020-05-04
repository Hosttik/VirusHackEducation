import random as rnd
import pymorphy2
import numpy as np
from sympy import symbols, simplify, preview
from skimage.io import imread
import networkx as nx

MORPH = pymorphy2.MorphAnalyzer()

CITIES = ['Томск', 'Москва', 'Воронеж']
MONTHS = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']

# https://pymorphy2.readthedocs.io/en/latest/user/grammemes.html
def set_case(word: str, case: str):
    assert case in ['nomn', 'gent', 'datv', 'accs', 'ablt', 'loct', 'voct'], "Unknown word case!"
    parse = MORPH.parse(word)[0]
    return parse.inflect({case}).word

def get_random(a, b):
    return (b - a) * rnd.random() + a

def get_random_int(a, b):
    return rnd.randint(a, b)

def get_random_from_list(a):
    index = rnd.randint(0, len(a) - 1)
    return a[index]

def get_random_day_from_month():
    return rnd.randint(1, 30)

def get_random_interval_from_month(length):
    start = rnd.randint(1, 30 - length)
    return start, start + length

def get_random_month():
    return get_random_from_list(MONTHS)

def get_random_year():
    return get_random_from_list(range(2000, 2020))

def get_random_city():
    return get_random_from_list(CITIES)

def get_random_func(difficulty=2):
    degree_funcs = ['(x)**2', '(x)**3']
    trig_funcs = ['cos(x)', 'sin(x)']
    exp_ln_funcs = ['exp(x)', 'ln(x)']
    math_funcs = degree_funcs + trig_funcs + exp_ln_funcs
    x = symbols('x')
    funcs = rnd.sample(math_funcs, difficulty)
    new_funcs = []
    for func in funcs:
        func = simplify(func)
        func = func.subs(x, get_random_int(2, 5) * x + get_random_int(-7, 7))
        new_funcs.append(func)
    return sum(new_funcs)

def save_sympy_as_image(func, filename='temp/temp.png'):
    preview(func, viewer='file', filename=filename)

def add_equal_y(img):
    y_img = imread('images/y_equal.png')
    d = (img.shape[0] - y_img.shape[0]) // 2
    result = 255 * np.ones((img.shape[0], img.shape[1] + y_img.shape[1], 3), dtype=np.uint8)
    result[d:d + y_img.shape[0], 0:y_img.shape[1], :] = y_img
    result[:, y_img.shape[1]:, :] = img
    return result

def random_walk(G, steps, start=0):
    A = nx.adj_matrix(G).todense()
    nodes = list(G.nodes)
    if isinstance(start, str):
        point = nodes.index(start)
        path = [start]
    else:
        point = start
        path = [nodes[start]]
    for _ in range(steps):
        indexs = [i for i in range(A.shape[0]) if A[point, i] == 1]
        if len(indexs) == 0:
            break
        point = get_random_from_list(indexs)
        path.append(nodes[point])
    return path
