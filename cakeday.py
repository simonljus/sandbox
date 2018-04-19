# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
import re
import datetime


def validateDate(dd_string,mm_string):
    is_date_valid = False
    if len(dd_string) == 2 and dd_string[0] ==0:
        day = int(dd_string[1])
    else:
        day =int(dd_string)
    if len(mm_string) == 2 and mm_string[0] ==0:
        month = int(mm_string[1])
    else:
        month = int(mm_string)
    if month == 2 and day <= 29:
        is_date_valid = True 

    elif month in [4,6,9,11] and day <= 30:
        is_date_valid = True 
    elif month in [3,5,7,8,10,12]:
        is_date_valid = True
    else:
        pass

    return is_date_valid, day,month

def askPerson():
    name = ""
    birthday = ""
    ask_name = "What is your name? \n"
    ask_birthday = "When is your birthday? format [DD/MM]\n" 
    need_input = True
    ddmm_regex = "^(0?[1-9]|[12][0-9]|3[01])\/(0?[1-9]|1[0-2])$"
    ddmm_pattern = re.compile(ddmm_regex)
    while(need_input):
        if sys.version > "3":
            if name == "":
                name = input(ask_name)
            birthday = input(ask_birthday)
        else:
            if name == "":
                name = raw_input(ask_name).decode("utf-8")
            birthday = raw_input(ask_birthday)
        if ddmm_pattern.match(birthday):
            date_list = birthday.rstrip().split("/")
            is_valid_date, day,month = validateDate(date_list[0],date_list[1])
            if is_valid_date:
                need_input = False
            else:
                print("This date does not exist in mmdd format :) \n")
        else:
            print("You have to enter your birthday kin the correct format :) \n")
    today = datetime.datetime.today()
    if today.day == day and today.month == month:
        print("Happy birthday %s !!!!!! \n  Hope you have a wonderful day! \n" % (name))
    else:
        print("Today is not your birthday but have a good day anyway! \n")
if __name__ == "__main__":
    askPerson()