import genshinstats as gs
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('url')

args = parser.parse_args()
authkey = gs.url_to_authkey(args.url)
data = gs.get_entire_gacha_log(authkey=authkey)

with open('gacha-history.pickle', 'wb') as f:
    pickle.dump(tuple(data), f)
