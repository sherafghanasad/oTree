from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        if self.round_number == 1:
            yield (pages.ConsentForm, {'name': "BOT", 'profile_link': "bot.com"})

        if self.player.id_in_group == 1 and self.round_number == 1:

            yield (pages.InstructionsForEmployerBaseline)
            yield (pages.ControlQuestions, {'YourRole': "Employer", 'Periods': 10, 'Question3E': 10, 'Question3W': 0,
                                            'Question4E': 30, 'Question4W': 34, 'Question5E': 20, 'Question5W': 62})

        if self.player.id_in_group == 1:

            yield (pages.FirstStageBaseline1, {'proposed_wage': 50, 'random_wage': 25})
            yield (pages.FirstStageBaseline2, {'expected_effort': 0.5})

        if self.player.id_in_group == 2 and self.round_number == 1:

            yield (pages.InstructionsForWorkerBaseline)
            yield (pages.ControlQuestions, {'YourRole': "Worker", 'Periods': 10, 'Question3E': 10, 'Question3W': 0,
                                            'Question4E': 30, 'Question4W': 34, 'Question5E': 20, 'Question5W': 62})
        if self.player.id_in_group == 2:
            yield (pages.WorkerBaseline1, {'guessed_wage': 40})
            yield (pages.WorkerBaseline2, {'effort': 0.3})

        yield (pages.Result)