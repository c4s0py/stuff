def count_negatives_1(numbers):
    sorted_tuple = ()
    sum = 0
    for i in numbers:
        if i < 0:
            sorted_tuple = sorted_tuple + (i,)
    for y in sorted_tuple:
        sum += y
    return len(sorted_tuple), sum / len(sorted_tuple)
print(count_negatives_1([-2,4,-3,1]))
