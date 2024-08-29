import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;

        Stack<Character> stack = new Stack<>();

        for(int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            
            if(c == '('){
                stack.push('(');
            }else{
                if(stack.isEmpty() || stack.pop()!='('){
                    answer = false;
                    break;
                }
            }
        }
        
        if(stack.size() > 0) answer = false;
        return answer;
    }   
}