import java.util.*;

class Solution {
    
    int[] parents;
    
    void union(int a, int b){
        a = find(a);
        b = find(b);
        
        if(a!=b){
            parents[b] = a;
        }
    }
    
    int find(int a){
        if(a == parents[a]){
            return a;
        }else{
            return parents[a] = find(parents[a]);
        }
    }
    
    public int solution(int n, int[][] computers) {
        int answer = 0;
        parents = new int[n];
        
        for(int i=0; i<n; i++){
            parents[i] = i;
        }
        
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                if(computers[i][j] == 1) union(i, j);
            }
        }
        
        for(int i=0; i<parents.length; i++){
            if(i==parents[i]) answer++;
        }
        
        return answer;
    }
}