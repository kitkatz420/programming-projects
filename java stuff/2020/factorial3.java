public class factorial3 {
	public static void main(String[] args) {
		int num=5, i=1;
		long factorial=1;
		while(i<=num)
		{
			factorial*=i;
			i++;
		}
		System.out.printf("factorial of %d=%d", num, factorial);
	}
}