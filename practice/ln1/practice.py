# 过滤掉 列表[3,-9,-1,10,20,-2] 中负数
A= [3,-9,-1,10,20,-2] 
def selectPositive(L):
  res = []
  for x in A:
    if x >= 0:
      res.append(x)
      L = res
  return L

a = selectPositive(A)
print(a)


# {'lili':79,'jim':88,'lucy':92,'aqie':60,'bob':'24'} 筛选字典高于60分的
B = {'lili':79,'jim':88,'lucy':92,'aqie':60,'bob':'24'}
def sortPass(D):
  for key, value in D.items():
    if value > 60:
      return D

b = list(sortPass(B))
print(b)

# b = list(filter(sortPass, B))

# {77,89,32,20} 集合中能被3整除的