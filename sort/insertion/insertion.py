
if __name__ == '__main__':

    numbers = [5, 2, 4, 6, 1, 3]
    print("Unsorted values: {}".format(numbers))

    for j in range(1, len(numbers)):
        key = numbers[j]
        i = j - 1
        while i > -1 and numbers[i] > key:
            numbers[i+1] = numbers[i]
            i = i - 1
        numbers[i+1] = key

    print("Sorted values: {}".format(numbers))
