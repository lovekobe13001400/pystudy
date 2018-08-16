'''
哈希表的定义：

　　哈希存储的基本思想是以关键字Key为自变量，通过一定的函数关系（散列函数或哈希函数），计算出对应的函数值（哈希地址），以这个值作为数据元素的地址，并将数据元素存入到相应地址的存储单元中。

　　查找时再根据要查找的关键字采用同样的函数计算出哈希地址，然后直接到相应的存储单元中去取要找的数据元素即可。
'''
#实现哈希表（线性地址再散列）
def ChangeKey(key,m,di):
    key01 = (key+di)%m
    return key01
def chainHash(InputList):
    res = {}
    for line in InputList:
        if line.split()[0] not in res:
            temp = []
            temp.append(line.split()[1])
            res["%s"%line.split()[0]] = temp
        else:
            res["%s"%line.split()[0].append(line.split()[1])]
    return res

#除法取余法实现的哈希函数
def myHash(data,hashLength,):
    return data % hashLength

#数据插入哈希表
def insertHash(hash={},hashLength=0,data=[]):
    hashAddress = myHash(data,hashLength)
    #如果key存在说明被别人占用，需要解决冲突
    while(hash.get(hashAddress)):
        hashAddress += 1
        hashAddress = myHash(hashAddress,hashLength)
    hash[hashAddress] = data
#哈希表检索数据
def searchHash(hash,hashLength,data):
    hashAddress = myHash(data,hashLength)
    while hash.get(hashAddress) and hash[hashAddress]!=data:
        hashAddress += 1
        hashAddress = hashAddress%hashLength
    if hash.get(hashAddress)==None:
        return None
    return hashAddress

hashLength = 20
L=[13, 29, 27, 28, 26, 30, 38 ]
hash = {}
for i in L:
    insertHash(hash,hashLength,i)
print(hash)
result = searchHash(hash,hashLength,38)
if result:
        print("数据已找到，索引位置在",result)
        print(hash[result])
else:
        print("没有找到数据")
#
# a = input().split()
# m = len(a)
# dic01 = {}
# for i in a:
#     key = int(i)%m
#     if "%s"%key in dic01:
#         NewKey = ChangeKey(key,m,1)
#         while "%s"%NewKey in dic01:
#             NewKey = ChangeKey(NewKey,m,1)
#         dic01["%s"%NewKey] = int(i)
#     else:
#         dic01["%s"%key] = int(i)
# print(dic01)
#
# li = [1,11,2,22,3,4]
# print(chainHash(li))