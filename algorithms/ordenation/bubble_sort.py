#!/usr/bin/python
class BubbleSort():

    def sort(self,list):
        length = len(list)

        if(length <= 1):
            return list

        for n in range(length):
            for i in range(length - 1):
                if list[i] > list[i + 1]:
                    list[i], list[i+1] = list[i+1], list[i]

        return list
