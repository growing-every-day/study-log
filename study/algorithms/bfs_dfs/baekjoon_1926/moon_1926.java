import java.io.*;
import java.util.*;

/**
 * 문제 : 1926번 - 그림
 * 메모리 : 47276 KB
 * 시간 : 460 ms
 * */
public class moon_1926 {
    private static int n, m; // 도화지의 세로 크기, 가로 크기
    private static int[][] arr;
    private static boolean[][] visited; // 방문 표시
    private static int[] dx = {0, 1, 0, -1}; // x축 이동
    private static int[] dy = {-1, 0, 1, 0}; // y축 이동
    private static int count = 0;
    private static int max = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        arr = new int[n][m];
        visited = new boolean[n][m];

        // 도화지 그림 정보 입력
        for(int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<m; j++){
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int numberOfPaintings = 0; // 그림 수
        // BFS 탐색
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                // 방문하지 않았고 색칠이 된 부분이면
                if(!visited[i][j] && arr[i][j]==1){
                    count = 1;
                    bfs(i, j);
                    numberOfPaintings++;
                }
            }
        }

        // 그림의 수 출력
        bw.write(numberOfPaintings+"\n");
        // 가장 넓은 그림의 넓이 출력
        bw.write(max+"");

        bw.flush();
        bw.close();
        br.close();
    }
    // BFS 탐색
    public static void bfs(int row, int col) {
        Queue<int[]> queue = new ArrayDeque<>();
        queue.add(new int[] {row, col});

        visited[row][col] = true;

        while (!queue.isEmpty()){
            int[] node = queue.poll();

            // 4방향 탐색
            for(int i=0; i<4; i++){
                int x = node[1] + dx[i];
                int y = node[0] + dy[i];

                // 주어진 범위 안에서만 이동 가능
                if(x>=0 && y>=0 && x<m && y<n){
                    // 방문하지 않았고 색칠이 된 부분이면
                    if(!visited[y][x] && arr[y][x]==1){
                        visited[y][x] = true; // 방문 표시
                        queue.add(new int[] {y, x}); // 좌표 저장
                        count++;
                    }
                }
            }
        }
        // 가장 넓은 그림의 넓이 값 갱신
        max = count > max ? count : max;
    }
}
