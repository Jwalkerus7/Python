# Part of the Modules and Pip lessons

import random

feet_in_mile = 5280
meters_in_kilometer = 1000
code_language = ["Python", "Xamarin", "C#", "Javascript"]


def get_file_ext(filename):
    return filename[filename.index(".") + 1:]


def roll_dice(num):
    return random.randint(1, num)