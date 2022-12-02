# Advent of code Year 2022 Day 2 solution
# Author = Roland Csosz
# Date = December 2022

from enum import Enum

class OutcomeStatus(Enum):
    LOST = 0
    DRAW = 3
    WIN = 6

class Option(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

decode_dict_for_first_part = {  "A": Option.ROCK,
                                "B": Option.PAPER,
                                "C": Option.SCISSORS,
                                "X": Option.ROCK,
                                "Y": Option.PAPER,
                                "Z": Option.SCISSORS}

decode_dict_for_second_part = { "A": Option.ROCK,
                                "B": Option.PAPER,
                                "C": Option.SCISSORS,
                                "X": OutcomeStatus.LOST,
                                "Y": OutcomeStatus.DRAW,
                                "Z": OutcomeStatus.WIN}


def read_input_into_list(file_path:str) -> list[str]:
    with open(file_path, 'r') as file:
         return file.read().splitlines()


def decode_code(code:str, decode_dict:dict):
    return decode_dict.get(code)


def get_earned_points_from_simple_round(opponent_option:Option, option:Option) -> int:
    outcome_status = OutcomeStatus.WIN

    if(opponent_option == Option.ROCK and option != Option.PAPER):
        outcome_status = OutcomeStatus.LOST
    if(opponent_option == Option.SCISSORS and option != Option.ROCK):
        outcome_status = OutcomeStatus.LOST
    if(opponent_option == Option.PAPER and option != Option.SCISSORS):
        outcome_status = OutcomeStatus.LOST

    if(opponent_option == option):
        outcome_status = OutcomeStatus.DRAW

    return outcome_status.value + option.value


def get_earned_points_from_reverse_round(opponent_option:Option, outcome:OutcomeStatus) -> int:
    option = None

    if(opponent_option == Option.ROCK):
        option = Option.SCISSORS
        if(outcome == OutcomeStatus.WIN):
            option = Option.PAPER
    if(opponent_option == Option.PAPER):
        option = Option.ROCK
        if(outcome == OutcomeStatus.WIN):
            option = Option.SCISSORS
    if(opponent_option == Option.SCISSORS):
        option = Option.PAPER
        if(outcome == OutcomeStatus.WIN):
            option = Option.ROCK

    if(outcome == OutcomeStatus.DRAW):
        option = opponent_option

    return outcome.value + option.value


def calculate_sum_of_rounds(all_rounds:list[str], calculator_func, decode_dict:dict) -> int:
    sum = 0
    for round in all_rounds:
        sum += calculator_func(decode_code(round.split()[0], decode_dict), decode_code(round.split()[1], decode_dict))
    
    return sum  


def main():
    all_rounds = read_input_into_list('day_2_input.txt')
    print("The total score by all the rounds:", calculate_sum_of_rounds(all_rounds, get_earned_points_from_simple_round, decode_dict_for_first_part))
    print("The total score with new startegy:", calculate_sum_of_rounds(all_rounds, get_earned_points_from_reverse_round, decode_dict_for_second_part))


if __name__ == '__main__':
    main()

