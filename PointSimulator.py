import requests

from bs4 import BeautifulSoup

import pandas as pd



def NBA_Scraper(url):
    s = requests.get(url).text
    soup = BeautifulSoup(s, 'html.parser')
    # get table
    soup_table = soup.find(class_='section_heading assoc_tgl_basic_playoffs')
    # get head
    soup_table_data = soup_table.find('thead')
    shead = soup_table_data.find_all('th')
    # get case value

    stats = []
    for th in shead:
        stat = th.get_text()
        stats.append(stat)
        # rint(th.get_text())
        #  get data stat value
        #  for th in shead:
        #  stat = th.get('data-stat')
        #  stats.append(stat)
    tbody = soup_table.find('tbody')
    tr_body = tbody.find_all('tr')
    games = []

    for trb in tr_body:
    # get id
    # print(trb.get('id'))
        th = trb.find('th')
        game_vals = []
    # game.append(th.get_text())
    # print(th.get_text())
    # print(th.get('data-stat'))
        for td in trb.find_all('td'):
        # get case value
            game_vals.append(td.get_text())
        # print(td.get_text())
        # get data-stat value
        # print(td.get('data-stat'))
        games.append(game_vals)

    # create dataframe from list of lists
    stats = list(filter(None, stats))

    #for i in stats:
        #if i == u'\xa0':
            #stats.remove(i)
    stats.remove('Team')
    stats.remove('Opponent')
    stats.remove('Rk')

    ## output whole table

    pd.set_option("display.max_rows", None, "display.max_columns", None)

    ## create dataframe, insert labels as columns
    df = pd.DataFrame(games, columns = stats)

    ## change column name for home/away
    df.columns.values[2] = 'Home/Away'
    df.columns.values[6] = 'Opponent'
    df.columns.values[24:-1] = df.columns[24:-1] + '1'

    return df



def NBA_Scraper1(url):
    s = requests.get(url).text
    soup = BeautifulSoup(s, 'html.parser')
    # get table
    soup_table = soup.find(class_='row_summable sortable stats_table')
    # get head
    soup_table_data = soup_table.find('thead')
    shead = soup_table_data.find_all('th')
    # get case value

    stats = []
    for th in shead:
        stat = th.get_text()
        stats.append(stat)
        # rint(th.get_text())
        #  get data stat value
        #  for th in shead:
        #  stat = th.get('data-stat')
        #  stats.append(stat)
    tbody = soup_table.find('tbody')
    tr_body = tbody.find_all('tr')
    games = []

    for trb in tr_body:
    # get id
    # print(trb.get('id'))
        th = trb.find('th')
        game_vals = []
    # game.append(th.get_text())
    # print(th.get_text())
    # print(th.get('data-stat'))
        for td in trb.find_all('td'):
        # get case value
            game_vals.append(td.get_text())
        # print(td.get_text())
        # get data-stat value
        # print(td.get('data-stat'))
        games.append(game_vals)

    # create dataframe from list of lists
    stats = list(filter(None, stats))

    #for i in stats:
        #if i == u'\xa0':
            #stats.remove(i)
    stats.remove("Advanced")
    stats.remove("Offensive Four Factors")
    stats.remove("Defensive Four Factors")
    stats.remove("Rk")

    ## output whole table

    pd.set_option("display.max_rows", None, "display.max_columns", None)

    ## create dataframe, insert labels as columns
    df = pd.DataFrame(games, columns = stats)

    ## change column name for home/away
    df.columns.values[2] = 'Home/Away'
    df.columns.values[6] = 'Opponent'
    df.columns.values[23:] = df.columns[23:] + '1'

    df['Total'] = df['Tm'].astype(float) + df['Opponent'].astype(float)

    return df


def col_float(df_col):
    df_col = pd.to_numeric(df_col, downcast = 'float')
    return df_col


#DAL = NBA_Scraper('https://www.basketball-reference.com/teams/DAL/2021/gamelog/')

#DAL1 = NBA_Scraper1('https://www.basketball-reference.com/teams/DAL/2022/gamelog-advanced/')

