package com.rroggia.day1;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;

public class CaptchaSolver {

	public static void main(String[] args) throws IOException {

		try (Scanner scanner = new Scanner(new BufferedReader(new FileReader("./src/com/rroggia/day1/puzzleInput")));) {

			String puzzleInput = scanner.next();

			int firstValue;
			int secondValue;
			int sum = 0;

			for (int i = 0; i < puzzleInput.length(); i++) {
				firstValue = Character.getNumericValue(puzzleInput.charAt(i));
				secondValue = Character.getNumericValue(puzzleInput.charAt(getNextIndex(puzzleInput, i)));

				if (firstValue == secondValue) {
					sum += firstValue;
				}
			}

			System.out.println(sum);

		}
	}

	private static int getNextIndex(String string, int currentIndex) {
		int index = (string.length() / 2) + currentIndex;
		return (index >= string.length()) ? index - string.length() : index;
	}

}
