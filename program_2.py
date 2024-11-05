# Author: Andrew Bittner
# Date: 11/2/2024

# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).

import random

def exit_sequence():
    # Function to keep console/window open until user ends program.
    input('\n\nPress [enter] to exit... ')

def validate_inp(inp, func, inp_msg ='Please re-enter your answer: '):
    # Set the loop control variable.
    repeat_cnv = True
    while repeat_cnv:
        #  Set the loop control variable to False so that loop does not run again on default.
        repeat_cnv = False
        try:
            # Execute input checker code.
            inp = func(inp)
        except ValueError:
            # Ask the user to input new data.
            print('Invalid input value. ', end='')
            inp = input(inp_msg)
            repeat_cnv = True
        except TypeError:
            # Ask the user to input new data.
            print('Invalid input type. ', end='')
            inp = input(inp_msg)
            repeat_cnv = True
        except:
            print('An error occurred. Program cannot continue.')
            exit_sequence()
    return inp

def check_in_range(inp):
    inp = int(inp)
    if inp not in range(1000):
        raise ValueError
    return inp

def main():
    with open('random_numbers.txt', 'w') as infile:
        rpt_cnt = validate_inp(input('Please enter how many numbers you would like written to the file; must be between 1 and 1000 (integer; digits only): '), check_in_range)
        for cnt in range(random.randint(1, rpt_cnt)):
            rand_num = random.uniform(1, 500)
            infile.write(str(rand_num) + '\n')
    print('Program completed successfully.')
    exit_sequence()

if __name__ == '__main__':
    main()