#LAL = NBA_Scraper('https://www.basketball-reference.com/teams/LAL/2022/gamelog/')

#LAL1 = NBA_Scraper1('https://www.basketball-reference.com/teams/LAL/2022/gamelog-advanced/')

#HOU = NBA_Scraper('https://www.basketball-reference.com/teams/HOU/2021/gamelog/')

#HOU1 = NBA_Scraper1('https://www.basketball-reference.com/teams/HOU/2021/gamelog-advanced/')

#UTA = NBA_Scraper('https://www.basketball-reference.com/teams/UTA/2021/gamelog/')

#UTA1 = NBA_Scraper1('https://www.basketball-reference.com/teams/UTA/2021/gamelog-advanced/')

#PHO = NBA_Scraper('https://www.basketball-reference.com/teams/PHO/2021/gamelog/')

#PHO1 = NBA_Scraper1('https://www.basketball-reference.com/teams/PHO/2022/gamelog-advanced/')

#CHO = NBA_Scraper('https://www.basketball-reference.com/teams/CHO/2021/gamelog/')

#CHO1 = NBA_Scraper1('https://www.basketball-reference.com/teams/CHO/2021/gamelog-advanced/')

#CLE = NBA_Scraper('https://www.basketball-reference.com/teams/CLE/2021/gamelog/')

#CLE1 = NBA_Scraper1('https://www.basketball-reference.com/teams/CLE/2022/gamelog-advanced/')

#PHI = NBA_Scraper('https://www.basketball-reference.com/teams/PHI/2021/gamelog/')

#PHI1 = NBA_Scraper1('https://www.basketball-reference.com/teams/PHI/2022/gamelog-advanced/')

#BKN = NBA_Scraper('https://www.basketball-reference.com/teams/BRK/2021/gamelog/')

BKN1 = NBA_Scraper1('https://www.basketball-reference.com/teams/BRK/2022/gamelog-advanced/')

#BKN1_Playoffs = NBA_Scraper1('https://www.basketball-reference.com/teams/BRK/2022/gamelog-advanced/')

#ORL = NBA_Scraper('https://www.basketball-reference.com/teams/ORL/2021/gamelog/')

#ORL1 = NBA_Scraper1('https://www.basketball-reference.com/teams/ORL/2021/gamelog-advanced/')

#NOP = NBA_Scraper('https://www.basketball-reference.com/teams/NOP/2021/gamelog/')

#NOP1 = NBA_Scraper1('https://www.basketball-reference.com/teams/NOP/2021/gamelog-advanced/')

#MIL = NBA_Scraper('https://www.basketball-reference.com/teams/MIL/2021/gamelog/')

#MIL1 = NBA_Scraper1('https://www.basketball-reference.com/teams/MIL/2022/gamelog-advanced/')

#NYK = NBA_Scraper('https://www.basketball-reference.com/teams/NYK/2021/gamelog/')

#NYK1 = NBA_Scraper1('https://www.basketball-reference.com/teams/NYK/2022/gamelog-advanced/')

#SAC = NBA_Scraper('https://www.basketball-reference.com/teams/SAC/2021/gamelog/')

#SAC1 = NBA_Scraper1('https://www.basketball-reference.com/teams/SAC/2021/gamelog-advanced/')

#DEN = NBA_Scraper('https://www.basketball-reference.com/teams/DEN/2021/gamelog/')

#DEN1 = NBA_Scraper1('https://www.basketball-reference.com/teams/DEN/2022/gamelog-advanced/')

#WAS = NBA_Scraper('https://www.basketball-reference.com/teams/WAS/2021/gamelog/')

#WAS1 = NBA_Scraper1('https://www.basketball-reference.com/teams/WAS/2021/gamelog-advanced/')

#CHO = NBA_Scraper('https://www.basketball-reference.com/teams/CHO/2021/gamelog/')

#CHO1 = NBA_Scraper1('https://www.basketball-reference.com/teams/CHO/2021/gamelog-advanced/')

#GSW = NBA_Scraper('https://www.basketball-reference.com/teams/GSW/2021/gamelog/')

