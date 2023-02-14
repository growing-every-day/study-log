class Solution {
    private static boolean[] visited; // 방문 여부
    public int removeStones(int[][] stones) {
        visited = new boolean[stones.length]; 
        int answer = 0;

        for(int i=0; i<stones.length; i++){
            // 방문하지 않았다면
            if(!visited[i]){ 
                answer++;
                // dfs 탐색
                dfs(i, stones.length, stones);                  
            }
        }

        return stones.length - answer;
    }

    public void dfs(int idx, int size, int[][] stones){
        // 방문 표시
        visited[idx] = true; 

        for(int i=0; i<size; i++){
            // 방문하지 않았고
            if(!visited[i]){
                // 같은 행이거나 같은 열이면  
                if(stones[idx][0] == stones[i][0] || stones[idx][1] == stones[i][1]){
                    // dfs 호출
                    dfs(i, size, stones);
                } 
            }
        }

        return;
    }
}
