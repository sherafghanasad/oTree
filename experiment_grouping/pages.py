from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import os
import re
import base64
dataUrlPattern = re.compile('data:image/(png|jpeg);base64,(.*)$')
from django.contrib.staticfiles.templatetags.staticfiles import static


class Survey(Page):
    form_model = 'player'
    form_fields = ['mturkid', 'gender', 'race', 'age', 'education']

    def before_next_page(self):
        self.participant.vars['Race'] = self.player.race
        print('self.participant.vars[Race] is', self.participant.vars['Race'])
        # self.participant.vars['testimage'] = self.player.testimage

    # def after_all_players_arrive(self):
    #     self.subsession.make_groups()

page_sequence = [
    Survey
]
