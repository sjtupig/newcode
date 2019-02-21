'''
1，两个数组
2，将其中一个数组进行排列
3，比较两个数组每个值的位置，不一样加1'''
'''
2 4 1 3 7 9 -> 1 2 3 4 7 9难道不是只需要移动两次就行了吗
--更新
重新理解题意--当一个元素不在它原来所在的位置,这个元素就是被移动了的，也就是在数组中的下标位置变了就移动了，而不是看相对位置
'''


n = eval(input())
a = list(map(int,input().split()))
b = sorted(a)
count = 0 
for i in range(n):  
    if a[i] != b[i]:
        count += 1 
print(count)

#####################################################################################################
n = int('37'.strip())
nums = list(map(int, '91 37 37 37 37 91 91 29 37 91 37 29 29 37 91 29 91 37 37 29 37 91 91 91 29 29 37 37 37 91 29 37 37 91 29 91 29'.strip().split(' ')))
#等价于找到最长升序序列（非连续的，把剩下的数插进去就可以了）
#结果=数组长度-最长升序 序列的长度
up_len = [1]*n 
for i in range(n):
    for j in range(i):
        if nums[j] <= nums[i]:
            up_len[i] = max(up_len[i], up_len[j]+1) 
print(up_len)
print(n-max(up_len))



n = eval('37')
a = list(map(int,'91 37 37 37 37 91 91 29 37 91 37 29 29 37 91 29 91 37 37 29 37 91 91 91 29 29 37 37 37 91 29 37 37 91 29 91 29'.split()))
b = sorted(a)
count = 0 
for i in range(n):  
    if a[i] != b[i]:
        count += 1 
print(count)
