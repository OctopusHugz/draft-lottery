#!/usr/bin/env python3
"""This module creates a draft lottery program for fantasy football leagues"""
import random
from typing import Dict, List


def assign_player_names() -> Dict:
    """ Assigns the names of each player based on final standings
        Return: A dictionary with player names as keys and number of balls
        as the value """
    team_1: str = input("Enter 12th place player's name: ")
    team_2: str = input("Enter 11th place player's name: ")
    team_3: str = input("Enter 10th place player's name: ")
    team_4: str = input("Enter 9th place player's name: ")
    team_5: str = input("Enter 8th place player's name: ")
    team_6: str = input("Enter 7th place player's name: ")
    return {
        team_1: 30,
        team_2: 24,
        team_3: 19,
        team_4: 14,
        team_5: 9,
        team_6: 4
    }


def assign_ball_numbers(player_dict: Dict):
    """ Randomly assigns the lottery ball numbers for each team """
    assigned_numbers: List = []
    numbers_dict: Dict = {}
    for name, number_of_balls in player_dict.items():
        numbers_list: List = []
        count: int = 0
        while count < number_of_balls:
            random_number = random.randrange(1, 101)
            if random_number in assigned_numbers:
                continue
            else:
                numbers_list.append(random_number)
                assigned_numbers.append(random_number)
                count += 1
        numbers_dict[name] = numbers_list
    return numbers_dict


def draft_lottery():
    """ Determines the draft order for the 6 lottery teams """
    player_dict: Dict = assign_player_names()
    numbers_dict: Dict = assign_ball_numbers(player_dict)
    picks_list: List = []
    draft_order: List = []
    print('\nStarting the lottery now...\n')
    while len(draft_order) < 6:
        random_number: int = random.randrange(1, 101)
        if random_number not in picks_list:
            for name, ball_numbers in numbers_dict.items():
                if random_number in ball_numbers and name not in draft_order:
                    picks_list.append(random_number)
                    draft_order.append(name)
                    print(f"Ball #{random_number} belongs to {name}")
    print(f"Drawn numbers are: {picks_list}\n")
    print("Draft order is:")
    for index, name in enumerate(draft_order):
        print(f"{index + 1}: {name}")


draft_lottery()
