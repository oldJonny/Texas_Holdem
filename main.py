import StrongGuard  as sg

if __name__=="__main__":
    raw_hand = eval(input("input here: "))
    # 输入说明：接受的输入在格式上有四种情况 2、5、6、7张牌，我直接把他们整合到了一起，按照以下四种对应的格式输入即可
    # eg：执行main()后，在input处 输入 (('H', 14), ('H', 11)) 即可分析出2张牌的结果
    # 同理 输入  (('H', 14), ('H', 11), ('H', 12), ('H', 13), ('D', 2),('D',5),('H',9))代表2张手牌+5张公共牌
    # 输入格式示例
    # 对手牌的判断，也就是raw_hand = (('H', 14), ('H', 11))
    if len(raw_hand) ==2:
        sg.hand_2_to_analysis(raw_hand)
    # raw_hand_5 = (('H', 14), ('H', 11), ('H', 12), ('H', 13), ('S', 10))
    elif len(raw_hand) == 5:
        sg.hand_5_analysis(raw_hand)
    # raw_hand_6 = (('H', 14), ('H', 11), ('H', 12), ('H', 13), ('D', 2),('D',5))
    elif len(raw_hand) == 6:
        raw_hand_5 = sg.raw_hand_6_to_raw_hand_5(raw_hand)
        sg.hand_5_analysis(raw_hand_5)
    # raw_hand_7 = (('H', 14), ('H', 11), ('H', 12), ('H', 13), ('D', 2),('D',5),('D',2))
    else:
        raw_hand_5 = sg.raw_hand_7_to_raw_hand_5(raw_hand)
        sg.hand_5_analysis(raw_hand_5)