# Use to_int to add two list then revert it back to list

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        def to_int(l):
            return l.val + 10 * to_int(l.next) if l else 0
        def to_list(val):
            l = ListNode(val % 10)
            if val > 9:
                l.next = to_list(val / 10)
            return l
        return to_list(to_int(l1) + to_int(l2))
