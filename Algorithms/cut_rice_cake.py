"""
떡볶이 떡 만들기
쥬리네 떡볶이 떡은 재밌게도 떡의 길이가 일정하지 않다. 대신 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춘다.
절단기에 높이(H)를 지정하면 줄지어진 떡을 한번에 절단한다. 높이가 H 보다 긴 떡은 H 윗 부분이 잘리고, 낮은 떡은 잘리지 않는다.
예로, 길이가 19, 14, 10, 17 인 떡이 있고 H 를 15로 지정하면 자른 뒤 떡의 높이는 15, 14, 10, 15 가 된다.
잘린 떡의 길이는 4, 0, 0, 2 로 총 6 이다. 손님은 자르고 남은 떡을 가져간다. (왠지 모르겠지만)
손님이 요청한 길이가 M 일 때, 적어도 M 만큼의 떡을 얻기 위한 H 의 최대값을 구하라
"""


def find_height(arr: list[int], target: int) -> int:
    ans = 0
    start, end = 0, max(arr)
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for x in arr:
            if x > mid:
                total += x - mid
        if total >= target:
            ans = max(ans, mid)
            start = mid + 1
        else:
            end = mid - 1
    return ans


if __name__ == '__main__':
    cakes = [19, 15, 10, 17]
    M = 10
    print(find_height(cakes, M))
