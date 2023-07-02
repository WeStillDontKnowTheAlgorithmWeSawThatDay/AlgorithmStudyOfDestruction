
import java.io.*;
import java.util.*;

public class Main {

	static List<int[]> brackets;
	static Set<String> result;
	static boolean[] check;
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String line = br.readLine();

		brackets = new ArrayList<>();
		Stack<Integer> s = new Stack<>();
		for(int i=0; i<line.length(); i++) {
			char c = line.charAt(i);
			if(c == '(') {
				s.push(i);
			}else if(c == ')'){
				brackets.add(new int[] {s.pop(), i});
			}
		}

		check = new boolean[line.length()];
		result = new TreeSet<>();
		comb(0, line.toCharArray());

		result.stream().forEach(System.out::println);
	}

	static void comb(int depth, char[] str) {
		if(depth == brackets.size()) {
			boolean f = false;
			StringBuilder sb = new StringBuilder();
			for(int i=0; i<str.length; i++) {
				if(!check[i]) {
					sb.append(str[i]);
				} else f = true;
			}
			if(f) {
				result.add(sb.toString());
			}
			return;
		}

		comb(depth+1, str);

		int[] bracket = brackets.get(depth);
		check[bracket[0]] = true;
		check[bracket[1]] = true;
		comb(depth+1, str);
		check[bracket[0]] = false;
		check[bracket[1]] = false;
	}
}
