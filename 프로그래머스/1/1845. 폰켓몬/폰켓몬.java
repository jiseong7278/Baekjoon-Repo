import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        
        HashSet<Integer> poketmon = new HashSet<>();
        
        for(int n: nums){
            poketmon.add(n);
        }
        
        if(poketmon.size()>=nums.length/2)
            answer = nums.length/2;
        else
            answer = poketmon.size();
        
        return answer;
    }
}