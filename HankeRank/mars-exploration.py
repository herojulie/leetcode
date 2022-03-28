def marsExploration(s) -> int:
    # Write your code here
    if len(s) % 3 != 0:
        return -1

    answer = 0
    i = 0
    while i < len(s):
        partial_string = s[i:i+3]
        answer += determineSOS(partial_string)
        i += 3
    return answer


def determineSOS(s) -> int:
    if len(s) != 3:
        raise Exception('Parameter s must consist of three characters!')
    count = 0
    if s[0] != 'S':
        count += 1
    if s[1] != 'O':
        count += 1
    if s[2] != 'S':
        count += 1
    return count


print(marsExploration('SOSSPSSQSSOR'))
