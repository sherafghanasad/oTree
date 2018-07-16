from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


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
    pass

class Group(BaseGroup):
    piece_rate = models.CurrencyField(
        choices=currency_range(0.01, 0.1, 0.01)
    )

    guessed_piece_rate = models.CurrencyField(
        choices=currency_range(0.01, 0.1, 0.01)
    )

    points = models.IntegerField()
    guessed_points = models.IntegerField()

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

    Question1 = models.LongStringField(
        choices=["Work on a task for 10 minutes.",
                 "Select a bonus rate for a person who will work on a task.",
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