#GSW1 = NBA_Scraper1('https://www.basketball-reference.com/teams/GSW/2022/gamelog-advanced/')

#SAS = NBA_Scraper('https://www.basketball-reference.com/teams/SAS/2021/gamelog/')

#SAS1 = NBA_Scraper1('https://www.basketball-reference.com/teams/SAS/2021/gamelog-advanced/')

#IND = NBA_Scraper('https://www.basketball-reference.com/teams/IND/2021/gamelog/')

#IND1 = NBA_Scraper1('https://www.basketball-reference.com/teams/IND/2021/gamelog-advanced/')

#POR = NBA_Scraper('https://www.basketball-reference.com/teams/POR/2021/gamelog/')

#POR1 = NBA_Scraper1('https://www.basketball-reference.com/teams/POR/2022/gamelog-advanced/')

#LAC = NBA_Scraper('https://www.basketball-reference.com/teams/LAC/2021/gamelog/')

#LAC1 = NBA_Scraper1('https://www.basketball-reference.com/teams/LAC/2022/gamelog-advanced/')

#BOS = NBA_Scraper('https://www.basketball-reference.com/teams/BOS/2021/gamelog/')

#BOS1 = NBA_Scraper1('https://www.basketball-reference.com/teams/BOS/2021/gamelog-advanced/')

#TOR = NBA_Scraper('https://www.basketball-reference.com/teams/TOR/2021/gamelog/')

#TOR1 = NBA_Scraper1('https://www.basketball-reference.com/teams/TOR/2021/gamelog-advanced/')

#MIA = NBA_Scraper('https://www.basketball-reference.com/teams/MIA/2021/gamelog/')

#MIA1 = NBA_Scraper1('https://www.basketball-reference.com/teams/MIA/2022/gamelog-advanced/')

#ORL = NBA_Scraper('https://www.basketball-reference.com/teams/ORL/2021/gamelog/')

#ORL1 = NBA_Scraper1('https://www.basketball-reference.com/teams/ORL/2021/gamelog-advanced/')

#MEM = NBA_Scraper('https://www.basketball-reference.com/teams/MEM/2021/gamelog/')

MEM1 = NBA_Scraper1('https://www.basketball-reference.com/teams/MEM/2022/gamelog-advanced/')

#ATL = NBA_Scraper('https://www.basketball-reference.com/teams/ATL/2021/gamelog/')

#ATL1 = NBA_Scraper1('https://www.basketball-reference.com/teams/ATL/2021/gamelog-advanced/')

#CHI1 = NBA_Scraper1('https://www.basketball-reference.com/teams/CHI/2022/gamelog-advanced/')

#MIN = NBA_Scraper('https://www.basketball-reference.com/teams/MIN/2022/gamelog/')

#MIN1 = NBA_Scraper1('https://www.basketball-reference.com/teams/MIN/2022/gamelog-advanced/')


