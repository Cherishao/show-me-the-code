#!/usr/bin/env python
name=raw_input("What is your name?")
raw_inpur("Press <enter>")##使用Enter键
print 'hello,'+name+'!'

#repr(x)可以作为'x'实现
temp=42
print("The temperature is"+temp)
print "The temperature is" + 'temp'
#input会假设用户输入的是合法表达式
name=input("What is your name?")
print "hello,"+name+"!"
#长字符串
print '''This is a very long string
It continues here
And it's not over yet
"hello world!"
still here.'''
