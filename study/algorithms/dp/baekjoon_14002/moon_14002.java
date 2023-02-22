import java.io.*;
import java.util.*;

/**
 * 문제 : 14002번 - 가장 긴 증가하는 부분 수열 4
 * 메모리 : 17620 KB
 * 시간 : 176 ms
 * */
public class moon_14002 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());

        int[] arr = new int[n];

        // 값 입력(10 20 10 30 20 50)
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0; i<n; i++)
            arr[i] = Integer.parseInt(st.nextToken());

        int[] dp = new int[n];
        dp[0] = 1;

        // 가장 긴 증가하는 부분 수열 탐색
        for(int i=1; i<n; i++){
            dp[i] = 1;

            for(int j=0; j<i; j++){
                if(arr[i]>arr[j] && dp[i]<=dp[j]){
                    dp[i] = dp[j] + 1;
                }
            }
        }

        int answer = 0;

        for(int value : dp){
            answer = Math.max(answer, value);
        }
        // 가장 긴 증가하는 부분 수열의 길이 출력
        bw.write(answer+"\n");

        ArrayList<Integer> list = new ArrayList<>();

        // 가장 긴 증가하는 부분 수열들을 저장하기 위해 탐색
        for(int i=n-1; i>=0; i--){
            // 앞에서 구한 가장 긴 증가하는 부분 수열의 길이를 이용하여 부분 수열들을 list에 저장
            if(answer==dp[i]){
                list.add(arr[i]);
                answer--;
            }
        }
        // 부분 수열 출력
        for(int i=list.size()-1; i>=0; i--)
            bw.write(list.get(i)+" ");
        bw.flush();

        bw.close();
        br.close();
    }
}
