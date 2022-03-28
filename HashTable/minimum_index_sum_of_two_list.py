from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        def load(stores: {}, l: [str]) -> {str: [int]}:
            for i, res in enumerate(l):
                if res in stores:
                    stores[res].append(i)
                else:
                    stores[res] = [i]
            return stores

        restaurants = load(dict(), list1)
        restaurants = load(restaurants, list2)

        min_store: [str] = []
        min_sum = 2000
        for name, indexes in restaurants.items():
            if len(indexes) == 2:
                if min_sum > sum(indexes):
                    min_sum = sum(indexes)
                    min_store = [name]
                elif min_sum == sum(indexes):
                    min_store.append(name)

        return min_store


if __name__ == '__main__':
    print(Solution().findRestaurant(list1=["Shogun", "Tapioca Express", "Burger King", "KFC"],
                                    list2=["KFC", "Piatti", "Tapioca Express", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse",
                                           "Shogun"]))
