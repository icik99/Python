import random
import time

# ini adalah program binary search, digunakan untuk mencari data yang BERURUTAN

# kita akan membandingkan naive search dengan binary search

#ini adalah naive search
def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

# anggap listnya telah berurutan

def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1
    
    if high < low:
        return -1

    # misal l = [1, 3, 5, 10, 12], kita ingin mencari 10, harusnya return 3
    titik_tengah = (low + high) // 2

    if l[titik_tengah] == target:
        return titik_tengah
    elif target < l[titik_tengah]:
        return binary_search(l, target, low, titik_tengah-1)
    else:
        #target > l[titik_tengah]
        return binary_search(l, target, titik_tengah +1, high)

if __name__ == "__main__":
    # l = [1, 3, 5, 10, 12]
    # target = 12
    # print (naive_search(l, target))
    
    length = 10000
    # kita akan membuat list yang berurutan 
    sorted_list = set()
    while len(sorted_list) < length:
        # sorted list akan terus mengulangi dari -30000 sampai 30000
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print ("Waktu pencarian Naive Search :" , (end - start) / length, "detik")

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print ("Waktu pencarian Binary Search :" , (end - start) / length, "detik")
