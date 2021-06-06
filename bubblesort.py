# Bubble Sort - Implement algoritm described by flowchart
        # Running program with outputs the foolowing nr list [1, 2, 56, 32 ,51, 2, 8, 92, 15]
        # Running program output in a asscending order 

# Binary Search - Implement alogirthm 2
        # Running program outputs list: [1, 2 , 4, 7, 11, 22, 38, 42, 43]
        # Running program output index searched value in listn, if is not return -1 (for val 4 return 2)

# Clean Code - Use function , make it easy to read and maintain
        # Running program result in same way befor and after refactoring
        # variable names in the prog are meaninful and not abbreviated
        # Functi names are meaningful verbs and not abbreviated
        # There are no unnecessary code of comm in the prog
        # There are no duplicated code parts
        # there are no funct that doing more than one thing
        # After each mod the changes are commited, progr is runnable, result in the same behavior 
        # Commit message are meaningful


# 1 . Bubble Sort:

def bubble_sort(array):  
    array = [1, 2, 56, 32, 51, 2, 8, 92, 15]
    print(array)
    i = 0
    n = len(array)
    while i < n - 1:    
        j = 0
        while j < n - i - 1:
            if array[j] > array[j + 1]:
                temp = array[j+1]
                array[j+1] = array[j]
                array[j] = temp
            j += 1
        i += 1
    print(array)

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
def main():
    print("Sorting Flowchart")
    bubble_sort(list)
    
if __name__ == "__main__":
    main()


