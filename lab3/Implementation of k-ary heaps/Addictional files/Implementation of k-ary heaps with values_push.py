# Implementation of k-ary heaps with values


import math

# 2-ary heap ------------------------------------------------------------------------------------------
class Heap2:
    def __init__(self):
        self.Heap = []

    def push(self, value):
        self.Heap.append(value)
        self._restore_properties()

    def _restore_properties(self):
        index = len(self.Heap) - 1
        while index > 0:
            parent = (index - 1) // 2
            if self.Heap[index] > self.Heap[parent]:
                self.Heap[index], self.Heap[parent] = self.Heap[parent], self.Heap[index]
                index = parent
            else:
                break

    def delete(self):
        if not self.Heap:
            return None
        if len(self.Heap) == 1:
            return self.Heap.pop()
        root = self.Heap[0]
        self.Heap[0] = self.Heap.pop()
        self._correct_Heap(0)
        return root

    def _correct_Heap(self, index):
        max_index = len(self.Heap)
        largest = index
        for i in range(1, 2+1): 
            child = 2*index + i
            if child < max_index and self.Heap[child] > self.Heap[largest]:
                largest = child
        if largest != index:
            self.Heap[index], self.Heap[largest] = self.Heap[largest], self.Heap[index]
            self._correct_Heap(largest)

    def print_pyramid(self):
        data = self.Heap
        children = 2
        levels = []
        max_len = max(len(str(x)) for x in data) + 2
        start_index = 0
        level_num = 0
        while start_index < len(data):
            num_elements = children**level_num
            level = data[start_index : start_index + num_elements]
            if not level:
                break
            levels.append(level)
            start_index += num_elements
            level_num += 1
        
        pyramid_width = 80

        for level in levels:
            line =""
            for x in level:
                line += str(x).center(max_len)

            print(line.center(pyramid_width))



# 5-ary heap--------------------------------------------------------------------------------------------------------
class Heap5:
    def __init__(self):
        self.Heap = []

    def push(self, value):
        self.Heap.append(value)
        self._restore_properties()

    def _restore_properties(self):
        index = len(self.Heap) - 1
        while index > 0:
            parent = (index - 1) // 5
            if self.Heap[index] > self.Heap[parent]:
                self.Heap[index], self.Heap[parent] = self.Heap[parent], self.Heap[index]
                index = parent
            else:
                break

    def delete(self):
        if not self.Heap:
            return None
        if len(self.Heap) == 1:
            return self.Heap.pop()
        root = self.Heap[0]
        self.Heap[0] = self.Heap.pop()
        self._correct_Heap(0)
        return root

    def _correct_Heap(self, index):
        max_index = len(self.Heap)
        largest = index
        for i in range(1, 5+1):
            child = 5*index + i
            if child < max_index and self.Heap[child] > self.Heap[largest]:
                largest = child
        if largest != index:
            self.Heap[index], self.Heap[largest] = self.Heap[largest], self.Heap[index]
            self._correct_Heap(largest)

    def print_pyramid(self):
        data = self.Heap
        children = 5
        levels = []
        max_len = max(len(str(x)) for x in data) + 2
        start_index = 0
        level_num = 0

        while start_index < len(data):
            num_elements = children**level_num
            level = data[start_index : start_index + num_elements]
            if not level:
                break
            levels.append(level)
            start_index += num_elements
            level_num += 1

        num_levels = len(levels)

        for i, level in enumerate(levels):
            line = ""
            for x in level:
                line += str(x).center(max_len)

        pyramid_width = 100

        for i, level in enumerate(levels):
            line =""
            for x in level:
                line += str(x).center(max_len)

            left_padding = " " * ((len(levels) - i - 1) * 2)
            print(left_padding + line.center(pyramid_width))


# 7-ary heap ---------------------------------------------------------------------------------
class Heap7:
    def __init__(self):
        self.Heap = []
        self.children = 7

    def push(self, value):
        self.Heap.append(value)
        self._restore_properties()

    def _restore_properties(self):
        index = len(self.Heap) - 1
        while index > 0:
            parent = (index - 1) // 7
            if self.Heap[index] > self.Heap[parent]:
                self.Heap[index], self.Heap[parent] = self.Heap[parent], self.Heap[index]
                index = parent
            else:
                break

    def delete(self):
        if not self.Heap:
            return None
        if len(self.Heap) == 1:
            return self.Heap.pop()
        root = self.Heap[0]
        self.Heap[0] = self.Heap.pop()
        self._correct_Heap(0)
        return root

    def _correct_Heap(self, index):
        max_index = len(self.Heap)
        largest = index
        for i in range(1, 7+1):
            child = 7*index + i
            if child < max_index and self.Heap[child] > self.Heap[largest]:
                largest = child
        if largest != index:
            self.Heap[index], self.Heap[largest] = self.Heap[largest], self.Heap[index]
            self._correct_Heap(largest)

    def print_pyramid(self):
        data = self.Heap
        children = 7
        levels = []
        max_len = max(len(str(x)) for x in data) + 2
        start_index = 0
        level_num = 0

        while start_index < len(data):
            num_elements = children**level_num
            level = data[start_index : start_index + num_elements]
            if not level:
                break
            levels.append(level)
            start_index += num_elements
            level_num += 1

        num_levels = len(levels)

        pyramid_width = 120

        for i, level in enumerate(levels):
            line =""
            for x in level:
                line += str(x).center(max_len)

            left_padding = " " * ((num_levels - i - 1) * (max_len // 2))
            print(left_padding + line.center(pyramid_width))
            

#----------------------------------------------------------------------------------

example_values = [20, 15, 10, 5, 12, 7]
example_values1= [55, 74, 66, 18, 28, 85, 56, 34, 64, 83, 25, 79, 80, 63, 84, 70, 69, 2, 23, 77, 89]
example_values2= [11, 59, 45, 15, 8, 67, 100, 53, 97, 16, 50, 87, 61, 33, 30, 37, 69, 2, 23, 77, 89, 86, 29]

if __name__ == "__main__":
    heap2 = Heap2()
    print("2-ary heap:")
    for val in example_values:
        heap2.push(val)
        print("2-ary heap: next element", val)
        heap2.print_pyramid()


    heap5 = Heap5()
    print("5-ary heap:")
    for val in example_values1:
        heap5.push(val)
        print("5-ary heap: next element", val)
        heap5.print_pyramid()
    

    heap7 = Heap7()
    print("7-ary heap:")
    for val in example_values2:
        heap7.push(val) 
        print("7-ary heap: next element",  val)
        heap7.print_pyramid()
   




