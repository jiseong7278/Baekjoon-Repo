import java.io.*;
import java.util.*;


public class Main {

    static int N, M, R;
    static int[] count;
    static boolean[] visited;
    static ArrayList<Integer>[] list;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());

        count = new int[N+1];
        visited = new boolean[N+1];
        list = new ArrayList[N+1];

        for (int i=0; i<=N; i++){
            list[i] = new ArrayList<>();
        }

        for (int i=0; i<M; i++){
            st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            list[a].add(b);
            list[b].add(a);
        }

        for (List<Integer> l: list){
            l.sort(Collections.reverseOrder());
        }

        BFS(R);

        for (int i=1; i<count.length; i++){
            System.out.println(count[i]);
        }
    }

    static void BFS(int r){
        Queue<Integer> queue = new LinkedList<>();
        queue.add(r);
        visited[r] = true;

        int cnt = 1;

        while(!queue.isEmpty()){
            int curIndex = queue.poll();

            count[curIndex] = cnt++;

            for(int l: list[curIndex]){
                if(visited[l]){
                    continue;
                }
                queue.add(l);
                visited[l] = true;
                count[l] = cnt;
            }
        }
    }
}