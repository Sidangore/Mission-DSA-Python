def intersection(nums1, nums2):
    m, n = len(nums1), len(nums2)
    i, j = 0, 0
    res = []

    while i < m and j < n:
        if i > 0 and nums1[i - 1] == nums1[i]:
            i += 1
        elif j > 0 and nums2[j - 1] == nums2[j]:
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        elif nums2[j] < nums1[i]:
            j += 1
        else:
            res.append(nums1[i])
            i += 1
            j += 1

    return res


if __name__ == '__main__':
    nums1, nums2 = [1, 3, 3, 3, 5, 6], [2, 3, 3, 4, 4, 6, 8, 8, 9]
    res = intersection(nums1, nums2)
    print(res)
