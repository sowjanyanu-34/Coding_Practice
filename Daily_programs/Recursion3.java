public class Recursion3 {
    public static int calcfact(int n){
        if (n == 1||n == 0){
        return 1;
    }
    int fact=calcfact(n-1);
    int fact1= n * fact;
    return fact1;
}
    public static void main(String args[])
    {
        int n=5;
        int ans=calcfact(n);
        System.out.println(ans);
    }
}
