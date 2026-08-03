class Solution {
    public boolean hasDuplicate(int[] nums) {
       Set<Integer> du = new HashSet<>();

       for(int num = 0; num < nums.length; num++){
        if(du.contains(nums[num])){
            return true;
        }
        du.add(nums[num]);
       }
       return false;
    }
}
