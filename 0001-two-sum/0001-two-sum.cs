public class Solution {
    public int[] TwoSum(int[] nums, int target) {
    //     int n=nums.Length;
    //     for(int i=0;i<n;i++){
    //         for (int j=i+1;j<n;j++){
    //             if((nums[i]+nums[j])==target){
    //                 return new int [] {i,j};
    //             }
    //         }
            
    //     }
    //     return new int[]{};
    // }

    // Approach 2
    Dictionary<int,int> map=new Dictionary<int,int>();
    for (int i=0;i<nums.Length;i++){
        int rem=target-nums[i];
        if(map.ContainsKey(rem)){
            return new int[]{map[rem],i};
        }
        map[nums[i]]=i;
    }
    return new int[]{};
}}