import json

data = {
    'name':'jack',
    'age':10
}
#转json

json_str = json.dumps(data)

print(json_str)

#json转python数据结构

data = json.loads(json_str)


#
j_list = [1,2,3,4]
print(json.dumps(j_list))


#json处理文本

with open('data.json','w') as f:
    #dump：将一个对象序列化存入文件
    json.dump(data,f)

with open('data.json','r') as f:
    #：从一个打开的文件句柄加载数据
    data = json.load(f)
    print('---------------')
    print(data)