import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int answer = -1;
        
        int N = maps.length;
        int M = maps[0].length;
        
        int[] dx = {0, 1, 0, -1};
        int[] dy = {1, 0, -1, 0};
        
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[] {0, 0, 1});
        maps[0][0] = 0;
        
        while(!queue.isEmpty()){
            int[] curIndex = queue.poll();
            
            for(int i=0; i<4; i++){
                int nx = curIndex[0] + dx[i];
                int ny = curIndex[1] + dy[i];
                int breadth = curIndex[2];
                
                if(nx < 0 || ny < 0 || nx >= N || ny >= M){
                    continue;
                }
                
                if(maps[nx][ny]!=1){
                    continue;
                }
                
                breadth++;
                
                if(nx == N-1 && ny == M-1){
                    answer = breadth;
                }
                
                queue.add(new int[] {nx, ny, breadth});
                maps[nx][ny] = 0;
            }
        }
        
        return answer;
    }
}