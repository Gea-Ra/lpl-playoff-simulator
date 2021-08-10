from team import Team
from match import BOGame

class ChampionLeagueEngine:
    def __init__(self, teams, cfg):
        self.teams = teams
        self.improve_ratio = cfg.improve_ratio
        self.winning_points = cfg.winning_points
        self.is_revive = cfg.is_revive

    def run(self):
        rankings = {
            '1': None,
            '2': None,
            '3': None,
            '4': None,
        }
        meta_history = {}
        ## Four to two: # 1对4, 2对3; 种子排名高者优先选边
        game_0_result = BOGame.fight(self.teams[0], self.teams[3], 
                                     first_side_picker=self.teams[0],
                                     improve_ratio=self.improve_ratio,
                                     WINNING_POINTS=self.winning_points)
        meta_history['game_0_result'] = game_0_result
        game_1_result = BOGame.fight(self.teams[1], self.teams[2],
                                     first_side_picker=self.teams[1],
                                     improve_ratio=self.improve_ratio,
                                     WINNING_POINTS=self.winning_points)
        meta_history['game_1_result'] = game_1_result

        ## Winners Group， 种子排名高者第一场优先选边
        team_a = game_0_result['winner']
        team_b = game_1_result['winner']
        first_side_picker = team_a if team_a.index < team_b.index else team_b
        winners_group_result = BOGame.fight(team_a, team_b,
                                     first_side_picker=first_side_picker,
                                     improve_ratio=self.improve_ratio,
                                     WINNING_POINTS=self.winning_points)
        meta_history['winners_group_result'] = winners_group_result

        ## Losers Group， 种子排名高者第一场优先选边
        team_a = game_0_result['loser']
        team_b = game_1_result['loser']
        first_side_picker = team_a if team_a.index < team_b.index else team_b
        losers_group_result = BOGame.fight(team_a, team_b,
                                     first_side_picker=first_side_picker,
                                     improve_ratio=self.improve_ratio,
                                     WINNING_POINTS=self.winning_points)
        meta_history['losers_group_result'] = losers_group_result
        rankings['4'] = losers_group_result['loser']

        if not self.is_revive:
            # 单败赛制
            rankings['3'] = losers_group_result['winner']
            rankings['2'] = winners_group_result['loser']
            rankings['1'] = winners_group_result['winner']
        else:
            # 双败赛制

            ## 复活组决赛, 原胜者组败者 对 原败者组胜者; 原胜者组守垒并先选边
            team_a = winners_group_result['loser']
            team_b = losers_group_result['winner']
            first_side_picker = team_a
            revive_group_result = BOGame.fight(team_a, team_b,
                                     first_side_picker=first_side_picker,
                                     improve_ratio=self.improve_ratio,
                                     WINNING_POINTS=self.winning_points)
            meta_history['revive_group_result'] = revive_group_result
            rankings['3'] = revive_group_result['loser']

            ## 冠军赛， 胜者组胜者 对 复活组胜者; 胜者组获取优先选边
            team_a = winners_group_result['winner']
            team_b = revive_group_result['winner']
            first_side_picker = team_a
            champion_group_result = BOGame.fight(team_a, team_b,
                                     first_side_picker=first_side_picker,
                                     improve_ratio=self.improve_ratio,
                                     WINNING_POINTS=self.winning_points)
            meta_history['champion_group_result'] = champion_group_result
            rankings['2'] = champion_group_result['loser']
            rankings['1'] = champion_group_result['winner']
        return rankings, meta_history

if __name__ == '__main__':
    ## Testing
    from config import cfg
    teams = [
        Team(**cfg.teams[i]) for i in range(len(cfg.teams))
    ]
    league = ChampionLeagueEngine(teams, cfg)
    rankings, meta_history = league.run()
    print(rankings, meta_history)
            

