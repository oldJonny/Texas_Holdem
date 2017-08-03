from  itertools import permutations
num = [8,9,10,5]
op = ['+','-','*','/','b-','b/']
opt = ('+', '-', '*')
print(opt[0])
num_all = list(permutations(num))
op_all = list(permutations(op,3))
print(num_all)
print(op_all)
all = []
for num in num_all:
    num = list(num)
    for op in op_all:
        num.insert(1,op[0])
        num.insert(3,op[1])
        num.insert(5,op[2])
        all.append(num)
        print(num)
        num.remove(op[0])
        num.remove(op[1])
        num.remove(op[2])
        # num[1:1] = op[0]
        # num[3:3] = op[1]
        # num[5:5] = op[2]

#         # for i in range(1,6,2):
#         #     num[i:i] = op[0]
#         #     # count += 1