import tornado.httpserver
import tornado.ioloop
import tornado.web
from operator import itemgetter, attrgetter

highscores=[]

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("tetris.html", title="My title", highscores=highscores)

class HighScoreHandler(tornado.web.RequestHandler):
    def post(self):
        name=self.get_argument("name")
        score=self.get_argument("score")
        if len(highscores)<=5:
            highscores.append((name,score))
            print 'hi'
            print highscores
        else:
            n=4
            while(n>=0 and score>highscores[n][1]):
                n=n-1
            highscores.insert(n+1,(name,score))
            highscores.pop()
                
application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/score", HighScoreHandler)
])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()