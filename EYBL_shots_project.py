'''
Programmer: Ryan Stampfli

EYBL Shots Porject

5/21/23

'''


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import json

def load_data(filename):
    '''
    Function to open the file into a dataframe
    Parameter: file
    Return: dataframe, index column
    '''
    base_df = pd.read_csv(filename, index_col=0)
    return base_df

def calculate_true_shooting(points, FGA, FTA):
    true_shooting_percentage = round(((points) / (2 * (FGA + (.44 * FTA)))), 3)
    return true_shooting_percentage

def calculate_EFG(two_point_FGM, three_point_FGM, FGA):
    effective_field_goal_perc = round((two_point_FGM + (1.5 * three_point_FGM)) / FGA, 3)
    return effective_field_goal_perc

def create_zone_shots(base_df, zone):
    zone_df = base_df[base_df['zoneBasic'] == zone]
    zone_shots = zone_df['isShotAttempted'].count()
    zone_makes_df = zone_df[zone_df['typeEvent'] == "Made Shot"]
    zone_makes = zone_makes_df['isShotMade'].count()
    zone_percentage = round(zone_makes / zone_shots, 3)

    return zone_percentage

def calculate_points(dataframe, FTM):

    shot_points_total = 0
    total_points = 0

    two_point_shot_df = dataframe[dataframe['typeShot'] == '2PT Field Goal']
    three_point_shot_df = dataframe[dataframe['typeShot'] == '3PT Field Goal']
    
    for _, row in two_point_shot_df.iterrows():
        if row['typeEvent'] == 'Made Shot':
            shot_points_total += 2

    for _, row in three_point_shot_df.iterrows():
        if row['typeEvent'] == 'Made Shot':
            shot_points_total += 3

    total_points = shot_points_total + FTM    

    return total_points

def count_unique_id_games(dataframe):

    unique_id_games = dataframe['idGame'].nunique()
    
    return unique_id_games

def rest_zone_by_side(base_df, zone, side):
    zone_df = base_df[base_df['zoneBasic'] == zone]
    zone_left_df = pd.DataFrame()
    zone_right_df = pd.DataFrame()
    zone_center_df = pd.DataFrame()

    
    for _, row in zone_df.iterrows():
        if row['locationX'] < -2:
            zone_left_df = zone_left_df.append(row)
        elif 2 >= row['locationX'] >= -2:
            zone_center_df = zone_center_df.append(row)
        elif row['locationX'] > 2:
            zone_right_df = zone_right_df.append(row)
    
    if side == 'left':
        return zone_left_df
    elif side == 'right':
        return zone_right_df
    elif side == 'center':
        return zone_center_df
    
def mid_zone_by_side(base_df, zone, side):
    zone_df = base_df[base_df['zoneBasic'] == zone]
    zone_left_df = pd.DataFrame()
    zone_right_df = pd.DataFrame()
    zone_center_df = pd.DataFrame()

    
    for _, row in zone_df.iterrows():
        if row['locationX'] < -6:
            zone_left_df = zone_left_df.append(row)
        elif 6 >= row['locationX'] >= -6:
            zone_center_df = zone_center_df.append(row)
        elif row['locationX'] > 6:
            zone_right_df = zone_right_df.append(row)
    
    if side == 'left':
        return zone_left_df
    elif side == 'right':
        return zone_right_df
    elif side == 'center':
        return zone_center_df
    
def corner_zone_by_side(base_df, zone, side):
    zone_df = base_df[base_df['zoneBasic'] == zone]
    zone_left_df = pd.DataFrame()
    zone_right_df = pd.DataFrame()
    zone_center_df = pd.DataFrame()

    
    for _, row in zone_df.iterrows():
        if row['locationX'] < 0:
            zone_left_df = zone_left_df.append(row)
        elif row['locationX'] > 0:
            zone_right_df = zone_right_df.append(row)
    
    if side == 'left':
        return zone_left_df
    elif side == 'right':
        return zone_right_df

def ATB_zone_by_side(base_df, zone, side):
    zone_df = base_df[base_df['zoneBasic'] == zone]
    zone_left_df = pd.DataFrame()
    zone_right_df = pd.DataFrame()
    zone_center_df = pd.DataFrame()

    
    for _, row in zone_df.iterrows():
        if row['locationX'] < -6:
            zone_left_df = zone_left_df.append(row)
        elif 6 >= row['locationX'] >= -6:
            zone_center_df = zone_center_df.append(row)
        elif row['locationX'] > 6:
            zone_right_df = zone_right_df.append(row)
    
    if side == 'left':
        return zone_left_df
    elif side == 'right':
        return zone_right_df
    elif side == 'center':
        return zone_center_df

def zone_side_percentage(df):
    zone_shots = df['isShotAttempted'].count()
    print(zone_shots)
    zone_makes_df = df[df['typeEvent'] == "Made Shot"]
    zone_makes = zone_makes_df['isShotMade'].count()
    print(zone_makes)
    zone_percentage = round(zone_makes / zone_shots, 3)

    return zone_percentage
