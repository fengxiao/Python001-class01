# 作业二：
# 自定义一个 python 函数，实现 map() 函数的功能

# 内置的map功能
def square(x): # 计算平方数
    return x ** 2

print('-------内置的map功能------')
mlist1 = map(square,[1,2,3,4,5]) # 计算列表各个元素的平方
for a in mlist1:
    print(a)

# 利用python自定义实现的map功能
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

