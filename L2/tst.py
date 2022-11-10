val = int(input("Enter value to search for: "))


def binary(arr, p, q, val):
    mid = int((p + q) / 2)
    if p <= q:
        if arr[mid] > val:
            return binary(arr, p, mid - 1, val)
        elif arr[mid] < val:
            return binary(arr, mid + 1, q, val)
        else:
            return mid
    else:
        return None


parameter_arr = [1, 2, 2, 4, 5, 6, 8, 8, 9, 10, 12]

print(binary(parameter_arr, 0, 10, val))
