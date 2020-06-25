#!/usr/bin/python
import click
import os
from algorithms.ordenation import BubbleSort
from algorithms.ordenation import ShellSort
from algorithms.ordenation import MergeSort
from algorithms.ordenation import QuickSort
from algorithms.ordenation import HeapSort


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
    def bubble(input, asc):
        """Sort a list using BUBBLE SORT algorithm.
        """
        list = arg_to_list(input)
        algo = BubbleSort()
        obtained = algo.sort(list)
        show(obtained)

    @click.command()
    @click.option("--input", "-i", "input", required=True,
                  help="List to be sorted (e.g. [1,2,3])",
                  )
    @click.option('--asc/--asc-order', "-a", default=True, help='Sort list in ascending order')
    def shell(input, asc):
        """Sort a list using SHELL SORT algorithm.
        """
        list = arg_to_list(input)
        algo = ShellSort()
        obtained = algo.sort(list)
        show(obtained)

    @click.command()
    @click.option("--input", "-i", "input", required=True,
                  help="List to be sorted (e.g. [1,2,3])",
                  )
    @click.option('--asc/--asc-order', "-a", default=True, help='Sort list in ascending order')
    def merge(input, asc):
        """Sort a list using MERGE SORT algorithm.
        """
        list = arg_to_list(input)
        algo = MergeSort()
        obtained = algo.sort(list)
        show(obtained)

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

    @click.command()
    @click.option("--input", "-i", "input", required=True,
                  help="List to be sorted (e.g. [1,2,3])",
                  )
    @click.option('--asc/--asc-order', "-a", default=True, help='Sort list in ascending order')
    def heap(input, asc):
        """Sort a list using BUBBLE SORT algorithm.
        """
        list = arg_to_list(input)
        algo = HeapSort()
        obtained = algo.sort(list)
        show(obtained)

    # Add commands to group
    process.add_command(bubble)
    process.add_command(shell)
    process.add_command(merge)
    process.add_command(quick)
    process.add_command(heap)
