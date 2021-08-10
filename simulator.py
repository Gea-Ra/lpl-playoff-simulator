from matplotlib import pyplot as plt
from tqdm import tqdm
from config import cfg
from game import ChampionLeagueEngine
from team import Team
import logging
import datetime
SIMTIME = int(1e6)

teams = [
    Team(**cfg.teams[i]) for i in range(len(cfg.teams))
]

cfg.is_revive = False
logging.basicConfig(filename='simulator.log', level=logging.INFO)
logging.info(f"time:{datetime.datetime.now()}")
logging.info(f"cfg:{cfg}")
logging.info(f"SIMTIME:{SIMTIME}")
for i in tqdm(range(SIMTIME)):
    league = ChampionLeagueEngine(teams, cfg)    
    rankings, history = league.run()
    for rank in rankings:
        team = rankings[rank]
        team.history[int(rank) - 1] += 1

for i, team in enumerate(teams):
    logging.info(f"Team {team.name}, average_ranking={team.mean_ranking()}")
    plt.subplot(4, 2, i+1)
    plt.title(f'Team {team.name}')
    team.plot_history()

logging.info(f"The probability of Team First, get first={teams[0].history[0] / SIMTIME},"+
f"second={teams[0].history[1] / SIMTIME}, third={teams[0].history[2] / SIMTIME}, fourth={teams[0].history[3] / SIMTIME}")


cfg.is_revive = True
teams_revived = [
    Team(**cfg.teams[i]) for i in range(len(cfg.teams))
]
logging.info(f"time:{datetime.datetime.now()}")
logging.info(f"cfg:{cfg}")
logging.info(f"SIMTIME:{SIMTIME}")
for i in tqdm(range(SIMTIME)):
    league = ChampionLeagueEngine(teams_revived, cfg)    
    rankings, history = league.run()
    for rank in rankings:
        team = rankings[rank]
        team.history[int(rank) - 1] += 1

for i, team in enumerate(teams_revived):
    logging.info(f"Team {team.name}, average_ranking={team.mean_ranking()}")
    plt.subplot(4, 2, i+1 + 4)
    plt.title(f'eam {team.name} in Revive')
    team.plot_history()

logging.info(f"The probability of Team First, get first={teams_revived[0].history[0] / SIMTIME},"+
f"second={teams_revived[0].history[1] / SIMTIME}, third={teams_revived[0].history[2] / SIMTIME}, fourth={teams_revived[0].history[3] / SIMTIME}")

plt.show()