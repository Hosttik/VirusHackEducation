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
import json
from bottle import run, route, response, request


#================================ GLOBAL VARS =====================================
all_ids = []


#================================ WRAPPER =========================================
def allow_cors(func):
    """ this is a decorator which enable CORS for specified endpoint """
    def wrapper(*args, **kwargs):
        response.headers['Access-Control-Allow-Origin'] = '*'
        return func(*args, **kwargs)
    return wrapper


#================================ INTERFACE FUNCTIONS =============================

@route('/test', method='GET')
@route('/test', method='POST')
@allow_cors
def get_new_session_id():
    print('SERVER: Connected')
    answer = {'result': True, 'test_field': 154}
    response.content_type = 'application/json'
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


# Server working directory
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='path/to/dir')



#================================ RUN SERVER ======================================
run(host='192.168.33.10', port=8080, debug=True, reloader=True)
