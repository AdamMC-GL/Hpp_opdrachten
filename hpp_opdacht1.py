
def bucket_sort(lst):
    """Een bucket sort algoritme dat een lijst sorteert, hier worden buckets gebruikt waar de meest rechtste waarden van
    een nummer wordt gebruikt om de bepalen welke bucket de waarden in moet, de index van de bucket wordt hiervoor naar gekeken.
    dan wordt elke waarden in volgorde van de buckets terug gezet en zo zijn de eentallen in volgorde, dan wordt gekeken naar
    de meest rechter getal - 1, als die er is. Zo verder tot de gehele lijst is gesorteerd"""
    # measure biggest digit size of list
    n = 0
    for i in lst:
        i = str(abs(i))
        if len(i) > n:
            n = len(i)

    # Bucket sort
    for i in range(1, n+1):  # based on biggest digit size
        bucket_array = [[], [], [], [], [], [], [], [], [], []]
        bucket_array_neg = [[], [], [], [], [], [], [], [], [], []]
        copylst = []  # temp list to hold already sorted values

        for j in lst:
            s = str(abs(j))  # make the value a string
            if len(s) >= i:  # check is current i value matches the length of the string, so that only not sorted value get a true
                if j < 0:
                    bucket_array_neg[int(s[-i])].append(j)  # if the number is negative it goes into the negative bucket array
                else:
                    bucket_array[int(s[-i])].append(j)  # if the number is positive it goes into the positive bucket array
            else:
                copylst.append(j)  # if its false the value has already been sorted and it goes into the copylst

        for k in range(len(bucket_array)):  # add everything from the buckets to the copylst to make the next batch sorted
            copylst += bucket_array[k]
            copylst = bucket_array_neg[k] + copylst

        # put the values of copylst in lst, this way the memory adress will not point at the same space
        lst = list(copylst)

    return lst


def bucket_sort_rec(lst, x=1):
    """Het zelfde als de funcite bucket_sort, maar hier wordt recursie gebruikt."""
    bucket_array = [[], [], [], [], [], [], [], [], [], []]
    bucket_array_neg = [[], [], [], [], [], [], [], [], [], []]
    n = 0
    copylst = []

    # Bucket sort
    for i in lst:
        s = str(abs(i))  # make the value a string
        if len(s) > n:
            n = len(s)
        if len(s) >= x:  # check is current x value matches the length of the string, so that only not sorted value get a true
            if i < 0:
                bucket_array_neg[int(s[-x])].append(i)  # if the number is negative it goes into the negative bucket array
            else:
                bucket_array[int(s[-x])].append(i)  # if the number is positive it goes into the positive bucket array
        else:
            copylst.append(i)  # if its false the value has already been sorted and it goes into the copylst

    for j in range(len(bucket_array)):  # add everything from the buckets to the copylst to make the next batch sorted
        copylst += bucket_array[j]
        copylst = bucket_array_neg[j] + copylst

    # put the values of copylst in lst, this way the memory adress will not point at the same space
    lst = list(copylst)
    if x >= n:
        return lst
    return bucket_sort_rec(lst, x+1)


print(bucket_sort([1, -6, 3, -97, 2, 8, 2, 54, -1212, 76, -232, 23, 0]))
print(bucket_sort_rec([1, -6, 3, -97, 2, 8, 2, 54, -1212, 76, -232, 23, 0]))
