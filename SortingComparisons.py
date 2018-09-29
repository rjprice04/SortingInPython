import random


def selection_sort(list1):
    comparisons = 0
    for num in range(len(list1)):
        min_index = num
        for j in range(num+1,len(list1)):
            # comparisons += 1
            if list1[min_index] > list1[j]:
                # comparisons += 1
                min_index = j

        list1[num], list1[min_index] = list1[min_index], list1[num]

    return list1
    # print(comparisons)


def insertion_sort(list2):

    comparisons = 0
    c2 = 0
    for num2 in range(1, len(list2)):
        key_value = list2[num2]
        j = num2 - 1
        comparisons += 1
        while j > -1 and key_value < list2[j]:
            list2[j+1] = list2[j]
            j -= 1
            c2 += 1
        list2[j+1] = key_value

    return list2


def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    else:
        midpoint = int(len(input_list)/2)
        left_sublist = merge_sort(input_list[:midpoint])
        right_sublist = merge_sort(input_list[midpoint:])
    return merge_lists(left_sublist,right_sublist)

def merge_lists(left_sublist,right_sublist):
    i,j = 0,0
    result = []
    # iterate through both left and right sublist
    while i<len(left_sublist) and j<len(right_sublist):
        # if left value is lower than right then append it to the result
        if left_sublist[i] <= right_sublist[j]:
            result.append(left_sublist[i])
            i += 1
        else:
            # if right value is lower than left then append it to the result
            result.append(right_sublist[j])
            j += 1
    # concatenate the rest of the left and right sublists
    result += left_sublist[i:]
    result += right_sublist[j:]
    # return the result
    return result


def quick_sort(list4):
    if len(list4) <= 1:
        return list4
    else:
        pivot = list4[0]
        i = 0
        for j in range(len(list4)-1):
            if list4[j+1] < pivot:
                list4[j+1],list4[i+1] = list4[i+1], list4[j+1]
                i += 1
        list4[0],list4[i] = list4[i],list4[0]
        first_part = quick_sort(list4[:i])
        second_part = quick_sort(list4[i+1:])
        first_part.append(list4[i])
        return first_part + second_part


# n = 50
# a = []
# i = 0
# for i in range(n):
#     a.append(random.randrange(1, n+1))
#
# print(len(a))
# print(selection_sort(a))
# print(insertion_sort(a))
# print(merge_sort(a))
# print(quick_sort(a))

n = 100
a = []
i = 0
for i in range(n):
    a.append(random.randrange(1, n+1))

print(len(a))
print(selection_sort(a))
print(insertion_sort(a))
print(merge_sort(a))
print(quick_sort(a))

# n = 1000
# a = []
# i = 0
# for i in range(n):
#     a.append(random.randrange(1, n+1))
#
# print(len(a))
# print(selection_sort(a))
# print(insertion_sort(a))
# print(merge_sort(a))
# print(quick_sort(a))

# n = 10000
# a = []
# i = 0
# for i in range(n):
#     a.append(random.randrange(1, n+1))
#
# print(len(a))
# print(selection_sort(a))
# print(insertion_sort(a))
# print(merge_sort(a))
# print(quick_sort(a))
