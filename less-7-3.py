# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда,
# делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой — не больше медианы. Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки,
# который не рассматривался на уроках (сортировка слиянием также недопустима).

from random import randint
import operator

m_letter = int(input('Введите m для (2m + 1) для длины массива: '))
list_length = 2 * m_letter + 1
rand_list = [randint(0, 50) for i in range(list_length)]
print('Изначальный список: {0}'.format(rand_list))


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


def median_find(ex_list):
    med_num_index = int((len(ex_list) / 2))
    med_num = ex_list[med_num_index]
    return med_num


rand_list = merge_sort(rand_list)
print('Отсортированный список: {0}.'.format(rand_list))
print('Медиана в списке: {0}.'.format(median_find(rand_list)))