package rroggia.github.io.day2.opcode;

public abstract class ChangeMemoryBasedOnTwoInputsOpcode implements Opcode {

	protected int operation;
	protected int firstIndexPosition;
	protected int secondIndexPosition;
	protected int storeIndexPosition;

	public ChangeMemoryBasedOnTwoInputsOpcode(int operation, int firstIndexPosition, int secondIndexPosition,
			int storeIndexPosition) {

		this.operation = operation;
		this.firstIndexPosition = firstIndexPosition;
		this.secondIndexPosition = secondIndexPosition;
		this.storeIndexPosition = storeIndexPosition;
	}

	@Override
	public String[] resolve(String[] opcodes) {
		opcodes[storeIndexPosition] = String.valueOf(applyConcreteOperation(opcodes));
		return opcodes;
	}

	public abstract int applyConcreteOperation(String[] opcodes);

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + firstIndexPosition;
		result = prime * result + operation;
		result = prime * result + secondIndexPosition;
		result = prime * result + storeIndexPosition;
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		ChangeMemoryBasedOnTwoInputsOpcode other = (ChangeMemoryBasedOnTwoInputsOpcode) obj;
		if (firstIndexPosition != other.firstIndexPosition)
			return false;
		if (operation != other.operation)
			return false;
		if (secondIndexPosition != other.secondIndexPosition)
			return false;
		if (storeIndexPosition != other.storeIndexPosition)
			return false;
		return true;
	}

}
