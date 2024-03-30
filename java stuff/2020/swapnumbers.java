public class swapnumbers {
	public static void main(String[ ]args) {
		float first=1.20f, second=2.45f;
		System.out.println("--before swap--");
		System.out.println("first number = " +first);
		System.out.println("second number = " + second);
		float temporary = first;
		first=second;
		second=temporary;
		System.out.println("--after swap--");
		System.out.println("first number = "+first);
		System.out.println("second number = "+second);
	}
}