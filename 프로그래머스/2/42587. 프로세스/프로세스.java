import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        
        int n = priorities.length;
        
        Queue<Integer> queue = new LinkedList<>();
        
        for(int p: priorities){
            queue.add(p);
        }
        
        Arrays.sort(priorities);
        
        int count = 1;
        
        while(!queue.isEmpty()){
            int temp = queue.poll();
            if(temp == priorities[n-count]){
                if(location == 0){
                    answer = count;
                    break;
                }
                location--;
                count++;
            }else{
                queue.add(temp);
                location--;
                if(location<0) location = queue.size()-1;
            }
        }
        
        return answer;
    }
}