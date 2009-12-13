from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from models import Post
import myweb
import util
import access
import pages
import os

class s():
    @classmethod
    def w(self,what,my):
        my.response.out.write(what)

class Posting(webapp.RequestHandler):    
    def get(self,user_id):
        user = access.wall(self)
        if user:
            self.post(user_id)
            if (user_id == user.user_id()):
                query = Post.all()
                query.filter("user =", user_id)
                query.order("-created")
                posts = query.fetch(999)
                s.w(pages.posts_page(posts,user),self)
            else:
                self.redirect('/')
        else:
            pass
    def post(self,user_id):
        vals = myweb.get_post_vars()
        if (len(vals) == 0):
            vals = myweb.get_get_vars()
        ret = ""
        if len(vals) > 0:                
            for i in vals:
                ret += str(i) + ":" + str(vals[i]) + ", "
            apost = Post()
            apost.post =  ret
            apost.user = user_id        
            apost.put()           
        
class MainPage(webapp.RequestHandler):
    def get(self):
        user = access.wall(self)
        if user:
            self.redirect('/' + user.user_id())
            self.response.out.write(user.user_id())
            s.w(access.logout_link(),self)
        else:
            pass

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      (r'/(\d*)', Posting),
                                      ],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
