def binary_search(lst,target):
    if len(lst) != 0:
        mid = len(lst)//2
        if lst[mid] == target:
            return mid
        else:
            if lst[mid]>target:
                return binary_search(lst[:mid],target)
            else:
                return binary_search(lst[mid+1:],target)
    else:
        return None

def binary_search_multipleargs(lst,*target):
    found_indices={}
    for target in target:
        found_indices[target] = binary_search(lst,target)
    return found_indices



def verify(result):
    for num,idx in result.items():
        if idx is None:
            print(f"Sorry,Dude! The number {num} doesn't exist in the list..")
        else:
            print(f"Number {num} is found in the list at index {idx}")



def main():
    lst = [1,2,3,4,6,8,9,10,12,15]
    user_input = input("Enter your numbers you wanna search from the list: ")
    number = [int(x.strip()) for x in user_input.split(",")]
    results = binary_search_multipleargs(lst, *number)
    verify(results)

if __name__ == "__main__":
    main()
