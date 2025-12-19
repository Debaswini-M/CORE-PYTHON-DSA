
#method for linearsearch
def linear_search(lst,*target):
    found_indices = {}
    for num in target:
        found_indices[num]=None
        for i in range(0, len(lst)):
            if lst[i]== num:
                found_indices[num]=i
                break
    return found_indices





def verify(result):
    for num,index  in result.items():
        if index is None:
            print(f"Sorry,Dude! The number{num} doesn't exist in the list..")
        else:
            print(f"Number {num} found in the list at index {index}")


def main():
    lst=[1,2,3,4,5,6,7,77,99,100,1456]
    try:

        number = input("Enter your desired number you wanna search for:")
        numbers = [int(x.strip()) for x in number.split(",")]
        results = linear_search(lst,*numbers)
        verify(results)
    except ValueError:
        print("Invalid input!Please Enter numbers separated by commas .")

if __name__ == "__main__":
    main()