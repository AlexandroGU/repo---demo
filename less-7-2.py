# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.


from random import randint
import operator

rand_list = [randint(0, 50) for i in range(15)]
print('Изначальный список: {0}.'.format(rand_list))


def merge_sort(ex_list, compare=operator.lt):
    if len(ex_list) < 2:
        return ex_list[:]
    else:
        med_ind = len(ex_list) / 2
        med_ind = int(med_ind)
        left = merge_sort(ex_list[:med_ind], compare)
        right = merge_sort(ex_list[med_ind:], compare)
        return merge(left, right, compare)


def merge(left, right, compare):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


rand_list = merge_sort(rand_list)
print('Отсортированный список: {0}.'.format(rand_list))