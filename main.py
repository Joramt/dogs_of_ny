import sys
import json
import tornado.ioloop
import tornado.web
import tornado.options

from argparse import ArgumentParser
from lib.routing.handlers import CountHandler, MainHandler


def main():

    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/count", CountHandler),
    ])
    args = sys.argv[1:]
    port = (args[0][7:]) if args else 5000
    application.listen(port)
    print("Your tornado server is up and running ! || " +
          "\033[94m" +
          "http://localhost:" + str(port) +
          "\033[0m")
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
