class Solution {
    public boolean hasDuplicate(int[] nums) {
        boolean ifTrue = false;

        for(int x = 0; x < nums.length; x++){
            for(int j = 0; j < nums.length; j++){
                if(x != j){
                  if(nums[x] == nums[j]){
                    ifTrue = true;
                  }  
                }    
            }
        }
        return ifTrue; 
    }
}
