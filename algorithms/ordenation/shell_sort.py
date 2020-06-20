#!/usr/bin/python
class ShellSort():

    def sort(self, list):
        length = len(list)
        gap = length // 2

        if(length <= 1):
            return list

        while gap > 0:
            list = self.gap_insertion_sort(list, gap)
            gap = 1 if gap == 2 else gap * 5 // 11
        return list

    def gap_insertion_sort(self, list, gap):
        for i, element in enumerate(list[gap:], gap):
            while i >= gap and list[i - gap] > element:
                list[i] = list[i - gap]
                i -= gap
            list[i] = element
        return list
