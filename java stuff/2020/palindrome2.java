public class palindrome2 {
	public static void main(String[] args) {
		int num=11221, reversedInteger=0, remainder, originalInteger;
		originalInteger=num;
		for(;num!=0; num/=10)
		{
			remainder=num%10;
			reversedInteger=reversedInteger*10+remainder;
			
		}
		if (originalInteger==reversedInteger)
			System.out.println(originalInteger+" is a palindrome");
		else
			System.out.println(originalInteger+" is not a palindrome");
	}
}