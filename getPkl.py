import pickle
import itertools as it
from StrongGuard import hand_5_to_15base
from StrongGuard import hand_2_to_15base
num_all = [i for i in range(2,15)]
color = ['H','S','D','C']
poker = list(it.product(color,num_all))
poker_all = list(it.combinations(poker,5))
# afterflop，把5张牌对应的260种牌型所一一对应的15进制值存入本地并保存成data.pkl文件
# data.pkl在StrongGurad.hand_5_to_analysis被读取调用
raw_hand_5 = (('H', 2), ('H', 3), ('H', 4), ('H', 5), ('H', 9))
m = 0
v1 = hand_5_to_15base(raw_hand_5)

data = [hand_5_to_15base(raw_hand_5) for raw_hand_5 in poker_all]
data.sort(reverse=True)

output = open('data.pkl', 'wb')
pickle.dump(data,output)
output.close()


# preflop，把2张牌对应的1326种牌型一一对应的15进制值写入本地并保存到data1.pkl中
# data1.pkl在StrongGurad.hand_2_to_analysis被读取调用
poker_2_all = list(it.combinations(poker,2))
data1 = [hand_2_to_15base(raw_hand_2) for raw_hand_2 in poker_2_all]
data1.sort(reverse=True)

output1 = open('data1.pkl', 'wb')
pickle.dump(data1,output1)
output1.close()
