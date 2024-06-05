List = [[2,4,6], {"apple":4,"orage":5}, (3,3),["wufate","4"]]
same_count = 0
for x, y in List:	#第一次遍历：x=2，y=4,
    if x == y:
        same_count = same_count + 1
print(same_count)