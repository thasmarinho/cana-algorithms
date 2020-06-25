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


def show(result, is_desc):
    print("Sorted list = ", end='')
    if(is_desc):
        print(result[::-1])
    else:
        print(result)


class TerminalView():

    @click.group()
    def process():
        pass

    @click.command()
    @click.option("--input", "-i", "input", required=True,
                  help="List to be sorted (e.g. [1,2,3])",
                  )
    @click.option('--desc/--desc-order', "-d", default=False, help='Sort list in descending order')
    def bubble(input, desc):
        """Sort a list using BUBBLE SORT algorithm.
        """
        list = arg_to_list(input)
        algo = BubbleSort()
        obtained = algo.sort(list)
        show(obtained, desc)

    @click.command()
    @click.option("--input", "-i", "input", required=True,
                  help="List to be sorted (e.g. [1,2,3])",
                  )
    @click.option('--desc/--desc-order', "-d", default=False, help='Sort list in descending order')
    def shell(input, desc):
        """Sort a list using SHELL SORT algorithm.
        """
        list = arg_to_list(input)
        algo = ShellSort()
        obtained = algo.sort(list)
        show(obtained, desc)

    @click.command()
    @click.option("--input", "-i", "input", required=True,
                  help="List to be sorted (e.g. [1,2,3])",
                  )
    @click.option('--desc/--desc-order', "-d", default=False, help='Sort list in descending order')
    def merge(input, desc):
        """Sort a list using MERGE SORT algorithm.
        """
        list = arg_to_list(input)
        algo = MergeSort()
        obtained = algo.sort(list)
        show(obtained, desc)

    @click.command()
    @click.option("--input", "-i", "input", required=True,
                  help="List to be sorted (e.g. [1,2,3])",
                  )
    @click.option('--desc/--desc-order', "-d", default=False, help='Sort list in descending order')
    def quick(input, desc):
        """Sort a list using QUICK SORT algorithm.
        """
        list = arg_to_list(input)
        algo = QuickSort()
        obtained = algo.sort(list)
        show(obtained, desc)

    @click.command()
    @click.option("--input", "-i", "input", required=True,
                  help="List to be sorted (e.g. [1,2,3])",
                  )
    @click.option('--desc/--desc-order', "-d", default=False, help='Sort list in descending order')
    def heap(input, desc):
        """Sort a list using HEAP SORT algorithm.
        """
        list = arg_to_list(input)
        algo = HeapSort()
        obtained = algo.sort(list)
        show(obtained, desc)

    # Add commands to group
    process.add_command(bubble)
    process.add_command(shell)
    process.add_command(merge)
    process.add_command(quick)
    process.add_command(heap)
