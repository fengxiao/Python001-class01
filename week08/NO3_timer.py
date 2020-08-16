# 作业三：
# 实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。
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

