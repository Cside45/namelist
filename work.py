"""
these functions store and recall data from the list.txt
"""


def add():                            # this function adds a name to the .txt file
    name = input('Insert Name:')
    with open('list.txt', 'a') as r:  # opens file to append and creates variable "r" for the file
        r.write(name + "\n")          # writes the "name" input variable on a new line
    print(name, " ", "added")         # informs user that the name has been added
    r.close()                         # closes file


def recall_all():                     # This function prints the contents of the .txt file
    print('This will print the whole list')
    with open('list.txt', 'r') as r:  # opens file to append and creates variable "r" for the file
        print(r.read())               # prints  the whole files contents
    r.close
    print('**End of List**')          # informs user that the this is the end of the list


def recall_one():                     # This function recalls an individual name
    print('This will only recall a name on the selected line')
    with open('list.txt', 'r') as r:  # opens file to append and creates variable "r" for the file
        w = r.readlines()
        line_number = len(w) - 1      # gathers the length of the list and subtracts by 1 b/c the list starts at 0
        print('there are', line_number, 'lines')

        i = int(input('which line # would you like to view?:'))  # identifies which line the use wishes to see

        print('name number', i, 'is', w[i])  # reads the line number as chosen by the user's "i" variable


def delete_one():
    print('this will delete a selected name')

    with open('list.txt', 'r') as r:   # opens the .txt file as read only

        filelines = r.readlines()      # reads lines

        indx = 1                       # index number to ensure that selected # and input # line up

        linenumb = int(input("which line would you like to delete?:")) + 1  # adds 1 to the list so correct # deleted

        with open('list.txt', 'w') as g:

            for line in filelines:

                if indx != linenumb:

                    g.write(line)

                indx += 1

    print("Line ", linenumb - 1, ' is deleted')

















