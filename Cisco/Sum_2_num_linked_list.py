#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


#
# Complete the 'getSum' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST num1
#  2. INTEGER_SINGLY_LINKED_LIST num2
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def convert_to_num(temp):
    """ Function to convert the linked list to number """
    num = 0
    place_holder = 1
    while temp:
        num = num + (place_holder * temp.data)
        place_holder = place_holder * 10
        temp = temp.next
    return num

def getSum(num1, num2):
    # Write your code here
    number1 = convert_to_num(num1)
    number2 = convert_to_num(num2)
    sum = number1 + number2
    
    reverse_sum = str(sum)[::-1]
    head = None
    prev = None
    flag = True
    for i in reverse_sum:
        temp = SinglyLinkedListNode(i)
        if flag:
            # First node is created, hence preserve this as HEAD node
            head = temp
            prev = temp
            flag = False
        else:
            # Subsequent nodes, so mark the prev node to point temp as next node
            prev.next = temp
            prev = temp
    
    return head
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num1_count = int(input().strip())

    num1 = SinglyLinkedList()

    for _ in range(num1_count):
        num1_item = int(input().strip())
        num1.insert_node(num1_item)

    num2_count = int(input().strip())

    num2 = SinglyLinkedList()

    for _ in range(num2_count):
        num2_item = int(input().strip())
        num2.insert_node(num2_item)

    result = getSum(num1.head, num2.head)

    print_singly_linked_list(result, '\n', fptr)
    fptr.write('\n')

    fptr.close()
