package rroggia.github.io.day3;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

public class GridConnectionDeterminerTest {

	private static final GridConnectionDeterminer GRID = GridConnectionDeterminer.getInstance();

	@Test
	public void determineUpConnections() {
		String lastExpectedPosition = "0,10";

		var gridConnections = GRID.determineConnections("U10");

		assertEquals(10, gridConnections.size());

		boolean containsKey = gridConnections.containsKey(lastExpectedPosition);
		assertTrue(containsKey);

		Integer steps = gridConnections.get(lastExpectedPosition);
		assertEquals(10, steps);
	}

	@Test
	public void determineDownConnections() {
		String lastExpectedPosition = "0,-10";

		var gridConnections = GRID.determineConnections("D10");

		assertEquals(10, gridConnections.size());

		boolean containsKey = gridConnections.containsKey(lastExpectedPosition);
		assertTrue(containsKey);

		Integer steps = gridConnections.get(lastExpectedPosition);
		assertEquals(10, steps);
	}

	@Test
	public void determineRightConnections() {
		String lastExpectedPosition = "10,0";

		var gridConnections = GRID.determineConnections("R10");

		assertEquals(10, gridConnections.size());

		boolean containsKey = gridConnections.containsKey(lastExpectedPosition);
		assertTrue(containsKey);

		Integer steps = gridConnections.get(lastExpectedPosition);
		assertEquals(10, steps);
	}

	@Test
	public void determineLeftConnections() {
		String lastExpectedPosition = "-10,0";

		var gridConnections = GRID.determineConnections("L10");

		assertEquals(10, gridConnections.size());

		boolean containsKey = gridConnections.containsKey(lastExpectedPosition);
		assertTrue(containsKey);

		Integer steps = gridConnections.get(lastExpectedPosition);
		assertEquals(10, steps);
	}

	@Test
	public void determineExampleConnection() {
		String lastExpectedPosition = "145,11";

		var gridConnections = GRID.determineConnections("R75,D30,R83,U83,L12,D49,R71,U7,L72");

		boolean containsKey = gridConnections.containsKey(lastExpectedPosition);
		assertTrue(containsKey);

		Integer steps = gridConnections.get(lastExpectedPosition);
		assertEquals(482, steps);
	}

	@Test
	public void determineStepsSamePositionConnection() {
		String lastExpectedPosition = "2,0";

		var gridConnections = GRID.determineConnections("R2,L1,R1");

		boolean containsKey = gridConnections.containsKey(lastExpectedPosition);
		assertTrue(containsKey);

		Integer steps = gridConnections.get(lastExpectedPosition);
		assertEquals(2, steps);
	}

	@Test
	public void determineWrongInvalidWireTraces() {
		assertThrows(RuntimeException.class, () -> GRID.determineConnections("X10"));

	}
}
