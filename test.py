
# import win32api,win32con
#
# win32api.MessageBox(0, "这是一个测试消息1111111111111111111111111111111", "消息框标题",win32con.MB_OK)


#coding=utf-8
# import urllib.request
# from mysql.proxy_api import proxy_list
# print(proxy_list())


# for _ in range(N):
#     A.append(int(input().split()))
# print(A)





import sys
import threading

# threading.stack_size(200000000)
# thread = threading.Thread()
# thread.start()

def mysqort(arr, low, high,):
    if low >= high:
        return
    i = low
    j = high
    base = arr[low]
    while(i<j):
        while(i<j and arr[j] > base):
            j -= 1
        if(i<j):
            arr[i] = arr[j]
            i = i + 1
        while(i<j and arr[i] < base):
            i += 1
        if(i<j):
            arr[j] = arr[i]
            j -= 1
    arr[i] = base
    mysqort(arr,low,i-1)
    mysqort(arr,i+1,high)

# def quick_sort(array):
#     def recursive(begin, end):
#
#         if begin > end:
#             return
#         l, r = begin, end
#         pivot = array[l]
#         while l < r:
#             while l < r and array[r] > pivot:
#                 r -= 1
#             while l < r and array[l] <= pivot:
#                 l += 1
#             array[l], array[r] = array[r], array[l]
#         array[l], array[begin] = pivot, array[l]
#         recursive(begin, l - 1)
#         recursive(r + 1, end)
#
#     recursive(0, len(array) - 1)
#     return array
# #创建10000个数
# arr = list(range(10000))
# #数组反转，为了排序的时候递归多一点
# arr.reverse()
# #排序
# new_arr = quick_sort(arr)
# print(new_arr)
# #mysqort(arr,0,9999)
# #堆栈溢出
# print(arr)
# while True:
#     N = int(input())
#     B = list(map(int, input().split()))
#     mysqort(B, 0, N - 1)
#     n = 0
#     while n < N:
#         if n == N-1:
#             print(B[n])
#         else:
#             print(B[n], end=' ')
#         n = n + 1

# while True:
#     data = list(map(int, input().strip().split()))
#     n, array = data[0], data[1:]
#     mysqort(array, 0, n-1)
#     for i in range(n):
#         if i == n - 1:
#             print(array[i])
#         else:
#             print(array[i], end=' ')


# import sys
# sys.setrecursionlimit(1000)
# def factorial(n):
#      if n == 0 or n == 1:
#          return 1
#      else:
#          return(n * factorial(n - 1))
#
# print(factorial(9000))

#把数组变成low mid high,并返回中间位置

# def sort_one(arr,low,high):
#     if(low>=high):
#         return low;
#     i = low
#     j = high
#     base = arr[low]
#     while(i<j):
#         while(i<j and arr[j]>base):
#             j -= 1
#         arr[i] = arr[j]
#
#         while(i<j and arr[i]<base):
#             i += 1
#         arr[j] = arr[i]
#     arr[i] = base
#     return i
#
# def qsort(arr,l,r):
#     if( l >= r):
#         return;
#     #mid = sort_one(arr,low,high)
#     stack = []
#     stack.append(l)
#     stack.append(r)
#     while(stack):
#         r = stack.pop()
#         l = stack.pop()
#         mid = sort_one(arr, l, r)
#         if l<mid-1:
#             stack.append(l)
#             stack.append(mid-1)
#         if r>mid+1:
#             stack.append(mid+1)
#             stack.append(r)
#     return
# arr = list(range(10000))
# #数组反转，为了排序的时候递归多一点
# arr.reverse()
# #qsort(arr,0,99999)
# sys.setrecursionlimit(100000000)
# mysqort(arr,0,9999)
# print(arr)
# def merge_sort(alist):
#     """合并函数"""
#     if len(alist) <= 1:
#         return alist
#     middle = len(alist)//2
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
# arr = list(range(100000))
# #数组反转，为了排序的时候递归多一点
# import random
# l = []
# for x in arr:
#     r = random.randint(0, 99999)
#     l.append(arr[r])
# #qsort(arr,0,99999)
# sys.setrecursionlimit(100000000)
# #print(mysqort(l))
# mysqort(l,0,99999)
# print(l)
import sys
sys.setrecursionlimit(100000000)
def mysort(arr,low,high):
    if(low>=high):
        return
    i = low
    j = high
    while(i<j):
        while(i<j and arr[i]<arr[(low+high)//2]):
            i += 1
        while(i<j and arr[j]>arr[(low+high)//2]):
            j -= 1
        arr[i],arr[j] = arr[j],arr[i]
    mysort(arr,low,i-1)

while True:
    N = int(input())
    B = list(map(int, input().split()))
    B = sorted(B)
    n = 0
    while n < N:
        if n == N-1:
            print(B[n])
        else:
            print(B[n], end=' ')
        n = n + 1