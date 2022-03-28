class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_list = [*a]
        b_list = [*b]
        a_num = a_list.pop(-1) if len(a_list) > 0 else None
        b_num = b_list.pop(-1) if len(b_list) > 0 else None
        carry = 0
        ans = []
        while a_num and b_num:
            temp = int(a_num) + int(b_num) + carry
            ans.append(str(temp % 2))
            carry = temp // 2
            a_num = a_list.pop(-1) if len(a_list) > 0 else None
            b_num = b_list.pop(-1) if len(b_list) > 0 else None

        while a_num:
            temp = int(a_num) + carry
            ans.append(str(temp % 2))
            carry = temp // 2
            a_num = a_list.pop(-1) if len(a_list) > 0 else None

        while b_num:
            temp = int(b_num) + carry
            ans.append(str(temp % 2))
            carry = temp // 2
            b_num = b_list.pop(-1) if len(b_list) > 0 else None

        if carry == 1:
            ans.append(str(carry))

        return ''.join(ans[::-1])

    def addBinary2(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

if __name__ == '__main__':
    print(Solution().addBinary2("11", "1"))

