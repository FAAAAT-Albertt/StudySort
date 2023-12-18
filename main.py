from typing import *
import time
from random import randint
import math

# сортировка пузырьком
def sort_bubble() -> NoReturn:
    """algo bubble sort"""
    n = 7
    mas = [1, 4, 2, 5, 8, 9, 7]
    # ввод в одну строку
    # mas = list(map(int, input().split()))
    count_iter = 0
    for i in reversed(range(n+1)):
        for j in range(len(mas[0:i])-1):
            if mas[j] > mas[j+1]:
                mas[j], mas[j+1] = mas[j+1], mas[j]

# слияние списков + метод сортировки двумя указателями
def sort_merge(a: list[int], b: list[int]) -> list[int]:
    """sort two branch"""
    start = time.monotonic()
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    c += a[i:] + b[j:]
    end = time.monotonic() - start
    return c, end

def merge_two_lists(var: list[int]) -> sort_merge:
    """recursion of two lists"""
    middle = len(var) // 2
    left = var[:middle]
    right = var[middle:]
    if len(left) > 1:
        left = merge_two_lists(left)
    if len(right) > 1:
        right = merge_two_lists(right)

    return sort_merge(left, right)[0]

# быстрая сортировка
def quick_sort(mas: list[int]) -> list[int]:
    """algo quick sort"""
    n = len(mas)
    supp_elem = randint(0, n-1)
    if n <= 1:
        return mas

    less_vars = list(filter(lambda x: x < mas[supp_elem], mas))
    quals_vars = list(filter(lambda x: x == mas[supp_elem], mas))
    more_vars = list(filter(lambda x: x > mas[supp_elem], mas))
    return quick_sort(less_vars) + quals_vars + quick_sort(more_vars)

print(quick_sort([1, 3, 2, 8, 1, 4, 10, -1]))

# сортировка выбором
def selection_sort(mas: list[int]) -> list[int]:
    """algo selection sort"""
    for i in range(len(mas)-1):
        if mas[i] > mas[i+1]:
            mas[i], mas[i+1] = mas[i+1], mas[i]

    return mas

# сортировка вставками
def insertion_sort(mas: list[int]) -> list[int]:
    """algo insertion sort"""
    start = time.monotonic()
    for i in range(1, len(mas)):
        for j in range(i, 0, -1):
            if mas[j] < mas[j-1]:
                mas[j], mas[j-1] = mas[j-1], mas[j]
            else:
                break

    end = time.monotonic() - start

# сортировка подсчетом
def method_counter(mas: list[int]) -> list[int]:
    """algo for count vars"""
    how_vars = [0, 0, 0, 0, 0, 0]
    for i in mas:
        how_vars[i] += 1

    return how_vars
