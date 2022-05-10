package rroggia.github.io.day3;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.Map;

import org.junit.jupiter.api.Test;

public class GridIntersectionDeterminerTest {

	private static final GridIntersectionDeterminer GRID = GridIntersectionDeterminer.getInstance();

	@Test
	public void determineIntersection() {
		var firstWireConnections = Map.of("0,0", 0);
		var secondWireConnections = Map.of("0,0", 0);

		var intersections = GRID.determineIntersections(firstWireConnections, secondWireConnections);
		assertEquals(1, intersections.size());
	}

	@Test
	public void multipleIntersections() {
		var firstWireConnections = Map.of("0,0", 0, "1,0", 1, "2,0", 2, "3,0", 3, "4,0", 4, "5,0", 5, "6,0", 6, "7,0",
				7);
		var secondWireConnections = Map.of("0,0", 0, "1,0", 1, "2,0", 2, "3,0", 3, "4,0", 4, "5,0", 5);

		var intersections = GRID.determineIntersections(firstWireConnections, secondWireConnections);
		assertEquals(6, intersections.size());
	}

	@Test
	public void determineIntersectionExample() {
		var firstConnections = GridConnectionDeterminer.getInstance().determineConnections("R8,U5,L5,D3");
		var secondConnections = GridConnectionDeterminer.getInstance().determineConnections("U7,R6,D4,L4");

		var intersections = GRID.determineIntersections(firstConnections, secondConnections);
		assertEquals(2, intersections.size());

	}

}
