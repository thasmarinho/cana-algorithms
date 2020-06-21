#!/usr/bin/python
class QuickSort():

    def sort(self,list):
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
