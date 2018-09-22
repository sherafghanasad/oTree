from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import os
import re
import base64
import random
dataUrlPattern = re.compile('data:image/(png|jpeg);base64,(.*)$')
from django.contrib.staticfiles.templatetags.staticfiles import static
#
# class DemographicSurvey(Page):
#     form_model = 'player'
#     form_fields = ['mturkid', 'gender', 'race', 'age', 'education', 'testimage']
#
#     def before_next_page(self):
#         ImageData = self.request.POST.get('testimage')
#         ImageData = dataUrlPattern.match(ImageData).group(2)
#
#         # If none or len 0, means illegal image data
#         if (ImageData == None or len(ImageData) == 0):
#             # PRINT ERROR MESSAGE HERE
#             pass
#
#         # Decode the 64 bit string into 32 bit
#         ImageData = base64.b64decode(ImageData)
#         print(ImageData)
#         BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#         path_to_file = os.path.join(BASE_DIR, 'static/experiment/photo{}.jpg'.format(self.participant.code))
#         f = open(path_to_file, 'wb' )
#         f.write( ImageData)
#         f.close()
#
# class Disqualified(Page):
#     def is_displayed(self):
#         return ((self.player.race != 'Black or African-American' and
#                 self.player.race != 'White or Caucasian') or
#                 self.player.age == 'Under 18')

class GroupingWaitPage(WaitPage):
#     pass
    group_by_arrival_time = True

    # def before_next_page(self):
    #     self.group.treatment = random.choice(['Baseline', 'Race Salient', 'Three Stage', 'Race Salient & Three Stage'])

    # randomize to treatments
    #     for g in self.get_groups():

        # print('set group.treatment to', self.group.treatment))

class InstructionsEmployer(Page):
    def is_displayed(self):
        return self.player.id_in_group == 1

    timer_text = 'You have 7 minutes maximum to read these instructions. If you finish early, you may proceed to the ' \
                 'next page. Time remaining:'

    timeout_seconds = 420

# class InstructionsEmployerRaceSalient(Page):
#     def is_displayed(self):
#         return (self.player.id_in_group == 1 and self.group.treatment == 'Race Salient')

class InstructionsWorker(Page):
    def is_displayed(self):
        return self.player.id_in_group == 2

class EmployerTask1(Page):
    def is_displayed(self):
        return self.player.id_in_group == 1

    timer_text = 'You have 2 minutes maximum to read this page. If you finish early, you may proceed to the ' \
                 'next page. Time remaining:'

    timeout_seconds = 120

class EmployerTask2(Page):
    form_model = 'group'
    form_fields = ['employer_points']

    timeout_seconds = 30

    def is_displayed(self):
        return self.player.id_in_group == 1

class EmployerDecision1(Page):
    form_model = 'group'
    form_fields = ['piece_rate', 'guessed_points', 'target_points']

    def is_displayed(self):
        return self.player.id_in_group == 1

    timer_text = 'You have 3 minutes maximum on this page. If you finish early, you may proceed to the ' \
                 'next page. Time remaining:'

    timeout_seconds = 180
    timeout_submission = {'piece_rate': 0,
                          'guessed_points': 0,
                          'target_points': 0}

