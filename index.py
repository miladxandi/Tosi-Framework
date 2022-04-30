#!C:\Users\Hossein\AppData\Local\Programs\Python\Python38\Python.exe
from Core.TemplateEngine import TemplateEngine as TemplateEngine
import os
import json
import route
import sys


_id = None


path = os.environ.get('REQUEST_URI')
method = os.environ.get('REQUEST_METHOD')
requested_body = sys.stdin.read()

# method = "GET"
# path= "/user"



if path in route.routes:
    if method in route.routes[path]["accepted_method"].split(','):
        controller = route.routes[path]["controller"]
    else:
        controller = "error.method_not_allowed"
else:
    controller = "error.not_found"







controller_items = controller.split('.')
_module = controller_items[0]
_attribute = controller_items[1]


Config={
    'engine':TemplateEngine,
    'method':method,
    'body':requested_body,
    'path':path
}



def run(Config, Controller, Function, Id):
    Method = getattr(Controller, Function)
    if Id != None:
        return Method(Config,Id)
    else:
        return Method(Config)


def route(Config,_module , _attribute, _id=None):
    module = __import__('Controllers.' + _module)
    instance = getattr(module, _module)
    return run(Config, instance, _attribute, _id)


if _module == 'api' :
    print('Content-type: application/json\r\n\r')
    #result = load_json("sample")
    result = "{\"" \
             "name\":\"Gonzalez\"}"
else:
    result = route(Config,_module, _attribute, _id)
    print('Content-type: text/html\r\n\r')




print(result)

