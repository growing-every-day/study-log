import java.io.*;

/**
 * 문제 : 11727번 - 2×n 타일링 2
 * 메모리 : 14440 KB
 * 시간 : 128 ms
 * */
public class moon_11727 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());

        int[] dp = new int[n+1];

        for(int i=0; i<=n; i++){
            if(i<=1)
                dp[i] = i;
            else if(i==2)
                dp[i] = 3;
            else {
                dp[i] = (2*dp[i-2] + dp[i-1]) % 10007;
            }
        }

        bw.write(dp[n]+"");
        bw.flush();

        bw.close();
        br.close();
    }
}
