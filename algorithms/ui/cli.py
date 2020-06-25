#!/usr/bin/python
import click
import os
from algorithms.ordenation import QuickSort


def arg_to_list(args):
    option = args
    try:
        option = str(option)
    except ValueError:
        pass

    option = option[1:-1]  # trim '[' and ']'

    options = option.split(',')

    for i, value in enumerate(options):
        # catch integers
        try:
            int(value)
        except ValueError:
            options[i] = value
        else:
            options[i] = int(value)
    return options


def show(result):
    print("Sorted list = ", end='')
    print(result)


class TerminalView():

    @click.group()
    def process():
        pass

    @click.command()
    @click.option("--input", "-i", "input", required=True,
                  help="List to be sorted (e.g. [1,2,3])",
                  )
    @click.option('--asc/--asc-order', "-a", default=True, help='Sort list in ascending order')
    def quick(input, asc):
        """Sort a list using QUICK SORT algorithm.
        """
        list = arg_to_list(input)
        algo = QuickSort()
        obtained = algo.sort(list)
        show(obtained)

    process.add_command(quick)
