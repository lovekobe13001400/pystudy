#

def sample():
    n = 0
    def func():
        print('n=',n)

    def get_n():
        return  n

    def set_n(value):
        nonlocal n
        n = value

    func.get_n = get_n

    func.set_n = set_n

    return func

f = sample()

f.set_n(10)

f.get_n()

