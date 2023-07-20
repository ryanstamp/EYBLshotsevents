import pandas as pd
import numpy as np


def load_data(filename):
    '''
    Function to open the file into a dataframe
    Parameter: file
    Return: dataframe, index column
    '''
    base_df = pd.read_csv(filename, index_col=0)
    return base_df

def filter_location_df(base_df, location):
    location_df = pd.DataFrame()
    
    for _, row in base_df.iterrows():
        if row['catchLocation'] == location:
            location_df = location_df.append(row)

    return location_df


def location_percentage(df):
    location_shots = df['isShotAttempted'].count()
    if location_shots == 0:
        return 0
    else:
        location_makes_df = df[df['typeEvent'] == "Made Shot"]
        location_makes = location_makes_df['isShotMade'].count()
        location_percentage = round(location_makes / location_shots, 3)
        print(location_percentage)
        return location_percentage


def filter_action_df(base_df, action):
    action_df = pd.DataFrame()
    
    for _, row in base_df.iterrows():
        if row['eventAction'] == action:
            action_df = action_df.append(row)

    return action_df

def action_percentage(df):
    action_shots = df['isShotAttempted'].count()
    if action_shots == 0:
        return 0
    else:
        action_makes_df = df[df['typeEvent'] == "Made Shot"]
        action_makes = action_makes_df['isShotMade'].count()
        action_percentage = round(action_makes / action_shots, 3)
        print(action_percentage)
        return action_percentage