def PointSim(teamDf, teamDfAdv, teamDf2, teamDfAdv2):
    Team1 = input('Enter First Team')
    Team2 = input('Enter Second Team')
    #Team_FGA = col_float(teamDf['FGA']).mean()
    #Team2_FGA = col_float(teamDf2['FGA']).mean()
    Team_avgPts = col_float(teamDf['Tm']).tail(10).mean()
    Team_avgOppPts = col_float(teamDf['Opponent']).tail(10).mean()
    Team2_avgPts = col_float(teamDf2['Tm']).tail(10).mean()
    Team2_avgOppPts = col_float(teamDf2['Opponent']).tail(10).mean()

    Team_FG = col_float(teamDf['FG%']).tail(10).mean()
    Team2_FG = col_float(teamDf2['FG%']).tail(10).mean()
    Team_Opp_FG = col_float(teamDf['FG%1']).tail(10).mean()
    Team2_Opp_FG = col_float(teamDf2['FG%1']).tail(10).mean()
    Team_3P = col_float(teamDf['3P%']).tail(10).mean()
    Team2_3P = col_float(teamDf2['3P%']).tail(10).mean()
    Team_Opp_3P = col_float(teamDf['3P%1']).tail(10).mean()
    Team2_Opp_3P = col_float(teamDf['3P%1']).tail(10).mean()
    Team_PACE = col_float(teamDfAdv['Pace']).tail(10).mean()
    Team2_PACE = col_float(teamDfAdv2['Pace']).tail(10).mean()
    Team_FTA = col_float(teamDf['FTA']).tail(10).mean()
    Team2_FTA = col_float(teamDf2['FTA']).tail(10).mean()
    Team_FT = col_float(teamDf['FT%']).tail(10).mean()
    Team2_FT = col_float(teamDf2['FT%']).tail(10).mean()
    Team_TOV = col_float(teamDf['TOV']).tail(10).mean()
    Team2_TOV = col_float(teamDf2['TOV']).tail(10).mean()
    Team_Opp_TOV = col_float(teamDf['TOV1']).tail(10).mean()
    Team2_Opp_TOV = col_float(teamDf2['TOV1']).tail(10).mean()
    Team_TOV_Game = (Team_TOV + Team2_Opp_TOV) / 2
    Team2_TOV_Game = (Team2_TOV + Team_Opp_TOV) / 2
    Team_OffReb = col_float(teamDf['ORB']).tail(10).mean()
    Team2_OffReb = col_float(teamDf2['ORB']).tail(10).mean()
    Team_Opp_OffReb = col_float(teamDf['ORB1']).tail(10).mean()
    Team2_Opp_OffReb = col_float(teamDf2['ORB1']).tail(10).mean()
    Proj_Pace = (Team_PACE + Team2_PACE) / 2
    Team_3PAr = col_float(teamDfAdv['3PAr']).tail(10).mean()
    Team2_3PAr = col_float(teamDfAdv['3PAr']).tail(10).mean()
    Team_FTr = col_float(teamDfAdv['FTr']).tail(10).mean()
    Team2_FTr = col_float(teamDfAdv['FTr']).tail(10).mean()

    Team_3PT_Attempts = ((Proj_Pace - Team_TOV_Game) + ((Team_OffReb + Team2_Opp_OffReb)/2)) * Team_3PAr #((Team_FG + Team2_Opp_FG)/2)
    Team_2PT_Attempts = (Proj_Pace - Team_TOV_Game) - Team_3PT_Attempts

    Team2_3PT_Attempts = ((Proj_Pace - Team2_TOV_Game) + ((Team2_OffReb + Team_Opp_OffReb)/2)) * Team2_3PAr
    Team2_2PT_Attempts = (Proj_Pace - Team2_TOV_Game) - Team2_3PT_Attempts

    Team_2PT = (Team_FG * ((Team_FG/.464) * (Team2_Opp_FG/.464))) * Team_2PT_Attempts * 2
    Team2_2PT = (Team2_FG * ((Team2_FG/.464) * (Team_Opp_FG/.464))) * Team2_2PT_Attempts * 2

    Team_3PT = (Team_3P * ((Team_3P/.368) * (Team2_Opp_3P/.368))) * Team_3PT_Attempts * 3
    Team2_3PT = (Team2_3P * ((Team2_3P/.368) * (Team_Opp_3P/.368))) * Team2_3PT_Attempts * 3

    Team_FTPoints = (Team_FTr * (Team_2PT_Attempts + Team_3PT_Attempts)) * Team_FT
    Team2_FTPoints = (Team2_FTr * (Team2_2PT_Attempts + Team2_3PT_Attempts)) * Team2_FT

    Team_TotalPoints = Team_2PT + Team_3PT + Team_FTPoints
    Team2_TotalPoints = Team2_2PT + Team2_3PT + Team2_FTPoints

    Team_W = teamDf[(teamDf['W/L'] == 'L')]
    Team_W_avgPts = (Team_W['Tm'].astype(float).tail(10).mean()) - (Team_W['Opponent'].astype(float).tail(10).mean())

    print(Team1,':', Team_TotalPoints)
    print(Team2,':', Team2_TotalPoints)
    print(Team1,':', Team_avgPts, Team_avgOppPts)
    print(Team2,':', Team2_avgPts, Team2_avgOppPts)
    print(Team_W_avgPts)

