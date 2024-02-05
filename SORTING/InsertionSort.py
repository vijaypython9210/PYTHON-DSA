class InsertionSort:
    @staticmethod
    def sort(arr):
        for i in range(1,len(arr)):
            for j in range(i,0,-1):
                if arr[j]<arr[j-1]:
                    arr[j],arr[j-1]=arr[j-1],arr[j]
                else:
                    break
        return arr


if __name__=="__main__":
    arr=[5,2,3,1,4]
    print(InsertionSort.sort(arr))