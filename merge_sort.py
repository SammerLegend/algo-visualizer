def run(numbers):
    arr = list(numbers)

    def merge_sort(items):
        if len(items) <= 1:
            return items

        midpoint = len(items) // 2
        left = merge_sort(items[:midpoint])
        right = merge_sort(items[midpoint:])

        merged = []
        left_index = 0
        right_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

        merged.extend(left[left_index:])
        merged.extend(right[right_index:])
        return merged

    return merge_sort(arr)
