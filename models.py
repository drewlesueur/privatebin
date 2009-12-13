from google.appengine.ext import db

class Post(db.Model):
    created = db.DateTimeProperty(auto_now_add=True)
    post = db.TextProperty()
    user = db.StringProperty()
