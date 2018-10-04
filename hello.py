#!/usr/bin/env python
# Coding: utf-8

import os
import sys
import re


def get_question():
	question = str(input())
	return question.lower()


def say_hello():
    print('Hello !!!')
    response = input(
        'Do you want to know which version of python you are using ? [O/n]\n')
    return response


def which_python(response):
    if response == 'n':
        print('Good Bye !!!')
    else:
        print(sys.version)
        print('\nlocation:')
        print(os.path.dirname(sys.executable))


if __name__ == "__main__":
	which_python(say_hello())
