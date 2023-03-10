import java.io.*;
import java.util.StringTokenizer;

/**
 * 문제 : 12869번 - 뮤탈리스크
 * 메모리 : 17324 KB
 * 시간 : 140 ms
 * */
public class moon_12869 {
    // 뮤탈리스크의 공격 패턴
    private static int[][] pattern = {  {-9, -3, -1},{-9, -1, -3},
                                        {-3, -9, -1},{-3, -1, -9},
                                        {-1, -3, -9},{-1, -9, -3}   };
    // scv의 최대 체력
    private static int[][][] dp = new int[61][61][61];
    private static int answer = Integer.MAX_VALUE;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        // scv의 수
        int n = Integer.parseInt(br.readLine());

        int[] arr = new int[3];

        // scv의 체력 입력
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0; i<n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        solve(arr, 0);

        bw.write(answer+"");
        bw.flush();

        bw.close();
        br.close();
    }

    public static void solve(int[] arr, int count) {
        // 각 scv 체력 저장
        int a1 = arr[0];
        int a2 = arr[1];
        int a3 = arr[2];

        // 최솟값보다 현재 공격 횟수가 같거나 클 경우 종료
        if(answer <= count) return;

        // 이미 방문한 곳이고 현재 공격 횟수(count)보다 더 작을 경우 종료
        if(dp[a1][a2][a3] != 0 && dp[a1][a2][a3] <= count) return;

        // 현재 공격 횟수로 방문 표시
        dp[a1][a2][a3] = count;

        // scv가 모두 파괴되었다면 최솟값 갱신
        if(a1==0 && a2==0 && a3==0){
            answer = Math.min(answer, count);
            return;
        }
        // 뮤탈리스크의 6가지 공격 패턴을 적용하여 탐색
        for(int i=0; i<6; i++){
            int scv1 = Math.max(a1+pattern[i][0], 0);
            int scv2 = Math.max(a2+pattern[i][1], 0);
            int scv3 = Math.max(a3+pattern[i][2], 0);

            solve(new int[]{scv1, scv2, scv3}, count+1);
        }
    }
}
