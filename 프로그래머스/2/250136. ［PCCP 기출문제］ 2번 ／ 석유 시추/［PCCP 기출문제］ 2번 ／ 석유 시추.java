import java.util.*;

class Solution {
    
    int[] sum;
    int[] dx = {0, 1, 0, -1};
    int[] dy = {1, 0, -1, 0};
    
    public int solution(int[][] land) {
        int answer = 0;
        
        sum = new int[land[0].length];
        
        for(int i=0; i<land.length; i++){
            for(int j=0; j<land[0].length; j++){
                if(land[i][j] == 1){
                    Queue<int[]> queue = new LinkedList<>();
                    queue.add(new int[] {i, j});
                    land[i][j] = 0;
                    
                    int count = 1;
                    
                    int[] nArr = new int[land[0].length];
                    
                    nArr[j] = 1;
                    
                    while(!queue.isEmpty()){
                        int[] cur = queue.poll();
                        
                        for(int k=0; k<4; k++){
                            int nx = cur[0] + dx[k];
                            int ny = cur[1] + dy[k];
                            
                            if(nx < 0 || ny < 0 || nx >= land.length || ny >= land[0].length){
                                continue;
                            }
                            
                            if(land[nx][ny] == 0){
                                continue;
                            }
                            
                            land[nx][ny] = 0;
                            queue.add(new int[] {nx, ny});
                            count++;
                            
                            nArr[ny] = 1;
                        }
                    }
                    
                    for(int k=0; k<nArr.length; k++){
                        if(nArr[k] == 1){
                            sum[k] += count;
                        }
                    }
                }
            }
        }
        
        for(int s: sum){
            answer = Math.max(answer, s);
        }
        
        return answer;
    }
}