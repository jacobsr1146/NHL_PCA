import pandas as pd


def importfile(playersFile, goaliesFile):
    with open(playersFile) as f:
        encode = f.encoding

    with open(goaliesFile) as f:
        encode = f.encoding

    playerdf = pd.read_csv(playersFile, sep=',', encoding = encode, low_memory=False) # read in skaters_2020-21.csv file
    goaliedf = pd.read_csv(goaliesFile, sep=',', encoding = encode, low_memory=False) # read in goalies_2020-21.csv file

    for index, row in playerdf.iterrows():
        if row['situation'] != 'all':
            playerdf.drop([index], inplace = True)
    
    playerdf = playerdf[playerdf['games_played'] >= 20]
    
    playerinfo = playerdf.copy()
    playerstats = playerdf.copy()

    playerinfo.drop(columns=['playerId', 'season'], axis=1, inplace = True)
    playerinfo.drop(columns=playerinfo.columns[3:], axis=1, inplace = True)
    playerstats.drop(columns=['playerId', 'season', 'name', 'team', 'position', 'situation'], axis=1, inplace = True)

    #players = list(map(list, playerdf.to_numpy()))
    #goalies = list(map(list, goaliedf.to_numpy()))

    return playerinfo, playerstats



#players, goalies = importfile("NHLplayerstats_2019-20.csv", "NHLgoaliestats_2019-20.csv")
players, goalies = importfile("skaters_2020-21.csv", "goalies_2020-21.csv")


