# Author: Andrew Bittner
# Date: 11/2/2024

# Program #1: Item Counter
# Assume a file containing a series of names (as strings) is named names.txt 
# (Use the included example file names.txt) and exists on the computer's disk.
# Write a program that displays the number of names that are stored in the file.

def exit_sequence():
    # Function to keep console/window open until user ends program.
    input('\n\nPress [enter] to exit... ')

def count_file_lines():
    entries_list = []
    with open('names.txt', 'r') as infile:
        entry = infile.readline().rstrip()
        while entry != '':
            entries_list.append(entry)
            entry = infile.readline().rstrip()
    print('In the count_file_lines function: ')
    for entry in entries_list:
        print(entry)

# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()
    exit_sequence()