"""
Writing and recalling names from a name list
Cside45 7/20/2022
"""
from work import *


def main():

    print('**welcome to your name list**')

    main_menu = int(input('to add a name press 1,'
                          ' to look up a name press 2,'
                          ' to print a name list press 3,'
                          ' to delete a name press 4,'
                          ' to quit press 5:'))

    if main_menu == 1:
        add()
        main()
    if main_menu == 3:
        recall_all()
        main()
    if main_menu == 2:
        recall_one()
        main()
    if main_menu == 4:
        delete_one()
        main()
    if main_menu == 5:
        print('**Now quitting Name List**')
        quit()
    if main_menu > 5:
        print('Please input a recognized value')
        main()
    if main_menu < 1:
        print('Please input a recognized value')
        main()


main()

