import java.io.*;
import java.util.StringTokenizer;

/**
 * 문제 : 2512번 - 예산
 * 메모리 : 15800 KB
 * 시간 : 172 ms
 * */
public class moon_2512 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        // 지방의 수
        int n = Integer.parseInt(br.readLine());

        int[] arr = new int[n];

        int sum = 0;
        int max = 0;

        // 각 지방의 예산 요청 입력
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0; i<n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
            sum += arr[i];
            max = Math.max(max, arr[i]);
        }

        // 총 예산
        int m = Integer.parseInt(br.readLine());

        if(m >= sum){
            bw.write(max+"");
        } else {
            // 이분 탐색
            int low = 0;
            int high = max;

            while(low <= high){
                int mid = (low + high) / 2;
                int budget = 0;

                for(int i=0; i<n; i++){
                    // 중간 값보다 크다면 mid 값을 예산에 누적해서 계산
                    if(arr[i] > mid){
                        budget += mid;
                    // 중간 값이 더 크다면 그냥 지방에서 요구하는 예산을 누적해서 계산
                    } else {
                        budget += arr[i];
                    }
                }

                // 아직 예산이 남은 경우
                if(budget <= m){
                    low = mid + 1;
                // 예산이 오버된 경우
                } else {
                    high = mid - 1;
                }
            }

            bw.write(high+"");
        }
        bw.flush();

        bw.close();
        br.close();
    }
}
