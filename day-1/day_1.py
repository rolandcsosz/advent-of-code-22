# Advent of code Year 2022 Day 1 solution
# Author = Roland Csosz
# Date = December 2022

def read_input_into_list(file_path:str) -> list[str]:
    with open(file_path, 'r') as file:
         return file.read().splitlines()


def group_calories(food_list:list[str]) -> list[int]:
    grouped_list = []
    actual_calorie_counter = 0
    for food in food_list:
        if not food:
            grouped_list.append(actual_calorie_counter)
            actual_calorie_counter = 0
            continue
        actual_calorie_counter += int(food)
    return grouped_list


def get_summary_of_n_greatest(grouped_calories_list:list[int], number_of_greatest:int) -> int:

    number_of_iter = number_of_greatest
    summery_of_greatest = 0
    perm_list = grouped_calories_list

    if len(grouped_calories_list) < number_of_greatest:
        number_of_iter = len(grouped_calories_list)

    for calorie in range(number_of_iter):
        summery_of_greatest += max(perm_list)
        perm_list.remove(max(perm_list))

    return summery_of_greatest


def main():
    all_food = read_input_into_list('day_1_input.txt')
    grouped_calories = group_calories(all_food)
    print("The calories carried by the best Elf:", max(grouped_calories))
    print("The amount of calories carried by the top 3 Elf:", get_summary_of_n_greatest(grouped_calories,3))


if __name__ == '__main__':
    main()