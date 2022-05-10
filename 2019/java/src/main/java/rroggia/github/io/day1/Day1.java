package rroggia.github.io.day1;

import java.io.IOException;
import java.nio.file.FileSystems;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.HashSet;
import java.util.List;

public class Day1 {

	private static final String RESOURCES_FOLDER = "src/main/resources";

	public static void main(String[] args) {

		try {
			Path path = FileSystems.getDefault().getPath(RESOURCES_FOLDER, "day1.txt");
			List<String> massesOfModules = Files.readAllLines(path);

			var modules = new HashSet<Module>();
			for (var mass : massesOfModules) {
				modules.add(new Module(Integer.parseInt(mass)));
			}

			var fuelRequirement = new FuelRequirement(modules);
			System.out.println(fuelRequirement.calculateFuelRequirement());

		} catch (IOException e) {
			System.out.println("Error reading the day1.txt file.");
		}

	}
}
