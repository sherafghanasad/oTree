from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
# from otree_tools.fields import OtherModelField
from otree_tools.models.fields import OtherModelField

# from .fields import OtherModelField
from django.db import models as django_models
import random
from django import forms as djforms

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
    gender = OtherModelField(
        choices=['Male', 'Female', 'Prefer not to answer'],
        # widget=widgets.RadioSelect
    )
    race = OtherModelField(
        choices=['American Indian or Alaskan Native', 'Asian (including East and South Asia)', 'Black or African-American', 'Hispanic or Latino',
                 'Native Hawaiian or other Pacific Islander', 'White or Caucasian', 'Prefer not to answer'],
    )
    age = models.StringField(
        choices=['Under 18', '18-24', '25-30', '31-40', '41-50', '51-64', '65 or over', 'Prefer not to answer'],
        widget=widgets.RadioSelect
    )
    education = OtherModelField(
        choices=['Less than high school', 'High School or equivalent', 'Vocational/Technical School', 'Some College',
                 'College Graduate', "Master's Degree", 'Doctoral Degree', 'Professional Degree', 'Prefer not to answer'],
        # widget=widgets.RadioSelect
    )
    testimage = django_models.TextField()
    delete_photo = models.BooleanField()
    consent = models.BooleanField(widget=djforms.CheckboxInput,
                                  initial=False
                                  )