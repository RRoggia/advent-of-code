package rroggia.github.io.day2;

public enum Operation {

	ADD("1"), MULTIPLIER("2"), HALT("99");

	private final String code;

	Operation(String code) {
		this.code = code;
	}

	public String getCode() {
		return this.code;
	}

}
