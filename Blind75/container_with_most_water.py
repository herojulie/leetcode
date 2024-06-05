# https://leetcode.com/problems/container-with-most-water/description/

def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    answer = 0
    l, r = 0, len(height) - 1
    while l < r:
        area = (r - l) * min(height[l], height[r])
        answer = max(answer, area)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return answer


if __name__ == '__main__':
    print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
