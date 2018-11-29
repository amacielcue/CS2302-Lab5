#CS2302 Lab5-B
#By: Alejandra Maciel
#Last Modified: Nov-28-2018
#Instructor: Diego Aguirre
#TA: Manoj  Pravaka  Saha
#The purpose of this lab was to practice the use of heaps and the implementation of heap sort. As well as to challenge
#us, the students, to solve problems with the use of heaps.

#Heap class
class Heap:
    def __init__(self):
        self.heap_array = []

    #Method to insert new numbers to the heap
    def insert(self, k):
        self.heap_array.append(k)

        self.sort_up(len(self.heap_array) - 1)

    #Method to sort new inserts mantaining the properties of the heap by comparing with the node's parent
    def sort_up(self, pos):
        #While the index of the node is bigger than 0
        while pos >= 1:
            #Get parent's index
            parent = (pos-1)//2
            #If the node is smaller than the parent then swap them
            if self.heap_array[pos] < self.heap_array[parent] :
                temp = self.heap_array[pos]
                self.heap_array[pos] = self.heap_array[parent]
                self.heap_array[parent] = temp
                pos = parent
            return
    #Method to sort new inserts mantaining the properties of the heap by comparing with the node's child
    def sort_down(self, pos):
        #Get child's index
        child = (pos * 2) + 1
        #While the child's index is smaller than the length of the heap array
        while child < len(self.heap_array):
            #Set the max values to the node and the max index to -1
            max_val = self.heap_array[pos]
            max_ind = -1
            i = 0
            #While i is less than 2 and i plus the child's index is bigger than the max value
            while i < 2 and i + child < len(self.heap_array):
                #If the node at the child's plus i index is greater than the max value
                if self.heap_array[i + child] > max_val:
                    #Set the max value to the node and tha max index to said index
                    max_val = self.heap_array[i + child]
                    max_ind = i + child
                i += 1
            #If the max values is the same as the node at the original index then return
            if max_val == self.heap_array[pos]:
                return
            #Else swap the node and the node at the max index
            temp = self.heap_array[pos]
            self.heap_array[pos] = self.heap_array[max_ind]
            self.heap_array[max_ind] = temp

            pos = max_ind
            child = (pos * 2) + 1


    #Method to extract the node with the minimum value (usually at the root)
    def extract_min(self):
        if self.is_empty():
            return None

        min_elem = self.heap_array[0]

        #Temp variable to save the last value
        temp = self.heap_array.pop()
        #If the length of the heap array is bigger than 0 then set the root to the last value and sort down the heap
        if len(self.heap_array) > 0:
            self.heap_array[0] = temp
            self.sort_down(0)
        return min_elem

    #Method to know if the heap is empty
    def is_empty(self):
        return len(self.heap_array) == 0

#Method to sort the heap completely
def heap_sort(list):
    heap = Heap()
    result = []
    #Insert each element on the given list to a heap
    for elem in list:
        heap.insert(elem)

    #While said heap is not empty, append the extracted minimum value
    while not heap.is_empty():
        result.append(heap.extract_min())

    #Return the resulted list
    return result

#Method to read the test file
def read_file(file_name):
    f = open(file_name)
    file = f.read().splitlines()
    list = []

    #Loop to split all the lines in the files and the numbers in each line and append each number to the list
    for i in range(len(file)):
        line = file[i].split(",")
        for j in range(len(line)):
            list.append(line[j])

    return list

#Main Method: Call the read file method and heap sort method, as well as print the elements in the sorted list.
def main():
    list = read_file("info")
    sorted = heap_sort(list)

    for i in range(len(sorted)):
        print(sorted[i])

main()