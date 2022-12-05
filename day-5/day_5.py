# Advent of code Year 2022 Day 5 solution
# Author = Roland Csosz
# Date = December 2022

import re

class CargoCrane():

    def __init__(self, start_state_lines: list[str]):
        self.stacks = []

        number_of_stacks = int((len(start_state_lines[0])+1)/4) # 3*n + n-1 character at the first line -> n stack

        places_with_values = {}
        for number in range(number_of_stacks):
            self.stacks.append([])
            places_with_values.update({(number+1)*4-2 : number}) # stack n -> letter at n*4-2 position in the line

        for line in start_state_lines:
            counter = 0
            for letter in line:
                counter += 1
                if counter in places_with_values.keys() and letter != " ":
                    self.stacks[places_with_values.get(counter)].append(letter)

        for stack in self.stacks:
            stack.pop()


    def execute_instructions(self, instruction_lines: list[str], is_order_retained:bool) -> None:
        format_string = 'move {number} from {source} to {destination}'

        for instruction in instruction_lines:
            lookup_dict = string_to_dict(instruction, format_string)
            self.move_crates(int(lookup_dict['number']), int(lookup_dict['source']), int(lookup_dict['destination']), is_order_retained)


    def move_crates(self, number:int, source:int, destination:int, is_order_retained:bool):
        movable_parts = self.stacks[source-1][0:number:1]
        if not is_order_retained:
            movable_parts = movable_parts[::-1]
        self.stacks[destination-1] = movable_parts + self.stacks[destination-1]
        self.stacks[source-1] = self.stacks[source-1][number:]


    def get_message(self) -> str:
        message = ""
        for stack in self.stacks:
            message += stack[0]
        return message


def read_input_into_list(file_path:str) -> list[str]:
    with open(file_path, 'r') as file:
         return file.read().splitlines()


def string_to_dict(string, pattern):
    regex = re.sub(r'{(.+?)}', r'(?P<_\1>.+)', pattern)
    values = list(re.search(regex, string).groups())
    keys = re.findall(r'{(.+?)}', pattern)
    return dict(zip(keys, values))


def get_inedex_of_separator_line(all_lines:list[str]) -> int:
    line_counter = 0
    for line in all_lines:
        if not line:
            break
        line_counter += 1
    return line_counter
    

def main():
    all_lines = read_input_into_list('day_5_input.txt')

    inedex_of_separator = get_inedex_of_separator_line(all_lines)

    start_state_lines = all_lines[0:inedex_of_separator:1]
    instruction_lines = all_lines[inedex_of_separator+1:len(all_lines):1]


    original_cargo_cane = CargoCrane(start_state_lines)
    original_cargo_cane.execute_instructions(instruction_lines, is_order_retained = False)
    print("The message after moving crates between stacks:", original_cargo_cane.get_message())

    new_cargo_cane = CargoCrane(start_state_lines)
    new_cargo_cane.execute_instructions(instruction_lines, is_order_retained = True)
    print("The message after moving crates between stacks with CrateMover 9001:", new_cargo_cane.get_message())


if __name__ == '__main__':
    main()

