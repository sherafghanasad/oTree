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
    name_in_url = 'experiment'
    players_per_group = 2
    num_rounds = 1
    task_timer = 600

class Subsession(BaseSubsession):

    def creating_session(self):
        # randomize to treatments
        for g in self.get_groups():
            # g.treatment = random.choice(['Baseline', 'Race Salient', 'Three Stage', 'Race Salient & Three Stage'])
            g.treatment = random.choice(['Race Salient'])
            print('set group.treatment to', g.treatment)

    # group_by_arrival_time = True

class Group(BaseGroup):

    treatment = models.StringField()

    piece_rate = models.CurrencyField(
        choices=currency_range(0, 0.1, 0.03)
    )

    guessed_piece_rate = models.CurrencyField(
        choices=currency_range(0, 0.1, 0.03)
    )

    fair_piece_rate = models.CurrencyField(
        choices=currency_range(0, 0.1, 0.03)
    )

    points = models.IntegerField(default='0')
    guessed_points = models.IntegerField()
    target_points = models.IntegerField()

    # def set_payoffs(self):
    #     print('in set_payoffs')
    #     employer = self.get_player_by_role('Employer')
    #     worker = self.get_player_by_role('Worker')
    #
    #     employer.payoff = (0.10-self.piece_rate) * (self.points/100)
    #     worker.payoff = self.piece_rate * (self.points/100)

class Player(BasePlayer):

    def role(self):
        if self.id_in_group == 1:
            return 'Employer'
        if self.id_in_group == 2:
            return 'Worker'

    def get_partner(self):
        return self.get_others_in_group()[0]

    # mturkid = models.StringField()
    # gender = models.StringField(
    #     choices=['Male', 'Female', 'Other', 'Prefer not to answer'],
    #     widget=widgets.RadioSelect
    # )
    # race = models.StringField(
    #     choices=['American Indian or Alaskan Native', 'Asian', 'Black or African-American', 'Native Hawaiian or other Pacific Islander',
    #              'White or Caucasian', 'Other',  'Prefer not to answer'],
    #     widget=widgets.RadioSelect
    # )
    # age = models.StringField(
    #     choices=['Under 18', '18-24', '25-30', '31-40', '41-50', '51-64', '65 or over', 'Prefer not to answer'],
    #     widget=widgets.RadioSelect
    # )
    # education = models.StringField(
    #     choices=['High School', 'College', 'Graduate School', 'Other', 'Prefer not to answer'],
    #     widget=widgets.RadioSelect
    # )
    # testimage = models.LongStringField()
    #
    # delete_photo = models.BooleanField()

    Question1 = models.LongStringField(
        choices=["Work on a task for 10 minutes.",
                 "Select a bonus rate for a person who will work on a task.",
                 "Select a bonus rate and a reward decision for a person who will work on a task.",
                 "Select a bonus rate and work on a task."],
        widget=widgets.RadioSelect
    )

    Question2 = models.IntegerField()
    Question3 = models.IntegerField()
    Question4 = models.BooleanField(
        choices=[True, False]
    )
    Question5 = models.BooleanField(
        choices=[True, False]
    )
    Question6E = models.FloatField()
    Question6W = models.FloatField()

    Question7E = models.FloatField()
    Question7W = models.FloatField()
    Question8 = models.StringField(
        choices=['Some other participant',
                 'Experimenters/Researchers',
                 'Computer/Random']
    )
    Question9 = models.BooleanField(
        choices=[True, False]
    )

    Feedback = models.LongStringField(
        blank=True
    )
    mturkid = models.StringField()

    testimage = django_models.TextField(default='0')
    delete_photo = models.BooleanField()