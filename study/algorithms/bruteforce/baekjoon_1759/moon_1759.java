import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

/**
 * 문제 : 1759번 - 암호 만들기
 * 메모리 : 14204 KB
 * 시간 : 128 ms
 * */
public class moon_1759 {
    private static int l, c;
    private static char[] ch, temp;
    private static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        // 만들어야 될 암호 문자 개수와 주어지는 알파벳 개수 입력
        StringTokenizer st = new StringTokenizer(br.readLine());
        l = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        ch = new char[c];
        temp = new char[l];

        // 알파벳 입력
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<c; i++)
            ch[i] = st.nextToken().charAt(0);

        // 오름차순 정렬
        Arrays.sort(ch);

        backtracking(0 , 0);

        bw.write(sb.toString());
        bw.flush();

        bw.close();
        br.close();
    }

    public static void backtracking(int depth, int start){
        // 만들어야 될 문자의 개수가 완성됐다면
        if(depth==l){
            // 그 문자의 모음과 자음 개수 확인
            if(check()) {
                for (char c : temp) {
                    sb.append(c);
                }
                sb.append('\n');
            }
            return;
        }

        for(int i=start; i<c; i++){
            temp[depth] = ch[i];
            backtracking(depth+1, i+1);
        }
    }

    // 모음, 자음 개수 확인
    public static boolean check() {
        int vow = 0, con = 0; // 모음, 자음 개수

        for(int i=0; i<temp.length; i++){
            char c = temp[i];

            if(c=='a' || c=='e' || c=='i' || c=='o' || c=='u')
                vow++;
            else
                con++;
        }

        if(vow>=1 && con>=2)
            return true;

        return false;
    }
}
