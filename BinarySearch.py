class BinarySearch:
    @staticmethod
    def find(arr,target):
        start=0
        end=len(arr)-1
        if arr[start]<arr[end]:
            while(True):
                mid=int((start+end)/2)
                if arr[mid]==target:
                    return mid
                elif arr[mid]<target:
                    start=mid+1
                else:
                    end=mid-1
        else:
            while(True):
                mid=int((start+end)/2)
                if arr[mid]==target:
                    return mid
                elif arr[mid]<target:
                    end=mid-1
                else:
                    start=mid+1
    
if __name__=="__main__":
    arr=[1,2,3,4,5]
    arr2=[5,4,3,2,1]
    print(BinarySearch.find(arr,3))
    print(BinarySearch.find(arr2,2))
    