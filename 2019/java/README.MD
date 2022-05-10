# DAY 1

* [readAllLines](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/nio/file/Files.html)
* using `var`:
    * `var` uses the implementation not interfaces (for example for a Set and HashSet)
* [FileSytem.getDefaults()](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/nio/file/FileSystems.html)
* using `Math.floorDiv` or not using it
* junit 5
* usage of `varargs` and `Iterable`

# DAY 2
* applied tdd
* create a whole framework to try to avoid changes to the code structure to ease second part
    * second part was a part that i didn't covered in the framework, had to change the code anyways . lol

# DAY 3
* tests after
* refactoring techniques
    * make the private static public
    * add test consuming it
    * create a wrapper class that calls the public static
    * move the public static to the wrapper class
    * remove any missing implmentation from the initial class.
* back and forth from stateles and stateful `GridConnectionDeterminer`
* testing exception junit 5
* `Map.of`, `Set.of`
* heavy usage of var