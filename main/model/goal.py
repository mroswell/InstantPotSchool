from google.appengine.ext import ndb
import model

# class Goal has attributes
class Goal(model.Base):
    name = ndb.StringProperty(required=True)
    detail = ndb.StringProperty(default='')
    level = ndb.StringProperty(default='')
    order = ndb.IntegerProperty(default=0)
    author = ndb.StructuredProperty(User)

class Level(model.Base):
    name = ndb.StringProperty(required=True)
    goals = ndb.StructuredProperty(Goal, repeated=True)
    order = ndb.IntegerProperty(default=0)


