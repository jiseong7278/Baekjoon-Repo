import java.util.*;

class Solution {
    public int solution(String[] friends, String[] gifts) {
        int answer = 0;
        
        int N = friends.length;
        int M = gifts.length;
        
        HashMap<String, Integer> hashMap = new HashMap<>();
        
        int[] result = new int[N];
        int[] giftIndex = new int[N];
        int[][] arr = new int[N][N];
        
        for(int i=0; i<N; i++){
            hashMap.put(friends[i], i);
        }
        
        for(int i=0; i<M; i++){
            String[] strArr = gifts[i].split(" ");
            int sender = hashMap.get(strArr[0]);
            int reciever = hashMap.get(strArr[1]);
            arr[sender][reciever]++;
            giftIndex[sender]++;
            giftIndex[reciever]--;
        }
        
        for(int i=0; i<N; i++){
            for(int j=i+1; j<N; j++){
                if(arr[i][j] > arr[j][i]){
                    result[i]++;
                }else if(arr[i][j] == arr[j][i]){
                    if(giftIndex[i] > giftIndex[j]){
                        result[i]++;
                    }else if(giftIndex[i] < giftIndex[j]){
                        result[j]++;
                    }
                }else{
                    result[j]++;
                }
            }
        }
        
        for(int i=0; i<result.length; i++){
            answer = Math.max(answer, result[i]);
        }
        
        return answer;
    }
}