import flask_wtf
import wtforms

# import goal

# create a form
class GoalUpdateForm(flask_wtf.FlaskForm):
  # name = wtforms.StringField('Goal', [wtforms.validators.required()])
  name = wtforms.StringField('Goal', [wtforms.validators.required()])
  level = wtforms.StringField('Level', [wtforms.validators.required()])
  detail = wtforms.TextAreaField('Detail', [wtforms.validators.optional()])
  order = wtforms.IntegerField('Order', [wtforms.validators.optional()])

import flask
import auth
import model
from main import app

# create a route
# view function
@app.route('/goal/create/', methods=['GET', 'POST'])
# @auth.login_required
def goal_create():
  form = GoalUpdateForm()
  # take data from form, and save it in the db
  if form.validate_on_submit():
    goal_db = model.Goal(
        user_key=auth.current_user_key(),
        name=form.name.data,
        detail=form.detail.data,
        level=form.level.data,
        order=form.order.data,
      )
    goal_db.put()
    return flask.redirect(flask.url_for('welcome'))
  # show the form
  return flask.render_template(
      'goal_create.html',
      html_class='goal-create',
      title='Create Goal',
      form=form,
    )

import util

# @app.route('/goals/')
# @auth.login_required
# def goal_list():
#   # contact_dbs, goal_cursor = model.Goal.get_dbs(
#   #     user_key=auth.current_user_key(),
#   #   )
#   goals.query.fetch()
#   return flask.render_template(
#       'goal_list.html',
#       html_class='goal-list',
#       title='Goal List',
#       contact_dbs=goal_dbs,
#       next_url=util.generate_next_url(goal_cursor),
#     )

@app.route('/goals/')
@auth.login_required
def goal_list():
  goals = model.Goal.query().fetch()
  return flask.render_template(
      'goal_list.html',
      html_class='goal-list',
      title='Goal List',
      goals=goals,
    )