#LAC1_Avg_eFG = LAC1['eFG%'].astype(float).tail(10).mean(skipna = True)

#NOP1_Avg_eFG = NOP1['eFG%'].astype(float).tail(10).mean(skipna = True)

#LAC1_OppAvg_eFG = LAC1['eFG%1'].astype(float).tail(10).mean(skipna = True)

#NOP1_OppAvg_eFG = NOP1['eFG%1'].astype(float).tail(10).mean(skipna = True)

league_AverageDef = .5372

league_AverageOff = .5367

#LAL_factor = (LAL1_Avg_eFG/league_AverageDef) * (GSW1_OppAvg_eFG/league_AverageOff)

#GSW_factor = (GSW1_Avg_eFG/league_AverageDef) * (LAL1_OppAvg_eFG/league_AverageOff)

#LAL_ProjAvg = LAL1_Avg_eFG * LAL_factor

#GSW_ProjAvg = GSW1_Avg_eFG * GSW_factor

#print('LAL:', LAL_ProjAvg)

#print('GSW:', GSW_ProjAvg)



def PointSim1(team1,team2):

    #labels to print
    Team1 = input('Enter First Team: ')
    Team2 = input('Enter Second Team: ')


    teamA_Games = team1[(team1['eFG%'].astype(float) > .50) & (team1['eFG%'].astype(float) < .54)]
    teamB_Games = team2[(team2['eFG%'].astype(float) > .51) & (team2['eFG%'].astype(float) < .56)]


    #LAL_Games = LAL1[(LAL1['Opp'] == 'PHO')]

    #NOP1_Games_Away = NOP1[(NOP1['Home/Away'] == '@')]

    #ORL1_Games_L = ORL1[(ORL1['W/L'] == 'L')]

    #ORL1_GamesL_OppScore = ORL1_Games_L['Opponent'].astype(float).mean()

    #POR1_W_Pts = POR1_Games_W['Tm'].astype(float).mean()

    #SAS1_Games_HomeScore = SAS1_Games_Home['Tm'].astype(float).mean()


    #1_Games_3ptShooters = MIA1[(MIA1['Opp'] == 'CHO')]

    teamA_avgScore = teamA_Games['Tm'].astype(float).mean()

    teamB_avgScore = teamB_Games['Tm'].astype(float).mean()

#print('DAL:', DAL1_avgScore)

    #print(Team1,':', teamA_avgScore)

    #print(Team2,':', teamB_avgScore)

    print(Team1,'Total Last 5 Games:', team1['Tm'].astype(float).tail(5).mean(skipna = True))

    print(Team1, 'Opp Pts (last 5):', team1['Opponent'].astype(float).tail(5).mean(skipna=True))

    print(Team1,'ORtg (last 5):', team1['ORtg'].astype(float).tail(5).mean(skipna = True))

    print(Team1,'DRtg (last 5):', team1['DRtg'].astype(float).tail(5).mean(skipna = True))

    print(Team1,'Pace:', team1['Pace'].astype(float).tail(5).mean(skipna = True))

    print(Team2,'Total Last 5 Games:', team2['Tm'].astype(float).tail(5).mean(skipna = True))

    print(Team2, 'Opp Pts (last 5):', team2['Opponent'].astype(float).tail(5).mean(skipna=True))

    print(Team2,'ORtg:', team2['ORtg'].astype(float).tail(5).mean(skipna = True))

    print(Team2,'DRtg', team2['DRtg'].astype(float).tail(5).mean(skipna = True))

    print(Team2,'Pace', team2['Pace'].astype(float).tail(5).mean(skipna=True))




#print(BKN1.tail(10))

#print(LAC1_Games_NOP)


#print('SAS:', SAS_avgScore)

#PointSim(LAL, LAL1, GSW, GSW1)

#ORL2  = ORL1.[(ORL1['eFG%'] < .54).astype(float)])


PointSim1(BKN1,MEM1)



#print(DAL1['Tm'].astype(float).mean())


#games = MIL1[(MIL1['Opp'] == 'BKN')]

print(BKN1.tail(5))

print(MEM1.tail(5))






