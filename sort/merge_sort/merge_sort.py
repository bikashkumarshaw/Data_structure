class Merge_Sort(object):
    def __init__(self, lis, l, r):
        self.to_list = lis
        k = self.merge_sort(self.to_list, l, r)

    def merge(self, array,l,m,r):
        left = [0]*(m-l+1)
        right = [0]*(r-m)

        for pos in range(len(left)):
            left[pos] = array[l+pos]

        for pos in range(len(right)):
            right[pos] = array[m+1+pos]

        i = 0
        j = 0
        k = l

        while (i<len(left) and j<len(right)):
            if left[i]<=right[j]:
                array[k] = left[i]
                i=i+1
                k = k+1
            else:
                array[k] = right[j]
                j = j+1
                k = k+1

        while i<len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j<len(right):
            array[k] = right[j]
            j += 1
            k += 1

        return

    def merge_sort(self, array, l, r):
        if l<r:
            mid = (l+(r-1))/2

            a = self.merge_sort(array, l, mid)
            b = self.merge_sort(array, mid+1, r)
            c = self.merge(array, l, mid, r)

    def __str__(self):
        return str(self.to_list)
