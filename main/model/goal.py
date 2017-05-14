from google.appengine.ext import ndb
import model

class Goal(model.Base):
  user_key = ndb.KeyProperty(kind=model.User, required=True)
  goal = ndb.StringProperty(required=True)
  detail = ndb.StringProperty(default='')
  level = ndb.StringProperty(default='')
