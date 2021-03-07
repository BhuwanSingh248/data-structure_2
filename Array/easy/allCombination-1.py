# all r combination with the complixity of nLogn

# Program to print all combination 
# of size r in an array of size n 

def printCombination(arr, n, r): 
    data = [0] * r 
    def combinationUtil(arr, n, r, index, data, i):  
        if (index == r): 
            for j in range(r): 
                print(data[j], end = " ") 
                print() 
            return
        if (i >= n): 
            return

        data[index] = arr[i] 
        combinationUtil(arr, n, r, index + 1, data, i + 1) 
        combinationUtil(arr, n, r, index, data, i + 1) 

    combinationUtil(arr, n, r, 0, data, 0) 





if __name__ == "__main__": 
    arr = [1, 2, 3, 4, 5] 
    r = 3
    n = len(arr) 
    printCombination(arr, n, r) 

