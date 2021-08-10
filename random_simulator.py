import numpy as np
from matplotlib import pyplot as plt
from tqdm import tqdm
from config import cfg
from game import ChampionLeagueEngine
from team import Team
import logging
import datetime
RANDOMTIME = int(100)
SIMTIME = int(3000)

def history_difference_kldivergence(history0, history1, sim_time=SIMTIME):
    prob_0 = history0 / sim_time
    prob_1 = history1 / sim_time

    kl_divergence = np.sum(
        prob_0 * np.log(prob_0 / prob_1)
    )
    return kl_divergence


cfg.is_revive = False
logging.basicConfig(filename='random_simulator.log', level=logging.INFO)
logging.info(f"time:{datetime.datetime.now()}")

kld_tracks = [[] for _ in range(4)]
for ran_index in tqdm(range(RANDOMTIME)):
    power_points = np.random.randint(30, 100, 4)
    improve_ratio = np.random.randint(20, 100) / 20.0

    cfg.improve_ratio = improve_ratio
    for i in range(4):
        cfg.teams[i].power_points = power_points[i]
    
    ## not revive
    cfg.is_revive = False
    revive_teams = [
        Team(**cfg.teams[i]) for i in range(len(cfg.teams))
    ]
    for i in range(SIMTIME):
        league = ChampionLeagueEngine(revive_teams, cfg)    
        rankings, history = league.run()
        for rank in rankings:
            team = rankings[rank]
            team.history[int(rank) - 1] += 1
    ## revive
    cfg.is_revive = True
    unrevive_teams = [
        Team(**cfg.teams[i]) for i in range(len(cfg.teams))
    ]
    for i in range(SIMTIME):
        league = ChampionLeagueEngine(unrevive_teams, cfg)    
        rankings, history = league.run()
        for rank in rankings:
            team = rankings[rank]
            team.history[int(rank) - 1] += 1

    for i in range(4):
        kld_tracks[i].append(history_difference_kldivergence(
            revive_teams[i].history, unrevive_teams[i].history
        ))

logging.info(f"time:{datetime.datetime.now()}")
logging.info(f"kldivergence_mean: {np.array(kld_tracks).mean()}")