#排序对象
class User:
    def __init__(self,user_id):
        self.user_id = user_id
    #重构__repr__方法后，不管直接输出对象还是通过print打印的信息都按我们__repr__方法中定义的格式进行显示了
    #打印对象可视化
    def __repr__(self):
        return 'User({})'.format(self.user_id)

myUser = User(23)
print(myUser.user_id)
users = [User(23),User(3),User(99)]
print(users)
#方法1：
sorted_users = sorted(users,key=lambda u:u.user_id)
print(sorted_users)


#方法2:
from operator import attrgetter
a = sorted(users,key=attrgetter('user_id'))
print(a)
