import random
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Sher Afghan Asad'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'gift_exchange'
    players_per_group = 2
    num_rounds = 10
    lowest_wage = 20
    highest_wage = 120

    efforts = [i / 10 for i in range(1, 11)]
    costs = [0, 1, 2, 4, 6, 8, 10, 12, 15, 18]

class Subsession(BaseSubsession):
    def creating_session(self):
        print('in creating_session')
        if self.round_number == 1:
            paying_round = random.randint(1, Constants.num_rounds)
            self.session.vars['paying_round'] = paying_round
            print('set the paying round to', paying_round)

            # players = self.get_players()

            self.group_randomly(fixed_id_in_group=True)

    # effort_cost = [
    #     {'effort': 0.1, 'cost': 0},
    #     {'effort': 0.2, 'cost': 1},
    #     {'effort': 0.3, 'cost': 2},
    #     {'effort': 0.4, 'cost': 4},
    #     {'effort': 0.5, 'cost': 6},
    #     {'effort': 0.6, 'cost': 8},
    #     {'effort': 0.7, 'cost': 10},
    #     {'effort': 0.8, 'cost': 12},
    #     {'effort': 0.9, 'cost': 15},
    #     {'effort': 1, 'cost': 18},
    # ]
    #
    # def e_cost(effort_cost, e):
    #     return [c['cost'] for c in effort_cost if c['effort'] == e]

class Group(BaseGroup):
    proposed_wage = models.CurrencyField(
        choices=currency_range(Constants.lowest_wage, Constants.highest_wage, c(5)),
    )
    random_wage = models.IntegerField()

    guessed_wage = models.CurrencyField(
        choices=currency_range(Constants.lowest_wage, Constants.highest_wage, c(5)),
    )
    effort = models.FloatField(
        choices=Constants.efforts,
        widget=widgets.RadioSelect
    )

    def get_cost(self):
        return Constants.costs[Constants.efforts.index(self.effort)]

    expected_effort = models.FloatField(
        choices=Constants.efforts,
        widget=widgets.RadioSelect
    )

    effort_cost = models.IntegerField()

    multiplier = models.FloatField(
        choices=[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2],
        widget=widgets.RadioSelect
    )
    guessed_multiplier = models.FloatField(
        choices=[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2],
        widget=widgets.RadioSelect
    )
    def set_payoffs(self):
        print('in set_payoffs')
        employer = self.get_player_by_role('Employer')
        worker = self.get_player_by_role('Worker')

        if self.subsession.round_number == self.session.vars['paying_round']:
            employer.payoff = c((120 - self.random_wage) * self.effort)
            worker.payoff = c(self.random_wage - 20 - self.get_cost())



#    treatment = models.StringField()



class Player(BasePlayer):
    name = models.StringField()
    profile_link = models.StringField()

# Defining fields for the Control Questions.

    YourRole = models.StringField(
        choices=['Employer', 'Worker'],
        widget=widgets.RadioSelect
    )

    Periods = models.IntegerField()
    Question3E = models.IntegerField()
    Question3W = models.IntegerField()
    Question4E = models.IntegerField()
    Question4W = models.IntegerField()
    Question5E = models.IntegerField()
    Question5W = models.IntegerField()

    def role(self):
        if self.id_in_group == 1:
            return 'Employer'
        if self.id_in_group == 2:
            return 'Worker'

    def get_partner(self):
        return self.get_others_in_group()[0]
