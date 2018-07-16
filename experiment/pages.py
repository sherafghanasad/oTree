from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class InstructionsEmployerBaseline(Page):
    def is_displayed(self):
        return self.player.id_in_group == 1

class InstructionsWorkerBaseline(Page):
    def is_displayed(self):
        return self.player.id_in_group == 2

class EmployerDecision(Page):
    form_model = 'group'
    form_fields = ['piece_rate', 'guessed_points']

    def is_displayed(self):
        return self.player.id_in_group == 1

class ControlQuestionsEmployerBaseline(Page):
    form_model = 'player'
    form_fields = ['Question1', 'Question2', 'Question3', 'Question4', 'Question5', 'Question6E', 'Question6W',
                   'Question7E', 'Question7W']

    def Question1_error_message(self, value):
        if not (value == 'Select a bonus rate for a person who will work on a task.'):
            return ['That was incorrect, please reread the instructions and then try again.']

    def Question2_error_message(self, value):
        if not(value == 0):
            return ['That was incorrect, please reread the instructions and then try again.']

    def Question3_error_message(self, value):
        if not (value == 10):
            return ['That was incorrect, please reread the instructions and then try again.']

    def Question4_error_message(self, value):
        if not(value == 1):
            return ['That was incorrect, please reread the instructions and then try again.']
    def Question5_error_message(self, value):
        if not (value == 1):
            return ['That was incorrect, please reread the instructions and then try again.']

    def Question6E_error_message(self, value):
        if not(value == 1.5):
            return ['That was incorrect, please reread the instructions and then try again.']

    def Question6W_error_message(self, value):
        if not (value == 0):
            return ['That was incorrect, please reread the instructions and then try again.']

    def Question7E_error_message(self, value):
        if not(value == 0.8):
            return ['That was incorrect, please reread the instructions and then try again.']

    def Question7W_error_message(self, value):
        if not (value == 1.2):
            return ['That was incorrect, please reread the instructions and then try again.']

    def is_displayed(self):
        return self.player.id_in_group == 1

class ControlQuestionsWorkerBaseline(Page):
    form_model = 'player'
    form_fields = ['Question1', 'Question2', 'Question3', 'Question4', 'Question5', 'Question8']

    def Question1_error_message(self, value):
        if not (value == 'Work on a task for 10 minutes.'):
            return ['That was incorrect, please reread the instructions and then try again.']

    def Question2_error_message(self, value):
        if not(value == 0):
            return ['That was incorrect, please reread the instructions and then try again.']

    def Question3_error_message(self, value):
        if not (value == 10):
            return ['That was incorrect, please reread the instructions and then try again.']

    def Question4_error_message(self, value):
        if not(value == 1):
            return ['That was incorrect, please reread the instructions and then try again.']
    def Question5_error_message(self, value):
        if not (value == 1):
            return ['That was incorrect, please reread the instructions and then try again.']
    def Question8_error_message(self, value):
        if not (value == 'Some other participant'):
            return ['That was incorrect, please reread the instructions and then try again.']


    def is_displayed(self):
        return self.player.id_in_group == 2

class BonusWorkerBaseline1(Page):
    form_model = 'group'
    form_fields = ['guessed_piece_rate']

    def is_displayed(self):
        return self.player.id_in_group == 2

class BonusWorkerBaseline2(Page):
    form_model = 'group'
    form_fields = ['guessed_piece_rate']

    def is_displayed(self):
        return self.player.id_in_group == 2

class Task(Page):
    form_model = 'group'
    form_fields = ['points']

    timeout_seconds = 600

    def vars_for_template(self):
        return {'other_bonus': (0.1 - self.group.piece_rate)}

    def is_displayed(self):
        return self.player.id_in_group == 2


class ResultsBaseline(Page):
    pass

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        group = self.group
        p1 = group.get_player_by_id(1)
        p2 = group.get_player_by_id(2)

        p1.payoff = (0.10-group.piece_rate) * (group.points/100)
        p2.payoff = group.piece_rate * (group.points/100)

    def is_displayed(self):
        return self.player.id_in_group == 2

# class Results(Page):
#     pass

page_sequence = [
    InstructionsEmployerBaseline,
    InstructionsWorkerBaseline,
    # ControlQuestionsEmployerBaseline,
    ControlQuestionsWorkerBaseline,
    EmployerDecision,
    BonusWorkerBaseline1,
    BonusWorkerBaseline2,
    Task,
    ResultsWaitPage,
    ResultsBaseline
    # ResultsWaitPage,
    # Results
]
