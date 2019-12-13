"""Asynchronous HTTP Server"""

import pymongo
import tornado.ioloop
import tornado.web

DB_HOST = 'localhost'
DB_PORT = 27017


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
        ]
        tornado.web.Application.__init__(self, handlers)
        self.connection = pymongo.MongoClient(DB_HOST, DB_PORT)
        self.db = self.connection.tinder


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print(self.request.arguments)
        self.write('<div class="auth_done">Done</div>')


if __name__ == "__main__":
    app = Application()
    app.listen(3000)
    tornado.ioloop.IOLoop.current().start()
