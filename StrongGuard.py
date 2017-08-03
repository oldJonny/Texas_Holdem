# 从初始化到hand和color分开
# 红桃 H(Heart)  黑桃 S(Spade) 方片 D(Diamond) 梅花 C(Club)
# 数字14 代表 A ，数字13 代表 K...以此类推...2 代表 2
import collections
import pickle
import itertools as it

# 把这样结构的输入raw_hand_5 = (('H', 14), ('S', 11), ('H', 12), ('D', 13), ('H', 10)) 转换成 color = ['H','S','H','D','H']
# 返回输入牌型的花色


def raw_hand_2_color(raw_hand):
    color = [t[0] for t in raw_hand]
    #print(colors)
    return color
# 与上函数同理，返回输入牌型的数字牌面


def raw_hand_2_hand(raw_hand):
    hand = [t[1] for t in raw_hand]
    return hand
# 牌面转化和排序


def card_sort(hand_5):
    # 降序排列
    hand_5.sort(reverse=True)
    # 对straight A 2 3 4 5 特殊处理
    if hand_5 == [14,5,4,3,2]:
        return [5,4,3,2,1]
    else:
        return hand_5


# 声明：以下判断牌面牌力等级均是以五张牌为分析对象
# 判断8种牌力(flush_straight,full_horse,triple_pair,flush,straight,two_pairs,one_pair,high)
# 分析牌面是五张，flush and straight
def flush_straight(hand,color):
    return flush(color) == True and straight(hand) == True


def flush(color):
    return len(set(color)) == 1


def straight(hand):
    return (max(hand) - min(hand)) == 4 and len(set(hand)) == 5


# kind函数能解析full_horse,triple_pair,flush,straight,one_pair,high
def kind(n,hand):
    for i in hand:
        if hand.count(i) == n: return i
    return False
# two_pairs不能直接用kind判定，可以在确实不是triple_pair的情况下，继续使用set函数 len(set(hand)) == 3


def two_pairs(hand):
    return len(set(hand)) == 3


# 返回牌力等级(由高到底依次是8-0)
def rank(raw_hand_5):

    hand = card_sort(raw_hand_2_hand(raw_hand_5))
    color = raw_hand_2_color(raw_hand_5)

    # 从最大的牌型flush_straight...到high的分析，返回牌型等级和牌面
    if flush_straight(hand, color):
        return 8, hand

    elif kind(4, hand):
        return 7, hand

    elif kind(3, hand) and kind(2, hand):
        suit = kind(3, hand)
        pair = kind(2, hand)
        hand = []
        for i in range(0, 3):
            hand.append(suit)
        for j in range(0, 2):
            hand.append(pair)
        return 6, hand

    elif flush(color):
        return 5, hand

    elif straight(hand):
        return 4, hand

    elif kind(3, hand):
        k_3 = kind(3, hand)
        for i in range(0, 3):
            hand.remove(k_3)
        for j in range(0, 3):
            hand.insert(j, k_3)
        return 3, hand

    elif two_pairs(hand):
        high_pair = kind(2, hand)
        hand.reverse()
        low_pair = kind(2, hand)
        set_hand = set(hand)
        set_hand.remove(high_pair)
        set_hand.remove(low_pair)
        hand = []
        list(set_hand)[0]
        for i in range(0, 2):
            hand.append(high_pair)
        for j in range(0, 2):
            hand.append(low_pair)
        hand.append(list(set_hand)[0])
        return 2, hand

    elif kind(2, hand):
        pair = kind(2, hand)
        for i in range(0, 2):
             hand.remove(pair)
        for j in range(0, 2):
            hand.insert(j, pair)
        return 1, hand
    else:
        return 0, hand


# 将已经整理过的手牌（调用rank（）函数）翻译成15进制，牌力按照翻译成15进制后的数值进行比较
def hand_5_to_15base(raw_hand_5):
    # 使用15进制(0-14)
    rank_value = rank(raw_hand_5)[0]
    hand = rank(raw_hand_5)[1]
    t = 14
    v = 0
    j = 4
    for i in hand:
        v = v + i * pow(t,j)
        j = j - 1
    v = v + rank_value*pow(t,5)
    return v
# 计数器，验证逻辑正确性
# print(count)
    # ilist.append(j[0])
# print(len(ilist))
# result = collections.Counter(ilist)


def hand_5_analysis(raw_hand_5):
    v1 = hand_5_to_15base(raw_hand_5)
    pkl_file = open('data.pkl','rb')
    data = pickle.load(pkl_file)
    pkl_file.close()
    v_rank = data.index(v1)
    rate = 1 - v_rank/2598960
    # print(v1)
    print("在全部牌型中处于第%d名" % (v_rank+1))
    print("牌力领先：%.2f%%" % (rate*100))

# 需要分析的是7张时，对7张进行组合，得到21种可能(不重复)
# 对21种可能的15进制值进行计算，其中21个值的最大值对应21种牌型的最大牌型


def raw_hand_7_to_raw_hand_5(raw_hand_7):
    raw_hand_7_all = list(it.combinations(raw_hand_7, 5))
    ilist = []
    for i in raw_hand_7_all:
        ilist.append(hand_5_to_15base(i))
    raw_hand_5 = raw_hand_7_all[ilist.index(max(ilist))]
    return raw_hand_5

# 与7张同理，6张会得到6中组合(不重复)


def raw_hand_6_to_raw_hand_5(raw_hand_6):
    raw_hand_6_all = list(it.combinations(raw_hand_6, 5))
    ilist = []
    for i in raw_hand_6_all:
        ilist.append(hand_5_to_15base(i))
    raw_hand_5 = raw_hand_6_all[ilist.index(max(ilist))]
    return raw_hand_5

# preflop（翻牌前）


def hand_2_to_15base(raw_hand_2):
    hand = [t[1] for t in raw_hand_2]
    hand.sort(reverse=True)
    t = 15
    if set(hand) == 1:
        v = 1*pow(t, 2) + hand[0]*pow(t, 1) + hand[1]*pow(t, 0)
    else:
        v = 0*pow(t,2) + hand[0]*pow(t, 1) + hand[1]*pow(t, 0)
    return v


def hand_2_to_analysis(raw_hand_2):
    v = hand_2_to_15base(raw_hand_2)
    pkl_file = open('data1.pkl','rb')
    data = pickle.load(pkl_file)
    pkl_file.close()
    v_rank = data.index(v)
    rate = 1 - v_rank/1175
    # print(v1)
    print("在全部牌型中处于第%d名"%(v_rank+1))
    print("牌力处于前：%.2f%%" %(rate*100))