package rroggia.github.io.day3;

import java.io.IOException;
import java.nio.file.FileSystems;
import java.nio.file.Files;

public class Day3 {

	private static final String RESOURCES_FOLDER = "src/main/resources";

	public static void main(String[] args) {

		try {
			var path = FileSystems.getDefault().getPath(RESOURCES_FOLDER, "day3.txt");
			var wireTraces = Files.readAllLines(path);

			var conectionDeterminer = GridConnectionDeterminer.getInstance();

			var firstWireGridConnections = conectionDeterminer.determineConnections(wireTraces.get(0));
			var secondWireGridConnections = conectionDeterminer.determineConnections(wireTraces.get(1));

			var intersectionDeterminer = GridIntersectionDeterminer.getInstance();
			var intersections = intersectionDeterminer.determineIntersections(firstWireGridConnections,
					secondWireGridConnections);

			System.out.println(ClosestPointCalculator.getInstance().calculate(intersections));

		} catch (IOException e) {
			System.out.println("Error while reading the input file;");
		}
	}

}
