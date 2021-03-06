#!/usr/bin/python
import random


class QuickSort():

    def sort(self, list):
        less = []
        equal = []
        greater = []

        length = len(list)
        if length > 1:
            pivot = list[0]
            for value in list:
                if value < pivot:
                    less.append(value)
                elif value > pivot:
                    greater.append(value)
                else:
                    equal.append(value)
            return self.sort(less)+equal+self.sort(greater)
        else:
            return list

    def sort_with_two_pivots(self, list):
        less = []
        between = []
        greater = []

        length = len(list)
        if length > 1:
            pivots = self.get_pivots(list, 2)
            for value in list:
                if value < pivots[0]:
                    less.append(value)
                elif value > pivots[1]:
                    greater.append(value)
                else:
                    between.append(value)
            return self.sort(less)+between+self.sort(greater)
        else:
            return list

    def validate(self, list, number_of_pivots):
        length = len(list)
        if length < 1 or number_of_pivots < 1:
            raise Exception("Error: length or number of pivots is bellow minimum (1)")
        elif number_of_pivots > length:
            raise Exception("Sorry, the number of pivots should be below list's length")

    def get_pivots(self, list, number_of_pivots):
        """Get first elements from list as pivots.

        Parameters:
        list (list): list of elements
        number_of_pivots (int): size of returned pivots' list

        Returns:
        pivots (list): pivots in ascending order

       """
        self.validate(list, number_of_pivots)
        pivots = []
        for i, element in enumerate(list[:number_of_pivots]):
            pivots.append(element)

        return self.sort(pivots)

    def get_last_as_pivots(self, list, number_of_pivots):
        """Get first elements from list as pivots.

        Parameters:
        list (list): list of elements
        number_of_pivots (int): size of returned pivots' list

        Returns:
        pivots (list): pivots in ascending order

       """
        self.validate(list, number_of_pivots)
        pivots = []
        for i, element in enumerate(list[-number_of_pivots:]):
            pivots.append(element)

        return self.sort(pivots)

    def get_middle_as_pivot(self, list):
        middle = len(list) // 2
        return list[middle]

    def get_random_as_pivots(self, list, number_of_pivots):
        self.validate(list, number_of_pivots)
        return random.sample(list, number_of_pivots)

    def get_average_as_pivot(self, list):
        length = len(list)
        if(length < 1):
            average = 0
        elif(length == 1):
            average = list[0]
        elif(length == 2):
            average = (list[0] + list[1]) // 2
        else:
            middle = length // 2
            average = (list[0] + list[middle] + list[-1]) // 3

        return average
