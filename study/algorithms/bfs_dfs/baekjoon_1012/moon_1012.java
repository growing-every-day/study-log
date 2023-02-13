import java.io.*;
import java.util.*;

/***
 * 문제 : 1012번 - 유기농 배추
 * 메모리 : 16344 KB
 * 시간 : 180 ms
 */

public class Main {
    private static int[] dx = {0, 1, 0, -1}; // x축 이동
    private static int[] dy= {-1, 0, 1, 0}; // y축 이동
    private static int[][] cabbage; // 배추 밭
    private static boolean[][] visited; // 방문 표시
    private static int m, n; // 배추밭 가로 길이와 세로 길이
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int T = Integer.parseInt(br.readLine()); // 테스트 케이스의 개수

        for(int t=0; t<T; t++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            m = Integer.parseInt(st.nextToken()); // 배추밭 가로의 길이
            n = Integer.parseInt(st.nextToken()); // 배추밭 세로의 길이
            int k = Integer.parseInt(st.nextToken()); // 배추가 심어져 있는 위치의 개수

            cabbage = new int[n][m];
            visited = new boolean[n][m];

            // 배추들의 위치 입력
            for(int i=0; i<k; i++){
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());

                cabbage[y][x] = 1;
            }

            int answer = 0;

            // 필요한 최소의 배추흰지렁이 마리 수 탐색
            for(int i=0; i<n; i++){
                for(int j=0; j<m; j++){
                    // 방문하지 않았고 배추가 심어져 있어야 함
                    if(!visited[i][j] && cabbage[i][j]==1){
                        bfs(i, j); // BFS 탐색
                        answer++; // 배추흰지렁이 수 추가
                    }
                }
            }

            bw.write(answer+"\n");
        }
        bw.flush();

        bw.close();
        br.close();
    }
    // BFS 방식
    public static void bfs(int row, int col){
        Queue<int[]> queue = new ArrayDeque<>();
        queue.add(new int[]{row, col}); // y축, x축 좌표 저장

        visited[row][col] = true;

        while(!queue.isEmpty()){
            int[] location = queue.poll(); // location[0]=y축, location[1]=x축

            // 4방향 탐색
            for(int i=0; i<4; i++){
                int y = location[0] + dy[i];
                int x = location[1] + dx[i];

                // 주어진 범위 안에만 이동할 수 있어야함
                if(x>=0 && y>=0 && x<m && y<n){
                    // 방문하지 않았고 배추가 심어져 있어야함
                    if(!visited[y][x] && cabbage[y][x]==1){
                        visited[y][x] = true; // 방문 표시
                        queue.add(new int[]{y, x}); // 좌표 저장
                    }
                }
            }
        }
    }
}
