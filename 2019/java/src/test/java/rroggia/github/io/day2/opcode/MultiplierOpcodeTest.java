package rroggia.github.io.day2.opcode;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;

import org.junit.jupiter.api.Test;

import rroggia.github.io.day2.opcode.MultiplierOpcode;

public class MultiplierOpcodeTest {

	@Test
	public void simpleMultiplication() {
		var multiplier = new MultiplierOpcode(1, 2, 1);
		String[] opcodes = { "2", "1", "2", "1" };
		String[] resolvedOpcode = multiplier.resolve(opcodes);

		String[] expectedResult = { "2", "2", "2", "1" };
		assertArrayEquals(expectedResult, resolvedOpcode);
	}
}
