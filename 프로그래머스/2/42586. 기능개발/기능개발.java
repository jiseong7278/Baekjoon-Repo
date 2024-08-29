import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int[] answer;
        
        int n = progresses.length;
        
        Queue<Integer> queue = new LinkedList<>();
        ArrayList<Integer> answerList = new ArrayList<>();
        
        for(int i=0; i<n; i++){
            int days = (100 - progresses[i])/speeds[i];
            if((100-progresses[i])%speeds[i]!=0){
                days++;
            }
            queue.add(days);
        }
        
        int now = queue.poll();
        int count = 1;
        
        while(!queue.isEmpty()){
            int next = queue.poll();
            
            if(now < next){
                answerList.add(count);
                now = next;
                if(queue.isEmpty()){
                    answerList.add(1);
                }
                count = 1;
            }else{
                count++;
                if(queue.isEmpty()){
                    answerList.add(count);
                }
            }
        }
        
        n = answerList.size();
        
        answer = new int[n];
        
        for(int i=0; i<n; i++){
            answer[i] = answerList.get(i);
        }
        
        return answer;
    }
}