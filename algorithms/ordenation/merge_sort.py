#!/usr/bin/python
class MergeSort():

    def sort(self,list):
        length = len(list)

        if length > 1:
            middle = length // 2
            left = list[:middle]
            right = list[middle:]
            left = self.sort(left)
            right = self.sort(right)

            list = self.merge_sort(left, right)

        return list

    def merge_sort(self, left, right):
        list = []

        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                list.append(left[0])
                left.pop(0)
            else:
                list.append(right[0])
                right.pop(0)

        for i in left:
            list.append(i)
        for i in right:
            list.append(i)

        return list
