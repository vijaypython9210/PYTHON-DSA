class SelectionSort:
    @staticmethod
    def ascendingSort(arr):
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i]>arr[j]:
                    arr[i],arr[j]=arr[j],arr[i]
        return arr
    
if __name__=="__main__":
    arr=[3,2,4,5,1]
    print(SelectionSort.ascendingSort(arr))