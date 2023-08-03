import pandas as pd
import numpy as np


def load_data(filename, has_header=True):
    '''
    Function to open the file into a dataframe
    Parameter: filename (str)
    Return: dataframe (pd.DataFrame)
    '''
    if has_header:
        base_df = pd.read_csv(filename)
    else:
        base_df = pd.read_csv(filename, header=None)  # Assuming there is no header
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
    print("Shots:", action_shots)
    if action_shots == 0:
        return 0
    else:
        action_makes_df = df[df['typeEvent'] == "Made Shot"]
        action_makes = action_makes_df['isShotMade'].count()
        action_percentage = round(action_makes / action_shots, 3)
        print(action_percentage)
        return action_percentage
    
def delete_none_finishes(df, column_name, target_string):
    df = df[df[column_name] != target_string]
    return df

def finishingHand_count(df, column_name, target_string):
    target_string_count = len(df[df[column_name] == target_string])
    return target_string_count


def filter_hand_df(base_df, hand):
    hand_df = pd.DataFrame()
    
    for _, row in base_df.iterrows():
        if row['finishingHand'] == hand:
            hand_df = hand_df.append(row)

    return hand_df


def finishingHand_percentage(df):
    hand_shots = df['isShotAttempted'].count()
    if hand_shots == 0:
        return 0
    else:
        hand_makes_df = df[df['typeEvent'] == "Made Shot"]
        hand_makes = hand_makes_df['isShotMade'].count()
        hand_percentage = round(hand_makes / hand_shots, 3)
        print(hand_makes)
        print(hand_shots)
        print(hand_percentage)
        return hand_percentage
    
def creating_driving_finishing_df(base_df, hand):
    finsihing_left_df = pd.DataFrame()
    finsihing_right_df = pd.DataFrame()

    
    for _, row in base_df.iterrows():
        if row['finishingHand'] == 'left':
            finsihing_left_df = finsihing_left_df.append(row)
        elif row['finishingHand'] == 'right':
            finsihing_right_df = finsihing_right_df.append(row)
        
    if hand == 'left':
        return finsihing_left_df
    elif hand == 'right':
        return finsihing_right_df