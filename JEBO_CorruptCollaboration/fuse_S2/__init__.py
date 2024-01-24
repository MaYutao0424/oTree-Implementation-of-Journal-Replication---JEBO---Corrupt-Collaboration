from otree.api import *


doc = """
Your app description
"""

class C(BaseConstants):
    NAME_IN_URL = 'fuse_S2'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 1
    ENDOWMENT = 60
    DICE_R1 = 30
    DICE_R2 = 60
    DICE_R3 = 90

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    group_profit = models.IntegerField()


class Player(BasePlayer):
    reported_dice = models.IntegerField(
        choices=[1,2,3],
        widget=widgets.RadioSelectHorizontal,
        label='您将汇报的掷骰子结果为：'
    )
    original_dice = models.IntegerField()

    decision_order = models.IntegerField()

    guess_1 = models.IntegerField()
    guess_2 = models.IntegerField()
    guess_3 = models.IntegerField()

# 在该sesssion创建时，随机分配组别，并且将该组别一直保持下去
def creating_session(subsession):
    subsession.group_randomly()
    session = subsession.session
    session.GroupStructure = subsession.get_group_matrix()
    
# PAGES
class Instruction(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import random
        choice = random.choices([1, 2, 3])[0]
        player.original_dice = choice
        if player.id_in_group == 1:
            player.decision_order = 1
        elif player.id_in_group == 2:
            player.decision_order = 2
        else:
            player.decision_order = 3

class OrderInstruction_first(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.decision_order == 1

class OrderInstruction_second(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.decision_order == 2
    
class OrderInstruction_third(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.decision_order == 3

class DecisionPage_first(Page):
    form_model = 'player'
    form_fields = ['reported_dice']

    @staticmethod
    def is_displayed(player: Player):
        return player.decision_order == 1

class DecisionFirstWaitPage(WaitPage):
    title_text = '请耐心等待第一行动者做出选择'
    body_text = '请耐心等待第一行动者做出选择'

class DecisionPage_second(Page):
    form_model = 'player'
    form_fields = ['reported_dice']

    @staticmethod
    def vars_for_template(player: Player):
        first_mover = player.group.get_player_by_id(1)
        return {
            'first_mover': first_mover,
        }
    
    @staticmethod
    def is_displayed(player: Player):
        return player.decision_order == 2
    
class DecisionPage_third(Page):
    form_model = 'player'
    form_fields = ['reported_dice']

    @staticmethod
    def vars_for_template(player: Player):
        first_mover = player.group.get_player_by_id(1)
        second_mover = player.group.get_player_by_id(2)
        return {
            'first_mover': first_mover,
            'second_mover': second_mover,
        }
    
    @staticmethod
    def is_displayed(player: Player):
        return player.decision_order == 3
    
class DecisionSecondWaitPage(WaitPage):
    title_text = '请耐心等待第二行动者做出选择'
    body_text = '请耐心等待第二行动者做出选择'      

class DecisionThirdWaitPage(WaitPage):
    title_text = '请耐心等待第三行动者做出选择'
    body_text = '请耐心等待第三行动者做出选择'  

class DecisionWaitPage(WaitPage):
    title_text = '请耐心等待第三行动者做出选择'
    body_text = '请耐心等待第三行动者做出选择'
    @staticmethod
    def after_all_players_arrive(group: Group):
        p1_guess = group.get_player_by_id(1).reported_dice
        p2_guess = group.get_player_by_id(2).reported_dice
        p3_guess = group.get_player_by_id(3).reported_dice
        if p1_guess == p2_guess == p3_guess == 1:
            group.group_profit = C.DICE_R1
        elif p1_guess == p2_guess == p3_guess == 2:
            group.group_profit = C.DICE_R2
        elif p1_guess == p2_guess == p3_guess == 3:
            group.group_profit = C.DICE_R3
        else:
            group.group_profit = 0
        for p in group.get_players():
            p.payoff = C.ENDOWMENT + group.group_profit

class Results(Page):

    @staticmethod
    def vars_for_template(player: Player):
        p1 = player.group.get_player_by_id(1)
        p2 = player.group.get_player_by_id(2)
        p3 = player.group.get_player_by_id(3)

        return {
            'p1': p1,
            'p2': p2,
            'p3': p3,
        }

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.app_payoffs['Stage2_payoff'] = player.payoff

page_sequence = [Instruction,
                 OrderInstruction_first,OrderInstruction_second,OrderInstruction_third,
                 DecisionPage_first,DecisionFirstWaitPage,
                 DecisionPage_second,DecisionSecondWaitPage,
                 DecisionPage_third,DecisionThirdWaitPage,
                 DecisionWaitPage,
                 Results]
