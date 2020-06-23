#!/usr/bin/python
class HeapSort():

    def sort(self, list):
        length = len(list)
        if(length < 1):
            return list

        middle = length // 2
        for i in range(middle, -1, -1):
            self.heapify(list, length, i)

        for i in range(length-1, 0, -1):
            list[i], list[0] = list[0], list[i]   # swap
            self.heapify(list, i, 0)
        return list

    def heapify(self, list, length, i):
        # Find largest among root and children
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < length and list[i] < list[l]:
            largest = l

        if r < length and list[largest] < list[r]:
            largest = r

        # If root is not largest, swap with largest and continue heapifying
        if largest != i:
            list[i], list[largest] = list[largest], list[i]
            self.heapify(list, length, largest)

        return list
