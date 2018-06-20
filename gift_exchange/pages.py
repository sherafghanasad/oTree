from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, random


class ConsentForm(Page):
    form_model = 'player'
    form_fields = ['name', 'profile_link']

    def is_displayed(self):
        return self.round_number == 1

class InstructionsForEmployerBaseline(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.id_in_group == 1 and self.round_number == 1

    # def is_displayed(self):
    #     return self.round_number == 1

class InstructionsForWorkerBaseline(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.id_in_group == 2 and self.round_number == 1

    # def is_displayed(self):
    #     return self.round_number == 1

class ControlQuestions(Page):
    form_model = 'player'
    form_fields = ['YourRole', 'Periods', 'Question3E', 'Question3W', 'Question4E', 'Question4W', 'Question5E',
                   'Question5W']
    #check if the entered role is correct

    def YourRole_error_message(self, value):
        print('value is', value)
        if not (value == self.player.role()):
            return ['That was incorrect. You are assigned the role of', self.player.role(), 'in this experiment']

    def Periods_error_message(self, value):
        print('value is', value)
        if not (value == Constants.num_rounds):
            return ['That was incorrect. There will be', Constants.num_rounds, 'periods in this experiment']

    def Question3E_error_message(self, value):
        print('value is', value)
        if not (value == 10):
            return ['That was incorrect. Employer earnings in this case will be (120 - 20) x 0.1 = 10']

    def Question3W_error_message(self, value):
        print('value is', value)
        if not (value == 0):
            return ['That was incorrect. Worker earnings in this case will be (20 - 20 - 0) = 0']

    def Question4E_error_message(self, value):
        print('value is', value)
        if not (value == 30):
            return ['That was incorrect. Employer earnings in this case will be (120 - 60) x 0.5 = 30']

    def Question4W_error_message(self, value):
        print('value is', value)
        if not (value == 34):
            return ['That was incorrect. Worker earnings in this case will be (60 - 20 - 6) = 34']

    def Question5E_error_message(self, value):
        print('value is', value)
        if not (value == 20):
            return ['That was incorrect. Employer earnings in this case will be (120 - 100) x 1 = 20']

    def Question5W_error_message(self, value):
        print('value is', value)
        if not (value == 62):
            return ['That was incorrect. Worker earnings in this case will be (100 - 20 - 18) = 62']

    def is_displayed(self):
        return self.round_number == 1

class FirstStageBaseline1(Page):
    form_model = 'group'
    form_fields = ['proposed_wage', 'random_wage']

    def vars_for_template(self):
        return {'rwage': random.randrange(Constants.lowest_wage, Constants.highest_wage, 5)}

    def is_displayed(self):
        return self.player.id_in_group == 1

class FirstStageBaseline2(Page):
    form_model = 'group'
    form_fields = ['expected_effort']

    def is_displayed(self):
        return self.player.id_in_group == 1

class WorkerBaseline1(Page):
    form_model = 'group'
    form_fields = ['guessed_wage']

    def is_displayed(self):
        return self.player.id_in_group == 2

class WorkerBaseline2(Page):
    form_model = 'group'
    form_fields = ['effort']

    def is_displayed(self):
        return self.player.id_in_group == 2

class Result(Page):
    form_model = 'group'
    form_fields = []

    def vars_for_template(self):
        return {'e_earnings': (120 - self.group.random_wage) * self.group.effort,
                'w_earnings': self.group.random_wage - 20 - self.group.get_cost()
                }

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs


page_sequence = [
    ConsentForm,
    InstructionsForEmployerBaseline,
    InstructionsForWorkerBaseline,
    ControlQuestions,
    FirstStageBaseline1,
    FirstStageBaseline2,
    ResultsWaitPage,
    WorkerBaseline1,
    WorkerBaseline2,
    ResultsWaitPage,
    Result
]
