def remove_dups(arr):
    count = len(arr)
    i = 0
    while i < count:
        j = i
        while j < count:
            if arr[j] == arr[i] and j != i:
                arr.pop(j)
                count -= 1
            j += 1
        i += 1

def main():
    arr = [-50, 66, 80, 58, -50, 86, -19, -35, 45, 80, 80, -6, 34]
    remove_dups(arr)
    print(arr)

main()