public class fibonacci3 {
	public static void main(String[] args) {
		int n=100, t1=0, t2=1;
		System.out.print("upto "+n+": ");
		while (t1<=n)
		{
			System.out.print(t1+" + ");
			int sum=t1+t2;
			t1=t2;
			t2=sum;
		}
	}
}