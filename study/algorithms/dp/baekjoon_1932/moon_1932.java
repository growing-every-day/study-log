import java.io.*;
import java.util.*;

/**
 * 문제 : 1932번 - 정수 삼각형
 * 메모리 : 26580 KB
 * 시간 : 288 ms
 * */
public class moon_1932 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        // 삼각형의 크기
        int n = Integer.parseInt(br.readLine());

        int[][] arr = new int[n][n];

        // 정수 삼각형 입력
        for(int i=0; i<n; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j=0; j<i+1; j++){
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // 맨 마지막 층-1번째 부터 계산
        for(int i=n-2; i>=0; i--){
            for(int j=0; j<i+1; j++){
                // 현재 층에서 바로 아래층에 있는 값과 아래층 옆에 있는 값 중에서 큰 값을 더함
                arr[i][j] += Math.max(arr[i+1][j], arr[i+1][j+1]);
            }
        }

        // 첫 번째 층 출력
        bw.write(arr[0][0]+"");
        bw.flush();

        bw.close();
        br.close();
    }
}
