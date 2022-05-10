package rroggia.github.io.day1;

import java.util.Arrays;

public class FuelRequirement {
	private Iterable<Module> modules;

	public FuelRequirement(Module... module) {
		modules = Arrays.asList(module);
	}

	public FuelRequirement(Iterable<Module> modules) {
		this.modules = modules;
	}

	public int calculateFuelRequirement() {
		int fuelRequirement = 0;
		for (var module : modules) {
			fuelRequirement += module.determineFuelRequiredToLaunch();
		}
		return fuelRequirement;
	}

}
