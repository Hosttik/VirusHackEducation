###################################################################################
###
### File:
###     python_server.py
###
###	Requirements:
### 	bottle
###		json
###
### Description:
###     This file is template for server interface
###
###################################################################################


#================================ PACKAGES ========================================
import os
import json
from bottle import run, route, response, request, static_file
import tasks.mathematic as t_math
import tasks.russian as t_rus
import pickle
import numpy as np
import matplotlib.pyplot as plt

#================================ GLOBAL VARS =====================================
# all_ids = []
DISCIPLINES_IDS = ['math', 'info', 'rus']
DISCIPLINES = {'math': 'Математика', 'info': 'Информатика', 'rus': 'Русский язык'}
MATH_TASKS = [('Работа с графиками', [t_math.task2]),
              ('Теория вероятностей', [t_math.task4]),
              ('Планиметрия', [t_math.task6]),
              ('Стереометрия', [t_math.task8]),
              ('Физические формулы', [t_math.task10]),
              ('Экстремумы', [t_math.task12])]
RUS_TASKS = [('Подбор местоимения', [t_rus.task2]),
             ('Ударения', [t_rus.task4]),
             ('Лексические ошибки', [t_rus.task6])]
DISCIPLINES_TASKS = {'math': MATH_TASKS, 'rus': RUS_TASKS}
RESULTS = []

#================================ WRAPPER =========================================
def allow_cors(func):
    """ this is a decorator which enable CORS for specified endpoint """
    def wrapper(*args, **kwargs):
        response.headers['Access-Control-Allow-Origin'] = '*'
        return func(*args, **kwargs)
    return wrapper

#================================ SERVER FUNCTIONS =============================
def discipline_img_path(imgid):
    imgpath = '{}.jpg'.format(imgid)
    return server_path(imgpath)

def server_path(imgpath):
    path = os.path.normpath('/static/' + imgpath).replace('\\', '/')
    return path



#================================ INTERFACE FUNCTIONS =============================
@route('/test', method='GET')
@route('/test', method='POST')
@allow_cors
def get_new_session_id():
    print('SERVER: Connected')
    answer = {'result': True, 'test_field': 154}
    response.content_type = 'application/json'
    return json.dumps(answer)


@route('/get_disciplines', method='GET')
@allow_cors
def get_disciplines():
    print('SERVER: Get disciplines')
    answer = [{'title': DISCIPLINES[d], 'id': d, 'image': discipline_img_path(d)} for d in DISCIPLINES_IDS]
    return json.dumps(answer)


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./images/')


@route('/get_discipline_tasks', method='GET')
@allow_cors
def get_discipline_tasks():
    disc_name = request.query.get('id')
    print('SERVER: Get tasks for discipline {}'.format(disc_name))
    tasks = DISCIPLINES_TASKS[disc_name]
    answer = []
    for i, task_group in enumerate(tasks):
        print('Progress.. {}/{}'.format(i + 1, len(tasks)))
        group_name = task_group[0]
        tasks_funcs = task_group[1]
        group_obj = {'title': group_name, 'list': []}
        for func in tasks_funcs:
            result = func()
            result['id'] = func.__name__
            result['answer'] = str(result['answer'])
            if result['image'] is not None:
                result['image'] = server_path(result['image'])
            group_obj['list'].append(result)
        answer.append(group_obj)
    return json.dumps(answer)


@route('/get_selected_tasks', method='GET')
@allow_cors
def get_selected_tasks():
    disc_name = request.query.get('disc')
    tasks_ids = request.query.get('ids').split('_')
    tasks = DISCIPLINES_TASKS[disc_name]
    answer = []
    for i, task_group in enumerate(tasks):
        print('Progress.. {}/{}'.format(i + 1, len(tasks)))
        tasks_funcs = task_group[1]
        for func in tasks_funcs:
            if func.__name__ in tasks_ids:
                result = func()
                result['id'] = func.__name__
                result['answer'] = str(result['answer'])
                if result['image'] is not None:
                    result['image'] = server_path(result['image'])
                answer.append(result)
    return json.dumps(answer)


@route('/save_result', method='GET')
@allow_cors
def save_result():
    disc_name = request.query.get('disc')
    path = request.query.get('path')
    percent = request.query.get('percent')
    RESULTS.append({'disc': disc_name, 'path': path, 'percent': percent})
    with open('results.pkl', 'wb') as f:
        pickle.dump(RESULTS, f)


@route('/get_results', method='GET')
@allow_cors
def get_results():
    data = {}
    for result in RESULTS:
        if result['disc'] in data:
            data[result['disc']].append(result['percent'])
        else:
            data[result['disc']] = [result['percent']]

    answer = []
    for key in data:
        imgname = 'result_{}.png'.format(key)
        scores = np.array([int(x) for x in data[key]])
        plt.figure(figsize=(12, 6))
        plt.plot(np.arange(1, len(scores) + 1), scores, '-o')
        plt.xticks(np.arange(1, len(scores) + 1))
        plt.grid()
        plt.savefig('images/{}'.format(imgname))

        answer.append({'disc': key, 'name': DISCIPLINES[key], 'image': server_path(imgname)})

    return json.dumps(answer)


@route('/load_results', method='GET')
@allow_cors
def load_results():
    disc_name = request.query.get('disc')

    answer = []
    for result in RESULTS:
        if result['disc'] == disc_name:
            obj = {'path': result['path'], 'percent': result['percent']}
            answer.append(obj)

    return json.dumps(answer)




#================================ RUN SERVER ======================================
if os.path.exists('results.pkl'):
    with open('results.pkl', 'rb') as f:
        RESULTS = pickle.load(f)

run(host='localhost', port=8080, debug=True, reloader=True)
