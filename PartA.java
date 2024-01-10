public class PartA {
    public static void main(String[] args) {
        int faces= 6;
        int total= faces* faces;
        System.out.println("Total Combinations: " + total);
        String combination[][] = new String[faces][faces];
        for(int i=1;i<=faces;i++)
        {
            for(int j=1;j<=faces;j++)
            {
                combination[i-1][j-1]="("+i+","+j+")";
            }
        }
        System.out.println("Combination Matrix");
        for(int i=0;i<faces;i++)
        {
            for(int j=0;j<faces;j++)
            {
                System.out.print(combination[i][j]+"\t");
            }
            System.out.println();
        }
        int[][] distribution = new int[faces][faces];
        for (int dieA = 1; dieA <= faces; dieA++) {
            for (int dieB = 1; dieB <= faces; dieB++) {
                int sum = dieA + dieB;
                distribution[dieA - 1][dieB - 1] = sum;
            }
        }
        System.out.println("Distribution Matrix:");
        for (int i=0;i<faces;i++) {
            for (int j=0;j<faces;j++) {
                System.out.print(distribution[i][j]+ "\t");
            }
            System.out.println();
        }
        int[] sums= new int[2 * faces+1];
        for (int[] row : distribution) {
            for (int value : row) {
                sums[value]++;
            }
        }
        System.out.println("Probability of Sums:");
        for (int i = 2;i<sums.length; i++) {
            int sum = i;
            double probability = (double)sums[i] / total;
            System.out.printf("P(Sum = %d) = %.4f\n", sum, probability);
        }
    }
}
