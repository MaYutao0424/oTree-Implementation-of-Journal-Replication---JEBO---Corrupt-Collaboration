from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'fuse_S1'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 1
    ENDOWMENT = 60
    DICE_R1 = 0
    DICE_R2 = 30
    DICE_R3 = 60
    # 估计的偏离程度，如果估计的标准差小于等于1，则奖励 C.GUESS_R 元
    GUESS_R = 10

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    reported_dice = models.IntegerField(
        choices=[1,2,3],
        widget=widgets.RadioSelectHorizontal,
        label='您将汇报的掷骰子结果为：'
    )
    original_dice = models.IntegerField()

    guess_1 = models.IntegerField()
    guess_2 = models.IntegerField()
    guess_3 = models.IntegerField()

# PAGES
class Instruction(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import random
        choice = random.choices([1, 2, 3])[0]
        player.original_dice = choice
    
class DecisionPage(Page):
    form_model = 'player'
    form_fields = ['reported_dice']

class DecisionWaitPage(WaitPage):
    title_text = '请等待其他玩家做出选择'
    body_text = '请耐心等待其他玩家做出选择'

class Guess(Page):
    form_model = 'player'
    form_fields = ['guess_1', 'guess_2', 'guess_3']

    @staticmethod
    def vars_for_template(player: Player):
        subsession = player.group.subsession
        all_players = subsession.get_players()
        others_len = len(all_players) - 1
        return {
            'others_len': others_len
        }

    @staticmethod
    def error_message(player, values):
        subsession = player.group.subsession
        all_players = subsession.get_players()
        others_len = len(all_players) - 1
        if values['guess_1'] + values['guess_2'] + values['guess_3'] != others_len:
            return f'您所猜测每一点数下的玩家数量之和应该等于场上其他玩家的数量({others_len}人)，请重新输入'

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        subsession = player.group.subsession
        participant = player.participant
        all_players = subsession.get_players()
        r1 = r2 = r3 = 0
        for p in all_players:
            if p.id_in_subsession != player.id_in_subsession:
                if p.reported_dice == 1:
                    r1 += 1
                elif p.reported_dice == 2:
                    r2 += 1
                else:
                    r3 += 1

        participant.guess_results = {}
        participant.guess_results['r1_A'] = r1
        participant.guess_results['r2_A'] = r2
        participant.guess_results['r3_A'] = r3
        participant.guess_results['r1_G'] = player.guess_1
        participant.guess_results['r2_G'] = player.guess_2
        participant.guess_results['r3_G'] = player.guess_3
        
        guess_sd = (1/3*(player.guess_1 - r1)**2 + 1/3*(player.guess_2 - r2)**2 + 1/3*(player.guess_3 - r3)**2)**0.5
        participant.guess_results['guess_sd'] = guess_sd
        # 如果估计的标准差小于等于1，则奖励 C.GUESS_R 元
        if guess_sd <= 1:
            player.payoff = C.ENDOWMENT + C.GUESS_R + (player.reported_dice-1)*3
        else:
            player.payoff = C.ENDOWMENT + (player.reported_dice-1)*3
        
        participant.app_payoffs = {}
        participant.app_payoffs['Stage1_payoff'] = player.payoff
        
class Stage1EndWaitPage(WaitPage):
    title_text = '请等待其他玩家做出选择'
    body_text = '请耐心等待其他玩家做出选择'
    wait_for_all_groups = True

page_sequence = [Instruction, DecisionPage, DecisionWaitPage, Guess,Stage1EndWaitPage]
