#!/usr/bin/env python
"""
A script to download Genshin Impact gacha history using url with authkey
"""

import genshinstats as gs
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('url')

args = parser.parse_args()
authkey = gs.url_to_authkey(args.url)
data = gs.get_entire_gacha_log(authkey=authkey)

filename = 'gacha-history.pickle'
with open(filename, 'wb') as f:
    pickle.dump(tuple(data), f)
    print(f'Saved to: {filename}')
