from easydict import EasyDict as edict

cfg = edict()
cfg.teams = [
    {'name': 'First',   'power_points': 100, 'index': 0}, 
    {'name': 'Second',  'power_points': 80,  'index': 1}, 
    {'name': 'Third',   'power_points': 60,  'index': 2}, 
    {'name': 'Fourth',  'power_points': 40,  'index': 3}, 
]

cfg.winning_points  = 3 # BO5
cfg.improve_ratio = 1.2 # side_picker improvement
cfg.is_revive = True    # Revive !
