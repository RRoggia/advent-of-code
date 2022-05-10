package rroggia.github.io.day3;

import java.util.HashMap;
import java.util.Map;

public class GridIntersectionDeterminer {

	private static final GridIntersectionDeterminer INSTANCE = new GridIntersectionDeterminer();

	private GridIntersectionDeterminer() {

	}

	public static GridIntersectionDeterminer getInstance() {
		return INSTANCE;
	}

	public Map<String, String> determineIntersections(Map<String, Integer> firstConections,
			Map<String, Integer> secondConections) {
		var intersections = new HashMap<String, String>();
		for (String key : firstConections.keySet()) {
			if (secondConections.containsKey(key)) {
				intersections.put(key, firstConections.get(key) + "," + secondConections.get(key));
			}
		}
		return intersections;
	}

}
