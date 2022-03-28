#!/bin/python3

def encrypt(c: str, k: int) -> str:
    n_alphabet = ord('z') - ord('a') + 1
    new_k = k % 26
    if c.isupper():
        shifted = ord(c) + new_k
        return chr(shifted) if shifted <= ord('Z') else chr(shifted - n_alphabet)
    elif c.islower():
        shifted = ord(c) + new_k
        return chr(shifted) if shifted <= ord('z') else chr(shifted - n_alphabet)
    else:
        return c

def caesarCipher(s, k):
    answer = ""
    for i in range(0, len(s)):
        answer += encrypt(s[i], k)
    return answer


if __name__ == '__main__':
    a = caesarCipher("There's-a-starman-waiting-in-the-sky", 3)
    print(a)