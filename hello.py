#!/usr/bin/env python
# Coding: utf-8

import sys


def say_hello():
    print('Hello !!!')
    response = input(
        'Do you want to know which version of python you are using ? [O/n]')
    return response


def which_python(response):
    if response == 'n':
        print('Good Bye !!!')
    else:
        print(sys.version)


if __name__ == "__main__":
    which_python(say_hello())
