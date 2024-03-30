import java.util.Scanner;
public class print1 {
	public static void main(String[] args) {
		Scanner reader=new Scanner(System.in);
		System.out.print("enter a number: ");
		int number=reader.nextInt();
		System.out.println("you entered: "+number);
	}
}