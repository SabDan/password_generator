import random
import sys


def main():
    header()
    user_input()
    password_generator()


def header():
    print('--------------------------------')
    print('     PASSWORD GENERATOR APP     ')
    print('--------------------------------')


def user_input():
    print("Password Must Be A Minimum of 6 Characters", "\n")


def password_generator():
    password_length = int(input("How long would you like your password to be: "))
    list_of_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                          'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                          'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                          '*', '$', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                          '^', '%', '#', '@', '!', ',', '.', '/', '|',
                          '>', '<', '(', ')', '+', '=', '-', '_', '{', '}',
                          '[', ']']

    password = random.sample(list_of_characters, password_length)  # sample returns a list

    if password_length <= 5:
        print("Sorry, password would be too short")
        password_generator()
    if password_length >= 6:
        print("Here is your password: ")
        for idx in password:
            print(idx,end="")

    print()

    while True:
        another_one = input("Would you like to change your password? (Y/N) : ")
        if another_one == "N":
            print("Goodbye")
            exit()
        elif another_one == "Y":
            password_generator()





if __name__ == '__main__':
    main()
