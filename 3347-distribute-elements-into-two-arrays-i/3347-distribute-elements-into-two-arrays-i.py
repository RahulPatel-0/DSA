class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        #Approach 1
        # arr1=[]
        # arr2=[]
        # arr1.append(nums[0])
        # arr2.append(nums[1])
        # n=len(nums)
        # for i in range(2,n):
        #     if arr1[-1]>arr2[-1]:
        #         arr1.append(nums[i])
        #     else:
        #         arr2.append(nums[i])
        # for i in arr2:
        #     arr1.append(i)
        # return arr1

        n=len(nums)
        arr=[0]*n
        arr[0]=nums[0]
        arr[n-1]=nums[1]
        idx,revIdx=0,n-1
        for i in range(2,n):
            if arr[idx]>arr[revIdx]:
                idx+=1
                arr[idx]=nums[i]
            else:
                revIdx-=1
                arr[revIdx]=nums[i]
        i,j=revIdx,n-1
        while i<j:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
        return arr

        
    