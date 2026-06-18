'''
The array could be rotated by an x amount. We can find the inflection point x and conduct 
binary search over [x, x + len(nums)] using modulos

nums = [4,5,6,7,0,1,2]

'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        if not nums[0] < nums[-1]:
            while l < r:
                mid = (l + r) // 2

                if nums[mid] > nums[mid + 1]:
                    l = mid + 1
                    break
                if nums[mid - 1] > nums[mid]:
                    l = mid
                    break
                if nums[mid] > nums[0]:
                    l = mid + 1
                else:
                    r = mid - 1

        r = len(nums) - 1 + l
        while l < r:
            mid = (l + r) // 2
            midMod = mid % len(nums)

            if nums[midMod] == target:
                return midMod
            elif target > nums[midMod]:
                l = mid + 1
            else:
                r = mid - 1

        if nums[l % len(nums)] == target:
            return l % len(nums)
        return -1

        