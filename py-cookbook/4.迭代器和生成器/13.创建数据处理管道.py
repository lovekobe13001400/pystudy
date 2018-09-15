#

import os
import fnmatch
import gzip
import bz2
import re

def gen_find(filepat,top):
    '''
    Find all filenames in a directory tree that match a shell wildcard pattern
    '''
    for path,dirlist,filelist in os.walk(top):
        for name in fnmatch.filter(filelist,filepat):
            yield os.path.join(path,name)


def gen_opener(filenames):
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename,'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename,'rt')
        else:
            f = open(filename,'rt')
        yield f
        f.close()
#在调用 gen_concatenate() 函数的时候你可能会有些不太明白。 这个函数的目的是将输入序列拼接成一个很长的行序列
def gen_concatenate(iterators):
    for it in iterators:
        yield from it

def gen_grep(pattern,lines):
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line


lognames = gen_find('access-log*', 'www')
files = gen_opener(lognames)
lines = gen_concatenate(files)
pylines = gen_grep('(?i)python', lines)
for line in pylines:
    print(line)