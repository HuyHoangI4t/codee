n = int(input())
def giai_thua (n):
  if n== 0:
    return 1
  else :
    return n * giai_thua(n-1)

print(giai_thua(n))
print 