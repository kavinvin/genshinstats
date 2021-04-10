import genshinstats as gs
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('authkey')

args = parser.parse_args()
data = gs.get_entire_gacha_log(authkey=args.authkey)

with open('gacha-history.pickle', 'wb') as f:
    pickle.dump(tuple(data), f)
