import pickle

data = 'aaa'

f = open('../dead.txt','wb')

s = pickle.dump(data,f)
print(s)

f = open('../dead.txt','rb')

data = pickle.load(f)
print(data)

data = pickle.loads(s)
print(data)