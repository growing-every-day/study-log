import java.io.*;
import java.util.*;

/**
 * 문제 : 2178번 - 미로 탐색
 * 메모리 : 102836 KB
 * 시간 : 672 ms
 * */
public class moon_2178 {
    private static int n, m; // 미로의 세로, 가로 크기
    private static boolean[][] visited; // 방문 표시
    private static int[][] maze;
    private static int[] dx = {0, 1, 0, -1}; // x축 이동
    private static int[] dy = {-1, 0, 1, 0}; // y축 이동
    private static int min = Integer.MAX_VALUE;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        maze = new int[n][m];
        visited = new boolean[n][m];

        // 미로 정보 입력
        for(int i=0; i<n; i++){
            String s = br.readLine();
            for(int j=0; j<m; j++){
                maze[i][j] = Integer.parseInt(s.split("")[j]);
            }
        }

        // BFS 탐색
        bfs(0, 0);

        // 최소 칸의 수 출력
        bw.write(min+"");
        bw.flush();

        bw.close();
        br.close();
    }
    // BFS 탐색
    public static void bfs(int row, int col){
        Queue<int[]> queue = new ArrayDeque<>();
        queue.add(new int[] {row, col});

        visited[row][col] = true;

        while (!queue.isEmpty()){
            int[] node = queue.poll();

            // 목적지에 도달했다면
            if(node[0]==n-1 && node[1]==m-1){
                // 최솟값 갱신
                min = Math.min(min, maze[node[0]][node[1]]);
                return;
            }

            for(int i=0; i<4; i++){
                int x = node[1] + dx[i];
                int y = node[0] + dy[i];

                // 주어진 범위 안에서만 이동
                if(x>=0 && y>=0 && x<m && y<n){
                    // 방문하지 않았고 이동할 수 있다면
                    if(!visited[y][x] && maze[y][x]!=0){
                        // 방문 표시
                        visited[y][x] = true;
                        // 좌표 저장
                        queue.add(new int[] {y, x});
                        // 미로를 나타내는 배열에 이전까지의 이동 거리를 누적해서 계산
                        maze[y][x] = maze[node[0]][node[1]] + 1;
                    }
                }
            }
        }
    }
}