class EmployerDecision2(Page):
    form_model = 'player'
    form_fields = ['testimage']

    def is_displayed(self):
        return self.player.id_in_group == 1

    def before_next_page(self):
        if self.timeout_happened != 1:
            ImageData = self.request.POST.get('testimage')
            ImageData = dataUrlPattern.match(ImageData).group(2)

            # If none or len 0, means illegal image data
            if (ImageData == None or len(ImageData) == 0):
                # PRINT ERROR MESSAGE HERE
                print('You must take a picture to continue')

            # Decode the 64 bit string into 32 bit
            ImageData = base64.b64decode(ImageData)
            # print(ImageData)
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            path_to_file = os.path.join(BASE_DIR, 'static/experiment/photo{}.jpg'.format(self.player.participant.code))
            f = open(path_to_file, 'wb' )
            f.write( ImageData)
            f.close()
            # if self.timeout_happened == 1:
            #     self.player.testimage = base64.b64encode('static/experiment/Black0.jpg')
        if self.timeout_happened:
            with open("experiment/static/experiment/Black0.jpg", "rb") as image_file:
                encoded_string = base64.standard_b64encode(image_file.read())
                Black0 = 'data:image/jpeg;base64,' + str(encoded_string)
                Black0 = Black0.replace('"', '')
                Black0 = Black0.replace('\'', '')
                Black0 = Black0.replace(',b/', ',/')

            with open("experiment/static/experiment/Black3.jpg", "rb") as image_file:
                encoded_string = base64.standard_b64encode(image_file.read())
                Black3 = 'data:image/jpeg;base64,' + str(encoded_string)
                Black3 = Black3.replace('"', '')
                Black3 = Black3.replace('\'', '')
                Black3 = Black3.replace(',b/', ',/')

            with open("experiment/static/experiment/Black6.jpg", "rb") as image_file:
                encoded_string = base64.standard_b64encode(image_file.read())
                Black6 = 'data:image/jpeg;base64,' + str(encoded_string)
                Black6 = Black6.replace('"', '')
                Black6 = Black6.replace('\'', '')
                Black6 = Black6.replace(',b/', ',/')

            with open("experiment/static/experiment/Black9.jpg", "rb") as image_file:
                encoded_string = base64.standard_b64encode(image_file.read())
                Black9 = 'data:image/jpeg;base64,' + str(encoded_string)
                Black9 = Black9.replace('"', '')
                Black9 = Black9.replace('\'', '')
                Black9 = Black9.replace(',b/', ',/')

            if self.group.piece_rate == 0:
                self.player.testimage = Black0
            if self.group.piece_rate == 0.03:
                self.player.testimage = Black3
            if self.group.piece_rate == 0.06:
                self.player.testimage = Black6
            if self.group.piece_rate == 0.09:
                self.player.testimage = Black9

    timer_text = 'You have 5 minutes maximum on this page. If you finish early, you may proceed to the ' \
                 'next page. Time remaining:'

    timeout_seconds = 300

    # with open("experiment/static/experiment/Black0.jpg", "rb") as image_file:
    #     encoded_string = base64.standard_b64encode(image_file.read())
    #     Black0 = 'data:image/jpeg;base64,' + str(encoded_string)
    #     Black0 = Black0.replace('"', '')
    #     Black0 = Black0.replace('\'', '')
    #     Black0 = Black0.replace(',b/', ',/')
    #
    # with open("experiment/static/experiment/Black3.jpg", "rb") as image_file:
    #     encoded_string = base64.standard_b64encode(image_file.read())
    #     Black3 = 'data:image/jpeg;base64,' + str(encoded_string)
    #     Black3 = Black3.replace('"', '')
    #     Black3 = Black3.replace('\'', '')
    #     Black3 = Black3.replace(',b/', ',/')
    #
    # with open("experiment/static/experiment/Black6.jpg", "rb") as image_file:
    #     encoded_string = base64.standard_b64encode(image_file.read())
    #     Black6 = 'data:image/jpeg;base64,' + str(encoded_string)
    #     Black6 = Black6.replace('"', '')
    #     Black6 = Black6.replace('\'', '')
    #     Black6 = Black6.replace(',b/', ',/')
    #
    # with open("experiment/static/experiment/Black9.jpg", "rb") as image_file:
    #     encoded_string = base64.standard_b64encode(image_file.read())
    #     Black9 = 'data:image/jpeg;base64,' + str(encoded_string)
    #     Black9 = Black9.replace('"', '')
    #     Black9 = Black9.replace('\'', '')
    #     Black9 = Black9.replace(',b/', ',/')

    # if group.piece_rate == 0:
    #     timeout_submission = {'testimage': Black0}
    # if group.piece_rate == 0.03:
    #     timeout_submission = {'testimage': Black3}
    # if group.piece_rate == 0.06:
    #     timeout_submission = {'testimage': Black6}
    # if group.piece_rate == 0.09:
    #     timeout_submission = {'testimage': Black9}



class ControlQuestionsEmployer(Page):
    form_model = 'player'
    form_fields = ['mturkid', 'Question1', 'Question2', 'Question3', 'Question4', 'Question5']

    timer_text = 'You have 7 minutes maximum to answer these questions. If you finish early, you may proceed to the ' \
                 'next page. Time remaining:'

    timeout_seconds = 420
    timeout_submission = {'mturkid':'NOT PROVIDED',
                          'Question1': 'Select a bonus rate for a team-member/worker who will work on a task.',
                          'Question2': 0,
                          'Question3': 9,
                          'Question4': True,
                          'Question5': True}

    def Question1_error_message(self, value):
        if (self.group.treatment == 'Baseline' or self.group.treatment == 'Race Salient'):
            if not (value == 'Select a bonus rate for a team-member/worker who will work on a task.'):
                return ['That was incorrect, please reread the instructions and then try again.']
        else:
            if not (value == 'Select a bonus rate and a reward decision for a person who will work on a task.'):
                return ['That was incorrect, please reread the instructions and then try again.']

    def Question2_error_message(self, value):
        if not(value == 0):
            return ['That was incorrect, please reread the instructions and then try again.']

    def Question3_error_message(self, value):
        if not (value == 9):
            return ['That was incorrect, please reread the instructions and then try again.']

    def Question4_error_message(self, value):
        if not(value == 1):
            return ['That was incorrect, please reread the instructions and then try again.']
    def Question5_error_message(self, value):
        if not (value == 1):
            return ['That was incorrect, please reread the instructions and then try again.']

    # def Question6E_error_message(self, value):
    #     if not(value == 1.5):
    #         return ['That was incorrect, please reread the instructions and then try again.']
    #
    # def Question6W_error_message(self, value):
    #     if not (value == 0):
    #         return ['That was incorrect, please reread the instructions and then try again.']
    #
    # def Question7E_error_message(self, value):
    #     if (self.group.treatment == 'Baseline' or self.group.treatment == 'Race Salient'):
    #         if not(value == 0.8):
    #             return ['That was incorrect, please reread the instructions and then try again.']
    #     else:
    #         if not(value == 0.72):
    #             return ['That was incorrect, please reread the instructions and then try again.']
    # def Question7W_error_message(self, value):
    #     if (self.group.treatment == 'Baseline' or self.group.treatment == 'Race Salient'):
    #         if not(value == 1.2):
    #             return ['That was incorrect, please reread the instructions and then try again.']
    #     else:
    #         if not(value == 1.28):
    #             return ['That was incorrect, please reread the instructions and then try again.']
    def is_displayed(self):
        return self.player.id_in_group == 1

