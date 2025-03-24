import java.util.*;

public class automata {

	// DFA Implementation
	public static boolean runDFA(String input) {
		String currentState = "q0";
		for (char ch : input.toCharArray()) {
			switch (currentState) {
			case "q0":
				currentState = (ch == 'a') ? "q1" : "q3";
				break;
			case "q1":
				currentState = (ch == 'b') ? "q2" : "q3";
				break;
			case "q2":
				currentState = (ch == 'a' || ch == 'b') ? "q2" : "q3";
				break;
			case "q3":
				currentState = (ch == 'a' || ch == 'b') ? "q3" : "q3";
				break;
			}
		}
		return currentState.equals("q2");
	}

	// NFA Implementation
	public static boolean runNFA(String input) {
		Set<String> currentStates = new HashSet<>();
		currentStates.add("q0");

		for (char ch : input.toCharArray()) {
			Set<String> nextStates = new HashSet<>();

			for (String state : currentStates) {
				switch (state) {
				case "q0":
					if (ch == '0') nextStates.addAll(Arrays.asList("q0", "q1"));
					if (ch == '1') nextStates.addAll(Arrays.asList("q0", "q2"));
					break;
				case "q1":
					if (ch == '0') nextStates.add("q3");
					break;
				case "q2":
					if (ch == '1') nextStates.add("q3");
					break;
				case "q3":
					if (ch == '0' || ch == '1') nextStates.add("q3");
					break;
				}
			}
			currentStates = nextStates;
		}
		return currentStates.contains("q3");
	}


	// Mealy Machine Implementation
	public static String runMealy(String input) {
		String currentState = "A";
		StringBuilder output = new StringBuilder();

		System.out.println("Input \t Output");

		for (char ch : input.toCharArray()) {
			char out = ' '; // Store the output

			switch (currentState) {
			case "A":
				if (ch == '0') {
					currentState = "D";
					out = '0';
				}
				else {
					currentState = "B";
					out = '0';
				}
				break;
			case "B":
				if (ch == '0') {
					currentState = "A";
					out = '1';
				}
				else {
					currentState = "D";
					out = '0';
				}
				break;
			case "C":
				if (ch == '0') {
					currentState = "B";
					out = '1';
				}
				else {
					currentState = "A";
					out = '1';
				}
				break;
			case "D":
				if (ch == '0') {
					currentState = "D";
					out = '1';
				}
				else {
					currentState = "C";
					out = '0';
				}
				break;
			}

			output.append(out);
			System.out.println(ch + "\t" + out);
		}

		return output.toString();
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// Test DFA
		
		System.out.println("Enter input for DFA:");
		String dfaInput = sc.nextLine();
		System.out.println("DFA Result: " + (runDFA(dfaInput) ? "Accepted" : "Rejected"));
	
		// Test NFA
	
		System.out.println("Enter input for NFA:");
		String nfaInput = sc.nextLine();
		System.out.println("NFA Result: " + (runNFA(nfaInput) ? "Accepted" : "Rejected"));
		 
		// Test Mealy Machine
		System.out.println("Enter input for Mealy Machine:");
		String mealyInput = sc.nextLine();
		System.out.println("Mealy Output: " + runMealy(mealyInput));

		sc.close();
	}
}
