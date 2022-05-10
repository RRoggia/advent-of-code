package rroggia.github.io.day2.opcode;

import rroggia.github.io.day2.Operation;

public class AddOpcode extends ChangeMemoryBasedOnTwoInputsOpcode {

	public AddOpcode(int firstIndexPosition, int secondIndexPosition, int storeIndexPosition) {
		super(1, firstIndexPosition, secondIndexPosition, storeIndexPosition);
	}

	@Override
	public int applyConcreteOperation(String[] opcodes) {
		return Integer.parseInt(opcodes[firstIndexPosition]) + Integer.parseInt(opcodes[secondIndexPosition]);
	}

	@Override
	public Operation getOperation() {
		return Operation.ADD;
	}

}
