学习笔记

作业一： 区分以下类型哪些是容器序列哪些是扁平序列，哪些是可变序列哪些是不可变序列： 

```
# 答：
# （1_1）扁平序列---存放的是相同类型的数据，只能容纳一种类型,包括：str;
# （1_2）容器序列---能存放不同类型的数据容器序列，可存放不同类型的数据，包括：ist、 tuple、dict、collections. deque;
# （2_1）可变序列---包括：list、dict、collections.deque;
# （2_2）不可变序列---包括：str、tuple;
```



作业二： 自定义一个 python 函数，实现 map() 函数的功能。 

```
# 内置的map功能
def square(x): # 计算平方数    
	return x ** 2

print('-------内置的map功能------')
mlist1 = map(square,[1,2,3,4,5]) # 计算列表各个元素的平方
for a in mlist1:    
	print(a)# 利用python自定义实现的map功能

def mymap(func,plist):    
	mretrun_list =[]    
	for m in plist:        
		m_result = func(m)        
		mretrun_list.append(m_result)    
	return mretrun_list

print('-------利用python自定义实现的map功能------')
mlist2 = mymap(square,[1,2,3,4,5])
for b in mlist2:    
	print(b)
```

![1597554496773](C:\Users\ewha\AppData\Roaming\Typora\typora-user-images\1597554496773.png)



作业三： 实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。 

```python
# 作业三：# 实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。
import datetime
import time

def timer(func):
    def inner(*args,**kwargs):
        time_start =datetime.datetime.now()
        ret = func(*args,**kwargs)
        time_end = datetime.datetime.now()
        time_cost = time_end - time_start
        print(f'{func.__name__}() 函数运行耗时：{time_cost}')
        return ret
    return inner

@timer
def student_setinfo(*args,**kwargs):
    time.sleep(2)
    print(f"我是{kwargs['name']},今年{kwargs['age']}岁，就读于{args[0]}{args[1]}！")

@timer
def teacher_setinfo(*args,**kwargs):
    time.sleep(2)
    print(f"我是{kwargs['name']},是{args[0]}{args[1]}{args[2]}！")

print("------------开始录入学生信息------------")
student_setinfo('深圳中学','三年一班',age=15,name='冯小明')

print("------------开始录入教师信息------------")
teacher_setinfo('深圳中学','三年一班','班主任',name='冯大明')
```



![1597554448211](C:\Users\ewha\AppData\Roaming\Typora\typora-user-images\1597554448211.png)