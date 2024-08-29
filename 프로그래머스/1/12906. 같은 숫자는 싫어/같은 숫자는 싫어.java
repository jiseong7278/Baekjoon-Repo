import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        int[] answer;
        
        Stack<Integer> stack = new Stack<>();

        for(int a: arr){
            if(stack.isEmpty()){
                stack.push(a);
            }else{
                int temp = stack.pop();
                if(temp == a){
                    stack.push(a);
                }else{
                    stack.push(temp);
                    stack.push(a);
                }
            }
        }
        
        int size = stack.size();
        
        answer = new int[size];
        
        for(int i=0; i<size; i++){
            answer[size-i-1] = stack.pop();
        }
        
        return answer;
    }
}