# Search for startIdx
# Search over startIdx...len(nums) + startIdx


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        startIdx = 0
        if nums[0] > nums[-1]:
            l = 0
            r = len(nums)-1

            while l < r:
                mid = (l + r) // 2

                if nums[mid] > nums[mid + 1]:
                    startIdx = mid + 1
                    break
                elif nums[mid] < nums[mid - 1]:
                    startIdx = mid
                    break
                
                if nums[mid] > nums[0]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        l = startIdx
        r = startIdx + len(nums) - 1

        print(l, r)

        while l <= r:
            mid = (l + r) // 2
            midIdx = mid % len(nums)

            if nums[midIdx] == target:
                return midIdx
            elif nums[midIdx] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1