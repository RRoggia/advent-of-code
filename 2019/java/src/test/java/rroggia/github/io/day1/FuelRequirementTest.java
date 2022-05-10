package rroggia.github.io.day1;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class FuelRequirementTest {

	@Test
	public void calculateFuelForOneModule() {
		var calculator = new FuelRequirement(new Module(12));
		assertEquals(2, calculator.calculateFuelRequirement());
	}

	@Test
	public void calculateFuelForMoreThanOneModule() {
		var calculator = new FuelRequirement(new Module(12), new Module(14), new Module(1969),
				new Module(100756));

		assertEquals(51316, calculator.calculateFuelRequirement());
	}

}
