# def merge_sort(alist):
#     """合并函数"""
#     if len(alist) <= 1:
#         return alist
#     #middle = len(alist)//2
#     middle = alist[0]
#     left = merge_sort(alist[:middle])
#     right = merge_sort(alist[middle:])
#     return merge(left, right)
#
# def merge(left, right):
#     """主排序函数"""
#     l, r = 0, 0
#     result = []
#     while l<len(left) and r<len(right):
#         if left[l] < right[r]:
#             result.append(left[l])
#             l += 1
#         else:
#             result.append(right[r])
#             r += 1
#     return result+left[l:]+right[r:]


def mysort(arr,low,high):
    if(low>=high):
        return
    i = low
    j = high
    mid = (low+high)//2
    base = arr[mid]
    while(i<j):
        while(i<j and arr[i]<base):
            i += 1
        while(i<j and arr[j]>base):
            j -= 1
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    mysort(arr,low,i-1)
    mysort(arr,i+1,high)
arr = list(range(100000))
arr.reverse()
mysort(arr,0,99999)
print(arr)

