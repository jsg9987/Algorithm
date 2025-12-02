import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    
    static class Country implements Comparable<Country> {
        int id;
        int gold;
        int silver;
        int bronze;

        public Country(int id, int gold, int silver, int bronze) {
            this.id = id;
            this.gold = gold;
            this.silver = silver;
            this.bronze = bronze;
        }

        @Override
        public int compareTo(Country other) {
            if (this.gold != other.gold) {
                return other.gold - this.gold;
            }
            if (this.silver != other.silver) {
                return other.silver - this.silver;
            }
            return other.bronze - this.bronze;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        Country[] countries = new Country[N];
        
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int id = Integer.parseInt(st.nextToken());
            int gold = Integer.parseInt(st.nextToken());
            int silver = Integer.parseInt(st.nextToken());
            int bronze = Integer.parseInt(st.nextToken());
            countries[i] = new Country(id, gold, silver, bronze);
        }

        Arrays.sort(countries);

        int targetRank = 1;
        
        for (int i = 0; i < N; i++) {
            int currentRank = i + 1;
            
            if (countries[i].id == K) {
                targetRank = currentRank;
                
                if (i > 0) {
                    Country current = countries[i];
                    Country prev = countries[i-1];
                    
                    if (current.gold == prev.gold && 
                        current.silver == prev.silver && 
                        current.bronze == prev.bronze) {
                        
                        targetRank = i;
                    }
                }
                
                break;
            }
        }
        
        System.out.println(targetRank);
    }
}