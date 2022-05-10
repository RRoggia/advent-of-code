package rroggia.github.io.day2;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

import rroggia.github.io.day2.opcode.AddOpcode;
import rroggia.github.io.day2.opcode.HaltOpcode;
import rroggia.github.io.day2.opcode.MultiplierOpcode;
import rroggia.github.io.day2.opcode.Opcode;

public class OpcodeReaderTest {

	private static final String ORIGINAL_OPCODE = "1,9,10,3,2,3,11,0,99,30,40,50";
	private static final String ADD_OPCODE = "1,9,10,3";
	private static final String HALT_OPCODE = "99";
	private static final String MULTIPLIER_OPCODE = "2,3,11,0";
	private static final String FIRST_OPCODE_RESOLVED = "1,9,10,70,2,3,11,0,99,30,40,50";
	private static final String ALL_OPCODES_RESOLVED = "3500,9,10,70,2,3,11,0,99,30,40,50";

	@Test
	public void getNextAddOpcode() {
		var opcodeReader = new OpcodeRunner(ADD_OPCODE);
		Opcode nextOpcode = opcodeReader.getNextOpcode();
		var expectedAddOpcode = new AddOpcode(9, 10, 3);
		assertEquals(expectedAddOpcode, nextOpcode);
	}

	@Test
	public void getNextMultiplierOpcode() {
		var opcodeReader = new OpcodeRunner(MULTIPLIER_OPCODE);
		Opcode nextOpcode = opcodeReader.getNextOpcode();
		var expectedMultiplierOpcode = new MultiplierOpcode(3, 11, 0);
		assertEquals(expectedMultiplierOpcode, nextOpcode);
	}

	@Test
	public void getNextHaltOpcode() {
		var opcodeReader = new OpcodeRunner(HALT_OPCODE);
		Opcode nextOpcode = opcodeReader.getNextOpcode();
		var expectedHaltOpcode = new HaltOpcode();
		assertEquals(expectedHaltOpcode, nextOpcode);
	}

	@Test
	public void getNextAfterResolvingOpcode() {
		var opcodeReader = new OpcodeRunner(ORIGINAL_OPCODE);
		opcodeReader.resolveNextOpcode();
		Opcode opcode = opcodeReader.getNextOpcode();
		var expectedOpcode = new MultiplierOpcode(3, 11, 0);
		assertEquals(expectedOpcode, opcode);
	}

	@Test
	public void readUntilHalt() {
		var opcodeReader = new OpcodeRunner(ORIGINAL_OPCODE);
		// read several times to ensure the index is not passing the halt opcode. 
		opcodeReader.resolveNextOpcode();
		opcodeReader.resolveNextOpcode();
		opcodeReader.resolveNextOpcode();
		opcodeReader.resolveNextOpcode();
		opcodeReader.resolveNextOpcode();
		Opcode opcode = opcodeReader.getNextOpcode();
		var haltOpcode = new HaltOpcode();
		assertEquals(haltOpcode, opcode);
	}

	@Test
	public void resolveAddOpcode() {
		var opcodeReader = new OpcodeRunner(ORIGINAL_OPCODE);
		opcodeReader.resolveNextOpcode();
		assertEquals(FIRST_OPCODE_RESOLVED, opcodeReader.getOpcodeCurrentState());
	}

	@Test
	public void resolveMultiplyOpcode() {
		var opcodeReader = new OpcodeRunner(ORIGINAL_OPCODE);
		opcodeReader.resolveNextOpcode();
		opcodeReader.resolveNextOpcode();
		assertEquals(ALL_OPCODES_RESOLVED, opcodeReader.getOpcodeCurrentState());
	}

	@Test
	public void resolveHaltOpcode() {
		var opcodeReader = new OpcodeRunner(ORIGINAL_OPCODE);
		opcodeReader.resolveNextOpcode();
		opcodeReader.resolveNextOpcode();
		opcodeReader.resolveNextOpcode();
		assertEquals(ALL_OPCODES_RESOLVED, opcodeReader.getOpcodeCurrentState());
	}

	@Test
	public void resolveAllOpcodes() {
		var opcodeReader = new OpcodeRunner(ORIGINAL_OPCODE);
		opcodeReader.resolveAllOpcodes();
		assertEquals(ALL_OPCODES_RESOLVED, opcodeReader.getOpcodeCurrentState());
	}

}
