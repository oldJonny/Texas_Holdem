from unittest import TestCase
import StrongGuard
import main

class TestAll(TestCase):

    def testStrongGuard(self):
        s = StrongGuard
        raw_hand_5 = (('H', 14), ('H', 11), ('H', 12), ('H', 13), ('H', 10))
        hand = [14, 13, 12, 11, 10]

        self.assertEqual(['H', 'H', 'H', 'H', 'H'], s.raw_hand_2_color(raw_hand_5))

        self.assertEqual([14, 11, 12, 13, 10], s.raw_hand_2_hand(raw_hand_5))

        self.assertEqual([5, 4, 3, 2, 1], s.card_sort([14, 2, 5, 4, 3]))

        self.assertEqual((8, hand), s.rank(raw_hand_5))

        self.assertEqual((8, [14, 13, 12, 11, 10]), s.rank((('S', 14), ('S', 12), ('S', 10), ('S', 11), ('S', 13))))

        self.assertEqual((7, [14, 14, 14, 14, 10]),s.rank((('S', 14), ('H', 14), ('D', 14), ('C', 14), ('H', 10))))

        self.assertEqual((6, [14, 14, 14, 10, 10]),s.rank((('S', 10), ('H', 14), ('D', 14), ('C', 14), ('H', 10))))

        self.assertEqual((5, [14, 8, 6, 5, 3]), s.rank((('D', 14), ('D', 8), ('D', 6), ('D', 3), ('D', 5))))

        self.assertEqual((4, [5, 4, 3 ,2, 1]), s.rank((('S', 14), ('H', 3), ('D', 2), ('C', 5), ('H', 4))))

        self.assertEqual((3, [14, 14, 14, 10, 2]), s.rank((('S', 14), ('H', 14), ('C', 2), ('H', 10), ('D', 14))))

        self.assertEqual((2, [14, 14, 8, 8, 10]), s.rank((('S', 14), ('H', 14), ('D', 8), ('C', 10), ('H', 8))))

        self.assertEqual((1, [14, 14, 8, 5, 2]), s.rank((('S', 14), ('H', 2), ('D', 8), ('C', 14), ('H', 5))))

        self.assertEqual((0, [13, 10, 9, 4, 2]), s.rank((('S', 13), ('H', 2), ('D', 4), ('C', 9), ('H', 10))))

        self.assertEqual((('H', 14), ('H', 12), ('H', 13), ('D', 2), ('S', 2)),s.raw_hand_7_to_raw_hand_5((('H', 14), ('H', 11), ('H', 12), ('H', 13), ('D', 2),('D',5),('S',2))))

        self.assertEqual((('H', 14), ('H', 11), ('H', 12), ('H', 13), ('D',5)),s.raw_hand_6_to_raw_hand_5((('H', 14), ('H', 11), ('H', 12), ('H', 13), ('D', 2),('D',5))))


