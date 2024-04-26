N = int(input('請輸入N:'))
#以前用for迴圈寫 今用含是呼叫韓式
def func(n):
  if n==1: return 1 #中指條件 
  return n * func(n-1) #含是呼叫韓式 把大問題改成小問題
ans = func(N)
print(ans)