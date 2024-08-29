import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] answer;
        
        int n = answers.length;
        
        int[] score = new int[3];
        
        int[] pattern1 = {1, 2, 3, 4, 5};
        int[] pattern2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] pattern3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        
        for(int i=0; i<n; i++){
            if(answers[i] == pattern1[i%5]) score[0]++;
        }
        
        for(int i=0; i<n; i++){
            if(answers[i] == pattern2[i%8]) score[1]++;
        }
        
        for(int i=0; i<n; i++){
            if(answers[i] == pattern3[i%10]) score[2]++;
        }
        
        int max = -1;
        
        for(int i=0; i<3; i++){
            max = Math.max(score[i], max);
        }
        
        int count = 0;
        
        for(int s: score){
            if(max == s) count++;
        }
        
        answer = new int[count];
        
        count = 0;
        
        for(int i=0; i<3; i++){
            if(score[i] == max){
                answer[count] = i+1;
                count++;
            }
        }
        
        return answer;
    }
}