public class power2 {
	public static void main(String[] args) {
		int base=3, exponent=4;
		long result=1;
		for(;exponent!=0; --exponent)
		{
			result*=base;
		}
		System.out.println("answer = "+result);
	}
}