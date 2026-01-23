def twoSum(arr, target):
    seen = set()

    for num in arr:
        complement = target - num

        if complement in seen:
            return True

        seen.add(num)

    return False


arr = [0, -1, 2, -3, 1]
target = -2

if twoSum(arr, target):
    print("true")
else:
    print("false")
