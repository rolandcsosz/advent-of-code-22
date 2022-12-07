# Advent of code Year 2022 Day 6 solution
# Author = Roland Csosz
# Date = December 2022

def read_input_into_string(file_path:str) -> str:
    with open(file_path, 'r') as file:
         return file.read()


def get_number_after_n_long_sequence(stream:str, length_of_sequence:int) -> int:
    for n in range(len(stream)-(length_of_sequence-1)):
        if len(set(stream[n:n+(length_of_sequence):1])) == length_of_sequence:
            return n+length_of_sequence


def main():
    stream = read_input_into_string('day_6_input.txt')
    print("The number of the last character after a 4 long sequence:", get_number_after_n_long_sequence(stream, 4))
    print("The number of the last character after a 14 long sequence:", get_number_after_n_long_sequence(stream, 14))

if __name__ == '__main__':
    main()