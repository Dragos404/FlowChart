def binary_search(list):
    list = [1, 2 , 4, 7, 11, 22, 38, 42, 43]
    print(list)
    start = 0 
    end = len(list) - 1
    val = int(input("Put your val here: "))
    index = 0
    while start <= end:
        mid = (start + end)//2
        if list[mid] == val:
            index = mid 
            break
        # This condition was hardcoded in the loop, instead of 4 it 
        # could have been another value in the list for that index (bug)
        # elif val == 4:
        #     print("2")
        #     break
        # else:
        if list[mid] > val:
            end = mid - 1
        else:
            start = mid + 1

    else:
        index = -1
    print(index)

binary_search(list)