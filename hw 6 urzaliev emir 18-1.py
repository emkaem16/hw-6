enter_num = int(input('enter num between 0 and 1_000_000 with interval 2:'))


class Solution:
    def get_list(self):
        return list(range(0, 10000000, 2))

    def find_target(self, list, target):
        self.begin = 0
        self.end = len(list) - 1


        while self.begin <= self.end:
            mid = self.begin + (self.end - self.begin) // 2



            element = list[mid]

            if element == target:
                return f'index: {mid}'
            elif target < element:
                self.end = mid - 1
            else:
                self.begin = mid + 1
            return None

sol = Solution()
b = sol.get_list()

print(sol.find_target(b, enter_num))