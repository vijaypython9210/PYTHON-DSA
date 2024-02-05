class BubbleSort:
    @staticmethod
    def ascendingSort(arr):
        for i in range(len(arr)-1):
            for j in range(0,len(arr)-1-i):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr
    
if __name__=="__main__":
    arr=[5,4,2,1,2]
    print(BubbleSort.ascendingSort(arr))