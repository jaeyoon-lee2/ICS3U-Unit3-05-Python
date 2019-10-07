#!/user/bin/env python3

# Created by: Jaeyoon
# Created on: Oct 2019
# This program displays the month of the year


def main():
    # this function displays the month of the year

    # input
    user_number = int(input("Enter the month as number " +
                            "(integer from 1 ~ 12): "))
    print("")

    # process
    if user_number == 1:
        # output
        print("January!")
    elif user_number == 2:
        print("February")
    elif user_number == 3:
        print("March")
    elif user_number == 4:
        print("April")
    elif user_number == 5:
        print("May")
    elif user_number == 6:
        print("June")
    elif user_number == 7:
        print("July")
    elif user_number == 8:
        print("August")
    elif user_number == 9:
        print("September")
    elif user_number == 10:
        print("October")
    elif user_number == 11:
        print("November")
    elif user_number == 12:
        print("December")
    else:
        print("Have no idea!")


if __name__ == "__main__":
    main()
