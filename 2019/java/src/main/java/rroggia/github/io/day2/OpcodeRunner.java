package rroggia.github.io.day2;

import static rroggia.github.io.day2.Operation.ADD;
import static rroggia.github.io.day2.Operation.HALT;
import static rroggia.github.io.day2.Operation.MULTIPLIER;

import rroggia.github.io.day2.opcode.AddOpcode;
import rroggia.github.io.day2.opcode.HaltOpcode;
import rroggia.github.io.day2.opcode.MultiplierOpcode;
import rroggia.github.io.day2.opcode.Opcode;

public class OpcodeRunner {

	private int instructionPointer = 0;
	private String[] opcodes;

	public OpcodeRunner(String opcodes) {
		this.opcodes = opcodes.split(",");
	}

	public Opcode getNextOpcode() {

		String operation = opcodes[instructionPointer];

		if (HALT.getCode().equals(operation)) {
			return new HaltOpcode();
		}

		var firstInstructionParameter = Integer.parseInt(opcodes[instructionPointer + 1]);
		var secondInstructionParameter = Integer.parseInt(opcodes[instructionPointer + 2]);
		var storeInstructionParameter = Integer.parseInt(opcodes[instructionPointer + 3]);

		if (ADD.getCode().equals(operation)) {
			return new AddOpcode(firstInstructionParameter, secondInstructionParameter, storeInstructionParameter);
		} else if (MULTIPLIER.getCode().equals(operation)) {
			return new MultiplierOpcode(firstInstructionParameter, secondInstructionParameter,
					storeInstructionParameter);
		}

		throw new RuntimeException("Could not identify operation.");
	}

	public void resolveNextOpcode() {
		Opcode nextOpcode = this.getNextOpcode();

		if (!isHaltOpcode(nextOpcode)) {
			instructionPointer += 4;
		}

		nextOpcode.resolve(opcodes);
	}

	public boolean nextIsHaltOpcode() {
		return isHaltOpcode(this.getNextOpcode());
	}

	public boolean isHaltOpcode(Opcode opcode) {
		return HALT == opcode.getOperation();
	}

	public void resolveAllOpcodes() {
		while (!nextIsHaltOpcode()) {
			resolveNextOpcode();
		}
	}

	public String getOpcodeCurrentState() {
		String opcodeCurrentState = "";
		for (var opcode : opcodes) {
			opcodeCurrentState += opcode + ",";
		}
		return opcodeCurrentState.substring(0, opcodeCurrentState.length() - 1);
	}

}
