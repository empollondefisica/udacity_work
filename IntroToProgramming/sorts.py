
def get_nums():
    return [6, 1, 4, 3, 8, 7, 5, 9, 0, 2]

def get_chars():
    return ['g', 'b', 'e', 'd', 'i', 'h', 'f', 'j', 'a', 'c']


def swap(items, first_i, second_i):
    items[first_i], items[second_i] = items[second_i], items[first_i]

# Bubble Sort ---------------------------------------------------------

def bubble_sort(items):
    i = len(items) - 1
    while i >= 0:
        j = 1
        while j <= i:
            if items[j - 1] > items[j]:
                swap(items, j, j - 1)
            j = j + 1
        i = i - 1

print "\n-- Bubble Sort"
data = get_nums()
bubble_sort(data)
print data
data = get_chars()
bubble_sort(data)
print data

# Selection Sort ------------------------------------------------------

def selection_sort(items):
    i = 0
    while i < len(items) - 1:
        smallest = i
        j = i + 1
        while j < len(items):
            if items[j] < items[smallest]:
                smallest = j
            j = j + 1
        swap(items, i, smallest)
        i = i + 1

print "\n-- Selection Sort"
data = get_nums()
selection_sort(data)
print data
data = get_chars()
selection_sort(data)
print data

# Insertion Sort ------------------------------------------------------

def insertion_sort(items):
    i = 0
    while i < len(items):
        index = items[i]
        j = i
        while j > 0 and items[j - 1] > index:
            items[j] = items[j - 1]
            j = j - 1
        items[j] = index
        i = i + 1

print "\n-- Insertion Sort"
data = get_nums()
insertion_sort(data)
print data
data = get_chars()
insertion_sort(data)
print data

# Merge Sort -----------------------------------------------------------

def merge(items, tmp, left, right, right_end):
    left_end = right - 1
    k = left
    num = right_end + 1

    while left <= left_end and right <= right_end:
        if items[left] <= items[right]:
            tmp[k] = items[left]
            k = k + 1
            left = left + 1
        else:
            tmp[k] = items[right]
            k = k + 1
            right = right + 1

    while left <= left_end:
        tmp[k] = items[left]
        k = k + 1
        left = left + 1

    while right <= right_end:
        tmp[k] = items[right]
        k = k + 1
        right = right + 1

    for i in range(0, num):
        items[right_end] = tmp[right_end]
        right_end = right_end - 1

def merge_sort_2(items, tmp, left, right):
    if left < right:
        center = (left + right) / 2
        merge_sort_2(items, tmp, left, center)
        merge_sort_2(items, tmp, center + 1, right)
        merge(items, tmp, left, center + 1, right)

def merge_sort(items):
    tmp = items[:]
    merge_sort_2(items, tmp, 0, len(items) - 1)

print "\n-- Merge Sort"
data = get_nums()
merge_sort(data)
print data
data = get_chars()
merge_sort(data)
print data

# Quick Sort -----------------------------------------------------------

import random

def partition(items, low, high):
    pivot = items[high]
    i = low
    for j in range(low, high):
        if items[j] <= pivot:
            swap(items, i, j)
            i = i + 1
    swap(items, i, high)
    return i

def quick_sort_2(items, low, high):
    if low < high:
        p = partition(items, low, high)
        quick_sort_2(items, low, p - 1)
        quick_sort_2(items, p + 1, high)

def quick_sort(items):
    quick_sort_2(items, 0, len(items) - 1)

print "\n-- Quick Sort"
data = get_nums()
quick_sort(data)
print data
data = get_chars()
quick_sort(data)
print data

