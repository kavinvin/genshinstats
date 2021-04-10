import pickle
from funcy import curry

@curry
def groupby(f, xs):
    d = {}
    for x in xs:
        y = f(x)
        if y in d:
            d[y].append(x)
        else:
            d[y] = [x]
    return d

with open('gacha.pickle', 'rb') as f:
    data = pickle.load(f)

gacha_types = groupby(lambda x: x['gacha_type']['name'])(data)
for gacha_type, history in gacha_types.items():
    print('-' * 30)
    print('Gacha Type:', gacha_type)
    counter = 0
    for gacha in reversed(history):
        if gacha['rarity'] == 5:
            print(gacha['name'], counter + 1)
            counter = 0
        else:
            counter += 1
