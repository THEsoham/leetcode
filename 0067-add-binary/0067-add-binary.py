class Solution(object):
    def addBinary(self, a, b):

        l1 = []
        l2 = []

        for x in a:
            l1.append(int(x))
        for y in b:
            l2.append(int(y))

        l1 = l1[::-1]
        l2 = l2[::-1]

        carry = 0
        result = []

        n = max(len(l1), len(l2))

        for i in range(n):

            if i < len(l1):
                A = l1[i]
            else:
                A = 0

            if i < len(l2):
                B = l2[i]
            else:
                B = 0

            sum_ = A ^ B ^ carry

            carry = (A & B) | (A & carry) | (B & carry)

            result.append(str(sum_))

        if carry:
            result.append("1")

        return "".join(result[::-1])