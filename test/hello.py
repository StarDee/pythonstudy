# !/usr/bin/env python3
# -*- coding: utf-8 -*-

class Hello(object):
    def hello(name='world'):
        print('Hello,%s.'%name)
    hello()
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add']=lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
class MyList(list, metaclass=ListMetaclass):
    pass
# 错误处理
try:
    print('try...')
    r = 100/0
    print('result:',r)
except ZeroDivisionError as e:
    print('except:',e)
finally:
    print('finally...')
print('END')
class Dict(dict):
    def __init__(self,**kw):
        super().__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" %key)
    def __setattr__(self, key, value):
        self[key]=value
