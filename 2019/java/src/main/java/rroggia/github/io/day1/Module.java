package rroggia.github.io.day1;

public class Module {

	private int mass;

	public Module(int mass) {
		this.mass = mass;
	}

	public int determineFuelRequiredToLaunch() {
		int fuel = (mass / 3) - 2;
		return (fuel <= 0) ? 0 : fuel + new Module(fuel).determineFuelRequiredToLaunch();

	}

}
