def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

if __name__ == "__main__":
    data = [56, 34, 23, 15, 89, 31, 28, 87, 2, 200]
    print("List awal:", data)

    target = int(input("Masukkan elemen yang ingin dicari: "))

    sorted_data = bubble_sort(data)
    print("Setelah BubbleSort:", sorted_data)

    result = binary_search(sorted_data, target)

    if result != -1:
        print(f"Elemen ditemukan pada posisi ke-{result + 1}")
    else:
        print("Elemen tidak ditemukan pada list")
