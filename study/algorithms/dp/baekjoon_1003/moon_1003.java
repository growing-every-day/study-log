import java.io.*;

/**
 * 문제 : 1003번 - 피보나치 함수
 * 메모리 : 16024 KB
 * 시간 : 152 ms
 * */
public class moon_1003 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        // 테스트 케이스의 개수
        int T = Integer.parseInt(br.readLine());

        for(int t=0; t<T; t++){
            int n = Integer.parseInt(br.readLine());

            // 0이면
            if(n==0){
                bw.write("1 0\n");
            // 1이면
            } else if(n==1){
                bw.write("0 1\n");
            // 2이상 이면
            } else {
                // 0의 개수를 나타내는 배열
                int[] zero = new int[n+1];
                // 1의 개수를 나타내는 배열
                int[] one = new int[n+1];

                // n이 0일 때, 0과 1의 개수
                zero[0] = 1; one[0] = 0;
                // n이 1일 때, 0과 1의 개수
                zero[1] = 0; one[1] = 1;

                for(int i=2; i<=n; i++){
                    // i번 인덱스의 값을 구하기 위해 i-2번와 i-1번 인덱스의 값들을 더해서 저장
                    zero[i] = zero[i-2] + zero[i-1];
                    one[i] = one[i-2] + one[i-1];
                }
                // 0과 1의 개수 출력
                bw.write(zero[n]+" "+one[n]+"\n");
            }
        }
        bw.flush();

        bw.close();
        br.close();
    }
}
