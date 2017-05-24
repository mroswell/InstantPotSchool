# from __future__ import absolute_import
from google.appengine.ext import ndb
from api import fields

import model

# class Goal has attributes
class Goal(model.Base):
    name = ndb.StringProperty(required=True)
    detail = ndb.StringProperty(default='')
    level = ndb.StringProperty(default='')
    order = ndb.IntegerProperty(default=0)
    user_key = ndb.KeyProperty(kind=model.User, required=False, verbose_name=u'User Key')

class Level(model.Base):
    name = ndb.StringProperty(required=True)
    goals = ndb.KeyProperty(kind=Goal, required=False, verbose_name=u'Goal Key', repeated=True)
    order = ndb.IntegerProperty(default=0)


