"""
문자열 재정렬
알파벳 대문자 + 숫자(0-9) 로만 구성된 문자열이 주어진다.
이 때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에,
모든 숫자를 더한 값을 이어서 출력한다.
Ex. K1KA5CB7 => ABCKK13
"""


def my_func(input: str) -> str:
    ans = []
    num = 0
    for c in input:
        if '0' <= c <= '9':
            num += int(c)
        else:
            ans.append(c)

    ans.sort()
    ans.append(str(num))
    print(''.join(ans))
    return ''.join(ans)


my_func('K1KA5CB7')
