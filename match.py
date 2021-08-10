from typing import Match, Tuple
import numpy as np
from team import Team
class MatchEngine:
    @staticmethod
    def _fight(point_a:float, point_b:float):
        return np.random.rand() < point_a / (point_a + point_b)

    @staticmethod
    def _get_points(team_a:Team, team_b:Team, meta_data:dict={})->Tuple[float, float]:
        improve_ratio = meta_data.get('improve_ratio', 1.0)
        side_picker = meta_data.get('side_picker', team_a)

        power_point_a = team_a.power_points
        power_point_b = team_b.power_points
        if side_picker is team_a:
            power_point_a = power_point_a * improve_ratio
        if side_picker is team_b:
            power_point_b = power_point_b * improve_ratio

        return power_point_a, power_point_b
    

    @staticmethod
    def fight(team_a:Team, team_b:Team, meta_data:dict={}):
        power_point_a, power_point_b = MatchEngine._get_points(team_a, team_b, meta_data)

        result = MatchEngine._fight(point_a=power_point_a, point_b=power_point_b)

        if result:
            winner = team_a
            loser  = team_b
        else:
            winner = team_b
            loser  = team_a

        return {
            'winner': winner,
            'loser' : loser
        }
        
class BOGame:
    @staticmethod
    def fight(team_a:Team, team_b:Team, first_side_picker:Team, improve_ratio:float=1.0, WINNING_POINTS:int=3):
        game_history={
            'team_a': team_a,
            'team_b': team_b,
            'WINNING_POINTS': WINNING_POINTS,
            'side_picker': [],
            'final_scores': [0, 0],
            'winner': None,
            'loser': None,
            'detailed_winners' : [],
        }

        meta_data = {
            'improve_ratio': improve_ratio,
            'side_picker': first_side_picker
        }

        while game_history['final_scores'][0] < WINNING_POINTS and game_history['final_scores'][1] < WINNING_POINTS:
            result = MatchEngine.fight(team_a, team_b, meta_data)

            game_history['side_picker'].append(meta_data['side_picker'])
            if result['winner'] is team_a:
                game_history['final_scores'][0] += 1
            else:
                game_history['final_scores'][1] += 1
            game_history['detailed_winners'].append(result['winner'].name)

            meta_data['side_picker'] = result['loser']
        
        if game_history['final_scores'][0] == WINNING_POINTS:
            game_history['winner'] = team_a
            game_history['loser'] = team_b
        else:
            game_history['winner'] = team_b
            game_history['loser'] = team_a

        return game_history

