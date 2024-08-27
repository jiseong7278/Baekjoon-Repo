class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int answer = 0;
        
        int curHealth = health;
        
        int healCount = 0; // 연속 회복
        
        int attackCount = 0; // 공격 횟수
        int endTime = attacks[attacks.length-1][0]; // 마지막 공격 시간
        
        for(int i=0; i<=endTime; i++){
            if(i==attacks[attackCount][0]){
                curHealth -= attacks[attackCount][1];
                attackCount++;
                healCount = 0;
                if(curHealth<=0){ // 체력이 0보다 낮을 경우 -1
                    curHealth = -1;
                    break;
                }
                continue;
            }
            
            if(curHealth<health){
                curHealth += bandage[1];
                healCount++;
                if(healCount==bandage[0]){
                    curHealth += bandage[2];
                    healCount=0;
                }
                
                if(curHealth > health){
                    curHealth = health;
                }
            }
        }
        
        answer = curHealth;
        
        return answer;
    }
}