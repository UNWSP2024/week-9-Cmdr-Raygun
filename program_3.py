# Author: Andrew Bittner
# Date: 11/2/2024

# Program #3: Average Numbers
# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
# (please use the provided numbers.txt)
# Write a program that reads all of the numbers stored in the file and calculates their total.  

# The program should handle the following exceptions: 

# It should handle any IOError exceptions that are raised.
# It should handle any ValueError exceptions that are raised when the items that are read from the file 
# are converted to a number.

def exit_sequence():
    # Function to keep console/window open until user ends program.
    input('\n\nPress [enter] to exit... ')

def sum_numbers_from_file():
    num_list = []
    sum = 0.0
    with open('numbers.txt', 'r') as infile:
        entry = infile.readline().rstrip()
        while entry != '':
            try:
                num_list.append(float(entry))
            except IOError:
                print('Unable to read file. Program cannot continue.')
                exit_sequence()
            except ValueError:
                while True:
                    yn = input('Error reading value. Program can continue by skipping value. Would you like to continue? (y/n): ')
                    if yn == 'y':
                        break
                    elif yn == 'n':
                        exit_sequence()
                    else:
                        print('Please enter "y" or "n": ')
            except:
                print('An error occurred. Program cannot continue.')
                exit_sequence()
            entry = infile.readline().rstrip()
    for num in num_list:
        sum += num
    print(f'In file "numbers.txt":\nTotal of numbers is {sum}\nAverage of numbers is {sum/len(num_list)}')

# You don't need to change anything below this line:
if __name__ == '__main__':
    sum_numbers_from_file()
    exit_sequence()