class ControlQuestionsWorker(Page):
    form_model = 'player'
    form_fields = ['mturkid', 'Question1', 'Question2', 'Question3', 'Question4', 'Question5', 'Question8']

    def Question1_error_message(self, value):
        if not (value == 'Work on a task for 10 minutes.'):
            return ['That was incorrect, please reread the instructions and then try again.']

    def Question2_error_message(self, value):
        if not(value == 0):
            return ['That was incorrect, please reread the instructions and then try again.']

    def Question3_error_message(self, value):
        if not (value == 9):
            return ['That was incorrect, please reread the instructions and then try again.']

    def Question4_error_message(self, value):
        if not(value == 1):
            return ['That was incorrect, please reread the instructions and then try again.']
    def Question5_error_message(self, value):
        if not (value == 1):
            return ['That was incorrect, please reread the instructions and then try again.']
    def Question8_error_message(self, value):
        if not (value == 'Team member/boss'):
            return ['That was incorrect, please reread the instructions and then try again.']
    def Question9_error_message(self, value):
        if not (value == 1):
            return ['That was incorrect, please reread the instructions and then try again.']


    def is_displayed(self):
        return self.player.id_in_group == 2

class BonusWorker1(Page):
    form_model = 'group'
    form_fields = ['guessed_piece_rate', 'imaginary_piece_rate']

    def is_displayed(self):
        return self.player.id_in_group == 2

    def vars_for_template(self):
        return {
            'image_path': 'experiment/photo{}.jpg'.format(self.player.get_partner().participant.code)
        }
class BonusWorker2(Page):
    form_model = 'group'
    form_fields = []

    def is_displayed(self):
        return self.player.id_in_group == 2

    # def vars_for_template(self):
    #     return {
    #         'image_path': 'experiment/photo{}.jpg'.format(self.player.get_partner().participant.code)
    #     }
    def vars_for_template(self):
        return {
            'image_path': self.player.get_partner().testimage
        }

class BonusWorker3(Page):
    form_model = 'group'
    form_fields = []

    def is_displayed(self):
        return self.player.id_in_group == 2

    def vars_for_template(self):
        return {
            'image_path': self.player.get_partner().testimage
        }
class FairRate(Page):
    form_model = 'group'
    form_fields = ['fair_piece_rate']

    def is_displayed(self):
        return self.player.id_in_group == 2

class Task(Page):
    form_model = 'group'
    form_fields = ['points']

    timeout_seconds = 600

    timer_text = 'You have 10 minutes maximum to work on the task. Time remaining:'

    def vars_for_template(self):
        return {'other_bonus': (0.1 - self.group.piece_rate)}

    def is_displayed(self):
        return self.player.id_in_group == 2


class Results(Page):
    form_model = 'player'
    form_fields = ['Feedback']

    def vars_for_template(self):
        return {'reward': (0.1*((0.1 - self.group.piece_rate)*(self.group.points/100)))}

class SurveyCode(Page):
    pass

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        group = self.group
        p1 = group.get_player_by_id(1)
        p2 = group.get_player_by_id(2)

        if abs(group.guessed_points-group.points)<=50:
            p1.payoff = 1+(((0.10 - group.piece_rate) * (group.points / 100)) + 0.05)
        else:
            p1.payoff = 1+((0.10 - group.piece_rate) * (group.points / 100))

        if group.guessed_piece_rate == group.piece_rate:
            p2.payoff = 1+((group.piece_rate * (group.points / 100)) + 0.05)
        else:
            p2.payoff = 1+(group.piece_rate * (group.points / 100))

        # if group.points < group.target_points:
        #     p1.payoff = (0.10-group.piece_rate) * (group.points/100)
        #     p2.payoff = group.piece_rate * (group.points/100)
        # else:
        #     p1.payoff = 0.9*((0.10-group.piece_rate) * (group.points/100))
        #     p2.payoff = (group.piece_rate * (group.points/100))+(0.1*((0.10-group.piece_rate) * (group.points/100)))


    def is_displayed(self):
        return self.player.id_in_group == 2

class NormalWaitPage(WaitPage):
    def is_displayed(self):
        return self.player.id_in_group == 2


page_sequence = [
    # GroupingWaitPage,
    InstructionsEmployer,
    EmployerTask1,
    EmployerTask2,
    InstructionsWorker,
    ControlQuestionsEmployer,
    ControlQuestionsWorker,
    EmployerDecision1,
    EmployerDecision2,
    NormalWaitPage,
    BonusWorker1,
    BonusWorker2,
    BonusWorker3,
    Task,
    FairRate,
    ResultsWaitPage,
    Results,
    SurveyCode,
]
