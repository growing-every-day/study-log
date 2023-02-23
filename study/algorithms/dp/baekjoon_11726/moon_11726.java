import java.io.*;

/**
 * 문제 : 11726번 - 2×n 타일링
 * 메모리 : 14348 KB
 * 시간 : 136 ms
 * */
public class moon_11726 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());

        int[] dp = new int[n+1];

        for(int i=0; i<=n; i++){
            if(i<=2)
                dp[i] = i;
            else
                dp[i] = (dp[i-2] + dp[i-1]) % 10007;
        }

        bw.write(dp[n]+"");
        bw.flush();

        bw.close();
        br.close();
    }
}
