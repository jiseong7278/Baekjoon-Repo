import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = 0;
        
        for(int i=0; i<s.length(); i++){
            boolean check = false;
            Stack<Character> stack = new Stack<>();
            for(int j=0; j<s.length(); j++){
                check = false;
                switch(s.charAt((i+j)%s.length())){
                    case '(':
                        stack.push('(');
                        break;
                    case '{':
                        stack.push('{');
                        break;
                    case '[':
                        stack.push('[');
                        break;

                    case ')':
                        if(stack.empty()){
                            break;
                        }else{
                            if(stack.pop()=='('){
                                check = true;
                                break;
                            }
                        }
                    case '}':
                        if(stack.empty()){
                            break;
                        }else{
                            if(stack.pop()=='{'){
                                check = true;
                                break;
                            }
                        }
                    case ']':
                        if(stack.empty()){
                            break;
                        }else{
                            if(stack.pop()=='['){
                                check = true;
                                break;
                            }
                        }
                }
                if(!stack.isEmpty()){
                    check = false;
                }
            }
            if(check){
                answer++;
            }
        }
        
        return answer;
    }
}