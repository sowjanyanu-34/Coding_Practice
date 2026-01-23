def twosum(arr,target):
    n= len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j]==target:
                return True
    return False

if __name__ == "__main__":
    arr = [10, 15, 3, 7]
    target = 17
    if twosum(arr,target):
        print("true")
    else:
        print("false")
