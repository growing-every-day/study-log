import java.io.*;
import java.util.StringTokenizer;

/**
 * 문제 : 11053번 - 가장 긴 증가하는 부분 수열
 * 메모리 : 14716 KB
 * 시간 : 156 ms
 * */
public class moon_11053 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        // 수열 크기 입력
        int n = Integer.parseInt(br.readLine());

        int[] arr = new int[n];

        // 값 입력(10 20 10 30 20 50)
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0; i<n; i++)
            arr[i] = Integer.parseInt(st.nextToken());

        int[] dp = new int[n];
        dp[0] = 1;

        for(int i=1; i<n; i++){
            // 초기에 길이 1 저장
            dp[i] = 1;

            for(int j=0; j<i; j++){
                // j 인덱스보다 현재 위치(i)에 있는 값이 더 크고, dp의 j 인덱스까지 저장된 길이가 더 큰 경우
                if(arr[i]>arr[j] && dp[i]<=dp[j]){
                    // 현재 위치까지 길이를 갱신
                    dp[i] = dp[j] + 1;
                }
            }
        }

        int answer = 0;

        // 가장 긴 증가하는 부분 수열의 길이 탐색
        for(int value : dp){
            answer = Math.max(answer, value);
        }

        bw.write(answer+"");
        bw.flush();

        bw.close();
        br.close();
    }
}
