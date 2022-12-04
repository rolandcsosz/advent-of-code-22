# Advent of code Year 2022 Day 4 solution
# Author = Roland Csosz
# Date = December 2022

class Range():
    start:int
    end:int

    def __init__(self, assignment: str):
        range = assignment.split('-')
        self.start = int(range[0])
        self.end = int(range[1])
    

class Pair():
    first_range:Range
    second_range:Range

    def __init__(self, pair:str):
        assignments = pair.split(',')
        self.first_range = Range(assignments[0])
        self.second_range = Range(assignments[1])


    def is_fully_overlapping_pair(self) -> bool:
        if (self.second_range.start <= self.first_range.start <= self.second_range.end) and (self.second_range.start <= self.first_range.end <= self.second_range.end):
            return True
        if (self.first_range.start <= self.second_range.start <= self.first_range.end) and (self.first_range.start <= self.second_range.end <= self.first_range.end):
            return True
        return False


    def is_overlapping_at_all(self) -> bool:
        if (self.second_range.start <= self.first_range.start <= self.second_range.end) or (self.second_range.start <= self.first_range.end <= self.second_range.end):
            return True
        if (self.first_range.start <= self.second_range.start <= self.first_range.end) or (self.first_range.start <= self.second_range.end <= self.first_range.end):
            return True
        return False


def read_input_into_list(file_path:str) -> list[str]:
    with open(file_path, 'r') as file:
         return file.read().splitlines()


def get_number_of_overlaping_pairs(pairs: list[str], compare_method) -> int:
    counter = 0
    for string_pair in pairs:
        actual_pair = Pair(string_pair)
        if compare_method(actual_pair):
            counter += 1
    return counter


def main():
    all_pairs = read_input_into_list('day_4_input.txt')
    print("The total amount of range fully contain the other in pairs:", get_number_of_overlaping_pairs(all_pairs, Pair.is_fully_overlapping_pair))
    print("The total amount of fully and partly overlapping pairs:", get_number_of_overlaping_pairs(all_pairs, Pair.is_overlapping_at_all))


if __name__ == '__main__':
    main()

