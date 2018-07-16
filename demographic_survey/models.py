from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from django.db import models as django_models
import random


author = 'Sher Afghan Asad'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'demographic_survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    mturkid = models.StringField()
    gender = models.StringField(
        choices=['Male', 'Female', 'Other', 'Prefer not to answer'],
        widget=widgets.RadioSelect
    )
    race = models.StringField(
        choices=['American Indian or Alaskan Native', 'Asian', 'Black or African-American', 'Native Hawaiian or other Pacific Islander',
                 'White or Caucasian', 'Other',  'Prefer not to answer'],
        widget=widgets.RadioSelect
    )
    age = models.StringField(
        choices=['Under 18', '18-24', '25-30', '31-40', '41-50', '51-64', '65 or over', 'Prefer not to answer'],
        widget=widgets.RadioSelect
    )
    education = models.StringField(
        choices=['High School', 'College', 'Graduate School', 'Other', 'Prefer not to answer'],
        widget=widgets.RadioSelect
    )
    testimage = django_models.TextField()
    delete_photo = models.BooleanField()