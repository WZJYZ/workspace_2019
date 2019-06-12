
def mergeSort(num, l, r):
    '''

    :param num: 数组
    :param l: 左边
    :param r: 右边
    :return:
    '''
    if l >= r:
        return

    mid = int((l + r)/2)
    mergeSort(num, l, mid)
    mergeSort(num, mid + 1, r)
    merge(num, l, mid, r)

def merge(num, l, mid, r):
    i = l
    j = mid + 1
    k = 0
    tmp = [0] * (r - l + 1)

    while (i <= mid and j <=r):
        if num[i] <= num[j]:
            tmp[k] = num[i]
            k += 1
            i += 1
        else:
           # count += (mid - l + 1)
            tmp[k] = num[j]
            k += 1
            j += 1

    while i <= mid:
        tmp[k] = num[i]
        k += 1
        i += 1
    while j <= r:
        tmp[k] = num[j]
        k += 1
        j += 1

    for i in range(r - l + 1):
        num[i] = tmp[i]


def count(num, n):
    '''

    :param num:
    :param n: 长度
    :return:
    '''
    count = 0
    mergeSort(num, 0, n - 1)
    print(num)

count([1, 5, 6, 2, 3, 4], 6)