package rroggia.github.io.day2.opcode;

import rroggia.github.io.day2.Operation;

public interface Opcode {

	String[] resolve(String[] opcodes);

	Operation getOperation();

}