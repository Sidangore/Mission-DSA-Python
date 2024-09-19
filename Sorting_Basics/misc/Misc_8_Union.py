def union(nums1, nums2):
    i, j = 0, 0
    m, n = len(nums1), len(nums2)
    res = []

    while i < m and j < n:
        if i > 0 and nums1[i - 1] == nums1[i]:
            i += 1
        elif j > 0 and nums2[j - 1] == nums2[j]:
            j += 1
        elif nums1[i] < nums2[j]:
            res.append(nums1[i])
            i += 1
        elif nums2[j] < nums1[i]:
            res.append(nums2[j])
            j += 1
        else:
            res.append(nums1[i])
            i += 1
            j += 1

    while i < m:
        if nums1[i] != nums1[i - 1]:
            res.append(nums1[i])
        i += 1

    while j < n:
        if nums2[j - 1] != nums2[j]:
            res.append(nums2[j])
        j += 1

    return res


if __name__ == '__main__':
    n1, n2 = [1, 3, 3, 3, 5, 6], [2, 3, 3, 4, 4, 7, 8, 8, 9]
    res = union(n1, n2)
    print(res) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
