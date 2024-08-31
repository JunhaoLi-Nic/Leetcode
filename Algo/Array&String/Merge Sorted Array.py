'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should
be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
'''


class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        list1 = []

        for index_m in range(m):
            list1.append(nums1[index_m])

        for index_n in range(n):
            list1.append(nums2[index_n])

        n = len(list1)

        for i in range(n):
            for j in range(0, n - i - 1):
                if list1[j] > list1[j + 1]:
                    list1[j], list1[j + 1] = list1[j + 1], list1[j]

        print(list1)


if __name__ == '__main__':
    solution = Solution()
    solution.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)

    solution.merge([1], 1, [], 0)

    solution.merge([0], 0, [1], 1)