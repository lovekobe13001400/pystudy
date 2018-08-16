#外部参数作为起始点不动，内部参数作为移动点
def quicksort(a, out_low, out_high):
    print(a)
    print(out_low,out_high)
    if out_low >= out_high:
        return
    in_low  = out_low
    in_high = out_high
    base = a[in_low]
    while in_low<in_high:
        while(in_low<in_high and a[in_high]>=base):
            in_high -= 1
        a[in_low] = a[in_high]
        while(in_low<in_high and a[in_low]<=base):
            in_low += 1
        a[in_high] = a[in_low]
    a[in_low] = base
    quicksort(a,out_low,in_low-1)
    quicksort(a,in_low+1,out_high)

def quicksort2(a,out_low,out_high):
    if(out_low>=out_high):
        return
    in_low = out_low
    in_high = out_high
    base = a[in_low]
    while(out_low<out_high):
        while(out_low<out_high and a[out_high]>=base):
            out_high -= 1
        a[out_low] = a[out_high]
        while(out_low<out_high and a[out_low]<=base):
            out_low += 1
        a[out_high] = a[out_low]
    a[out_low] = base
    quicksort2(a,in_low,out_low-1)
    quicksort2(a,out_low+1,in_high)

def quicksort3(arr,low,high):
    if low>=high:
        return
    i = low
    j = high
    base = arr[i]
    while(i<j):
        while (arr[j] >= base and i < j):
            j = j - 1
        if(i<j):
            arr[i] = arr[j]
            i = i+1
        while(arr[i]<=base and i<j):
            i = i + 1
        if(i<j):
            arr[j] = arr[i]
            j = j-1
    arr[i] = base
    quicksort3(arr,low,i-1)
    quicksort3(arr,i+1,high)

def quicksort4(a,low,high):
    print(low,high)
    print(a)
    if(low>=high):
        return
    i = low
    j = high
    base = a[int((low+high)/2)]
    while i<j:
        while i<j and a[i]<=base:
            i += 1
        while i<j and a[j]>=base:
            j -= 1
        print(i,j)
        if(i<j):
            a[i],a[j] = a[j],a[i]
            i += 1
            j -= 1
        else:
            a[i],a[j+1] = a[j+1],a[i]

    quicksort4(a,low,i-1)
    quicksort4(a,i+1,high)
while True:
    try:
        n = int(input())
        lst = [int(x) for x in input().split()]
        quicksort4(lst, 0, n - 1)
        print(' '.join([str(x) for x in lst]))
    except:
        break