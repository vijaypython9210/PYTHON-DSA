class LinearSearch:
    @staticmethod
    def find(arr,target):
        for i in range(len(arr)):
            if arr[i]==target:
                return i
        return -1
    
    @staticmethod
    def find_2d_array(arr,target):
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j]==target:
                    return [i,j]
        return -1
    
    @staticmethod
    def contains(arr,target):
        for i in range(0,len(arr)):
            if arr[i]==target:
                return True
        return False
    
    
if __name__=="__main__":
    arr=[1,2,3,4,5,6]
    arr2=[[1,2,3],[4,5,6]]
    arr3=[['vijay','ajay','viky'],['vinoth','harish','yogesh']]
    name="Durai"
    arr_target=6
    arr2_target=6
    arr3_target='harish'
    name_target='o'
    print(LinearSearch.find(arr,arr_target))
    print(LinearSearch.find(name,name_target))
    print(LinearSearch.contains(arr,arr_target))
    print(LinearSearch.contains(name,name_target))
    print(LinearSearch.find_2d_array(arr3,arr3_target))