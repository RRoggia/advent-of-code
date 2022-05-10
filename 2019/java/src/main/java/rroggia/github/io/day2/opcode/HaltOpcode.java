package rroggia.github.io.day2.opcode;

import rroggia.github.io.day2.Operation;

public class HaltOpcode implements Opcode {

	@Override
	public String[] resolve(String[] opcodes) {
		return opcodes;
	}

	@Override
	public Operation getOperation() {
		return Operation.HALT;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;

		return Operation.HALT == ((HaltOpcode) obj).getOperation();
	}

}
