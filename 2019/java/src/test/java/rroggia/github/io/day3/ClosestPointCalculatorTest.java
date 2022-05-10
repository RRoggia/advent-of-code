package rroggia.github.io.day3;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.Map;

import org.junit.jupiter.api.Test;

public class ClosestPointCalculatorTest {

	@Test
	public void calculateWithAbsoluteNumber() {
		var intersections = Map.of("10,24", "34,34", "-10,-24", "34,34", "10,-24", "34,34", "-10,24", "34,34");
		int closestPoint = ClosestPointCalculator.getInstance().calculate(intersections);
		assertEquals(68, closestPoint);
	}

	@Test
	public void calculateClosestPoint() {
		var intersections = Map.of("-1,60", "61,61", "1,3", "4,4", "50,50", "50,50");
		int closestPoint = ClosestPointCalculator.getInstance().calculate(intersections);
		assertEquals(8, closestPoint);
	}

}
