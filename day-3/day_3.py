# Advent of code Year 2022 Day 3 solution
# Author = Roland Csosz
# Date = December 2022

def read_input_into_list(file_path:str) -> list[str]:
    with open(file_path, 'r') as file:
         return file.read().splitlines()

#ASCII magic
def get_priority_by_character(character:str) -> int:
    if(65 <= ord(character) <= 90):
        return ord(character)-38
    if(97 <= ord(character) <= 122):
        return ord(character)-96
    return 0


def get_share_item_from_rucksack_for_first_part(rucksack:str) -> str:
    rucksack_length = int(len(rucksack))
    compartment_length = int(rucksack_length/2)

    first_compartment = rucksack[0:compartment_length:1]
    second_compartment = rucksack[compartment_length:rucksack_length:1]
    common_items = list(set(first_compartment)&set(second_compartment))

    return common_items[0]


def calculate_sum_of_priorities_for_first_part(rucksacks:list[str]) -> int:
    sum = 0
    for rucksack in rucksacks:
        sum += get_priority_by_character(get_share_item_from_rucksack_for_first_part(rucksack))

    return sum


def get_share_item_from_rucksack_for_second_part(rucksacks:list[str]) -> str:
    common_items = rucksacks[0]

    for rucksack in rucksacks:
        common_items = list(set(common_items)&set(rucksack))

    return common_items[0]


def calculate_sum_of_priorities_for_second_part(rucksacks:list[str], group_size:int) -> int:
    sum = 0
    actual_group = []

    for rucksack in rucksacks:
        actual_group.append(rucksack)

        if len(actual_group) == group_size:
            sum += get_priority_by_character(get_share_item_from_rucksack_for_second_part(actual_group))
            actual_group.clear()

    return sum




def main():
    all_rucksacks = read_input_into_list('day_3_input.txt')
    print("The total summary of priorities:", calculate_sum_of_priorities_for_first_part(all_rucksacks))
    print("The total summary of priorities with new groups:", calculate_sum_of_priorities_for_second_part(all_rucksacks, 3))


if __name__ == '__main__':
    main()

