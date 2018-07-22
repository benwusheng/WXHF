# -*- coding: utf-8 -*-
# filename: main.py
import web
from handle import Handle

urls = (
    '/', 'Handle',
)

# class Handle(object):
#     def GET(self):
#         return "hello GET"
#     def POST(self):
#         data=web.input()
#         return data

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()