import java.io.*;
import java.util.StringTokenizer;

/**
 * 문제 : 12015번 - 가장 긴 증가하는 부분 수열 2
 * 메모리 : 96268 KB
 * 시간 : 556 ms
 * */
public class moon_12015 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        // 수열의 크기
        int n = Integer.parseInt(br.readLine());

        int[] arr = new int[n];

        // 수열 입력{10, 20, 30, 15, 20, 30, 50, 40, 45 ,60}
        // {10, 15, 20, 30, 40, 45, 60}
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0; i<n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        // 부분 수열들을 저장할 배열
        int[] seq = new int[n];
        // 초기 상태
        seq[0] = arr[0];

        // 수열의 길이
        int length = 1;

        for(int i=1; i<n; i++){
            int value = arr[i];

            // 부분 수열의 가장 마지막 값보다 크다면
            if(seq[length-1] < value){
                length++;
                seq[length-1] = value;
            } else {
                // 이분 탐색
                int low = 0;
                int high = length;

                while(low < high){
                    int mid = (low+high) / 2;

                    // seq의 중간 값보다 크다면
                    if(seq[mid] < value){
                        low = mid + 1;
                    } else {
                        high = mid;
                    }
                }

                // low 인덱스가 바꿀 원소의 위치가 되어 value 값으로 바꿔준다.
                seq[low] = value;
            }
        }

        bw.write(length+"");
        bw.flush();

        bw.close();
        br.close();
    }
}
