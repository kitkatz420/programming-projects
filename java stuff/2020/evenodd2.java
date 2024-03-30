import java.util.Scanner;
public class evenodd2 {
	public static void main(String[] args) {
		Scanner reader = new Scanner(System.in);
		System.out.print("enter a number: ");
		int num = reader.nextInt();
		String evenodd2 = (num % 2 == 0) ? "even":"odd";
		System.out.println(num+" is "+evenodd2);
	}
}