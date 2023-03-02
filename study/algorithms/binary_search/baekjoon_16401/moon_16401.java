import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

/**
 * 문제 : 16401번 - 과자 나눠주기
 * 메모리 : 124368 KB
 * 시간 : 1256 ms
 * */
public class moon_16401 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        // 조카의 수, 과자의 수 입력
        StringTokenizer st = new StringTokenizer(br.readLine());
        int m = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());

        int[] arr = new int[n];

        // 과자의 길이 입력
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        // 과자 길이 오름차순 정렬
        Arrays.sort(arr);

        // 이분 탐색
        int low = 1;
        int high = arr[n-1];

        while(low <= high){
            int mid = (low+high) / 2;
            // 나누어 줄 수 있는 과자의 개수
            int count = 0;

            for(int i=0; i<n; i++){
                if(arr[i] >= mid){
                    count += arr[i]/mid;
                }
            }
            // 조카의 수보다 더 많은 과자를 나누어 줄 수 있다면 과자의 길이를 늘림
            if(count>=m){
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        bw.write(high+"");
        bw.flush();

        bw.close();
        br.close();
    }
}
