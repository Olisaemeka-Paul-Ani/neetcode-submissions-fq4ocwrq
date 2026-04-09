class Solution {

    hasDuplicate(nums) {
        let hashSet = new Set ([nums[0]])
        for (let i = 1; i < nums.length;i++){
            if (hashSet.has(nums[i])){
                return true 
                
            }else{ 
                hashSet.add(nums[i])

                }
        }
        return false
    }
}
