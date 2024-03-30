public class swapnumbers2 {
	public static void main(String[] args) {
		float first=12.0f, second=24.5f;
		System.out.println("--before swap--");
		System.out.println("first number = "+first);
		System.out.println("sceond number = "+second);
		first=first-second;
		second=first+second;
		first=second-first;
		System.out.println("--after swap--");
		System.out.println("first number = "+first);
		System.out.println("second number = "+second);
	}
}