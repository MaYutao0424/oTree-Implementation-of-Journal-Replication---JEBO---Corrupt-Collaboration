from otree.api import *


doc = """
Your app description
"""

class C(BaseConstants):
    NAME_IN_URL = 'fuse_S3'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 5
    ENDOWMENT = 60
    DICE_R1 = 6
    DICE_R2 = 12
    DICE_R3 = 18

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    group_profit = models.FloatField()


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

    final_chosen_stage = models.StringField()
    
# PAGES
class BeginWaitPage(WaitPage):
    title_text = '请等待其他玩家进入游戏'
    body_text = '请耐心等待其他玩家进入游戏' 
    wait_for_all_groups = True

    @staticmethod
    def after_all_players_arrive(subsession):
        matrix = subsession.session.GroupStructure
        subsession.set_group_matrix(matrix)

        players = subsession.get_players()
        for p in players:
            import random
            choice = random.choices([1, 2, 3])[0]
            p.original_dice = choice
            if p.id_in_group == 1:
                p.decision_order = 1
            elif p.id_in_group == 2:
                p.decision_order = 2
            else:
                p.decision_order = 3

class Instruction(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class OrderInstruction_first(Page):
    @staticmethod
    def is_displayed(player: Player):
        if player.round_number == 1 and player.decision_order == 1:
            return True

class OrderInstruction_second(Page):
    @staticmethod
    def is_displayed(player: Player):
        if player.round_number == 1 and player.decision_order == 2:
            return True
    
class OrderInstruction_third(Page):
    @staticmethod
    def is_displayed(player: Player):
        if player.round_number == 1 and player.decision_order == 3:
            return True

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
            if p.round_number == 1:
                p.payoff = C.ENDOWMENT + group.group_profit
            else:
                prev_player = p.in_round(p.round_number - 1)
                p.payoff = prev_player.payoff + group.group_profit

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
        participant.app_payoffs['Stage3_payoff'] = player.payoff

        import random
        stages = ['Stage1_payoff','Stage2_payoff','Stage3_payoff']
        stage_selected = random.choice(stages)

        if stage_selected == 'Stage1_payoff':
            player.final_chosen_stage = '一'
        elif stage_selected == 'Stage2_payoff':
            player.final_chosen_stage = '二'
        else:
            player.final_chosen_stage = '三'

        participant = player.participant
        participant.payoff = participant.app_payoffs[stage_selected]

class FinalResults(Page):
    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        r1 = participant.guess_results['r1_A']  
        r2 = participant.guess_results['r2_A'] 
        r3 = participant.guess_results['r3_A'] 
        g1 = participant.guess_results['r1_G'] 
        g2 = participant.guess_results['r2_G'] 
        g3 = participant.guess_results['r3_G'] 
        guess_sd = round(participant.guess_results['guess_sd'],2)
        guess = False
        if guess_sd <= 1:
            guess = True
        else:
            pass

        return {
            'r1': r1,
            'r2': r2,
            'r3': r3,
            'g1': g1,
            'g2': g2,
            'g3': g3,
            'participant': participant,
            'guess_sd': guess_sd,
            'guess': guess,
        }
        
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS
    
page_sequence = [BeginWaitPage,Instruction,
                 OrderInstruction_first,OrderInstruction_second,OrderInstruction_third,
                 DecisionPage_first,DecisionFirstWaitPage,
                 DecisionPage_second,DecisionSecondWaitPage,
                 DecisionPage_third,DecisionThirdWaitPage,
                 DecisionWaitPage,
                 Results,FinalResults]
