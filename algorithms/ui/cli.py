#!/usr/bin/python
import click
from algorithms.ordenation import QuickSort


class TerminalView():

    @click.command()
    @click.option("--input", "-i", "option", required=True,
                  help="List to be sorted (e.g. [1,2,3])",
                  )
    def process(option):
        try:
            option = str(option)
        # option = str(option)  # this also works
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

        algo = QuickSort()
        obtained = algo.sort(options)
        print("Sorted list = ", end='')
        print(obtained)
