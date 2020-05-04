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
from bottle import run, route, response, request

#================================ GLOBAL VARS =====================================
# all_ids = []
DISCIPLINES_IDS = ['math', 'info', 'rus']
DISCIPLINES = {'math': 'Математика', 'info': 'Информатика', 'rus': 'Русский язык'}
DISCIPLINES_IMGS = {}

#================================ WRAPPER =========================================
def allow_cors(func):
    """ this is a decorator which enable CORS for specified endpoint """
    def wrapper(*args, **kwargs):
        response.headers['Access-Control-Allow-Origin'] = '*'
        return func(*args, **kwargs)
    return wrapper

#================================ SERVER FUNCTIONS =============================
def discipline_img_path(imgid):
    imgpath = 'images/{}.jpg'.format(imgid)
    return imgpath

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
def get_desciplines():
    print('SERVER: Get disciplines')
    answer = [{'title': DISCIPLINES[d], 'id': d, 'image': discipline_img_path(d)} for d in DISCIPLINES_IDS]
    return json.dumps(answer)


# POST method
@route('/command-1', method='POST')
@route('/command-1', method='OPTIONS')
@allow_cors
def command_1():
    # get value
    value = request.forms.get('variable')
    print('command -> "variable" value:' + str(value))

    # get file
    image_data = request.files.get('file')

    # return json answer
    answer = {'is_success': True, 'content': {}, 'errors': []}
    return json.dumps(answer)


# GET method
@route('/command-2', method='GET')
@allow_cors
def command_2():
    # get value
    value = request.query.variable

    print('command-2 -> "variable" value: ' + str(value))

    # return json answer
    answer = {'is_success': True, 'content': {}, 'errors': []}
    return json.dumps(answer)


#================================ RUN SERVER ======================================
# run(host='192.168.33.10', port=8080, debug=True, reloader=True)
run(host='localhost', port=8080, debug=True, reloader=True)
