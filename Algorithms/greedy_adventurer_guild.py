"""
모험가 길드
한 마을에 모험가가 N 명 있습니다. 모험가 길드에서는 N 명의 모험가를 대상으로 '공포도'를
측정했는데, '공포도'가 높은 모험가는 쉽게 공포를 느껴 위험 상황에서 제대로 대처할 능력이 떨어집니다.
모험가 길드장인 쥬리는 모험가 그룹을 안전하게 구성하고자 공포도가 X 인 모험가는 반드시 X 명 이상으로
구성한 모험가 그룹에 참여해야 여행을 떠날 수 있도록 규정했습니다.
단 몇 명의 모험가는 마을에 그대로 남아있어도 되기 때문에, 모든 모험가를 그룹에 할당할 필요는 없습니다.
N 명의 모험가를 대상으로 만들 수 있는 최대 모험가 그룹 수를 구하는 프로그램을 작성하시오.
"""

class AdventurerGroup:
    def create_groups(self, adventurers):
        adventurers.sort()
        group = 0
        while adventurers:
            t = adventurers[0]
            if t <= len(adventurers):
                adventurers = adventurers[t:]
                group += 1
            else:
                break
        return group


if __name__ == '__main__':
    ans = AdventurerGroup().create_groups(adventurers=[5, 3, 1, 2, 2])
    print(ans)
