package rroggia.github.io.day2;

import java.io.IOException;
import java.nio.file.FileSystems;
import java.nio.file.Files;
import java.util.Arrays;

public class Day2 {
	private static final String RESOURCES_FOLDER = "src/main/resources";

	public static void main(String[] args) {

		try {
			var path = FileSystems.getDefault().getPath(RESOURCES_FOLDER, "day2.txt");
			var opcodes = Files.readString(path);

			String result = null;
			for (int noun = 0; noun <= 99; noun++) {
				for (int verb = 0; verb <= 99; verb++) {
					String[] split = opcodes.split(",");

					split[1] = String.valueOf(noun);
					split[2] = String.valueOf(verb);
					var changedOpcodes = String.join(",", Arrays.asList(split));

					var opcodeReader = new OpcodeRunner(changedOpcodes);
					opcodeReader.resolveAllOpcodes();

					String opcodeCurrentState = opcodeReader.getOpcodeCurrentState();
					String[] results = opcodeCurrentState.split(",");
					result = results[0];

					if ("19690720".equals(result)) {
						System.out.println(100 * noun + verb);
						noun = 100;
						break;
					}
				}
			}

		} catch (IOException e) {
			System.out.println("Error reading the day2.txt file.");
		}

	}

}
