Secure ninja Psychic
====================

SnP Project for 2013

Style Guidelines
----------------

Every method should have documentation with the following:

 * @param
 * @return
 * @throws

Each class should have:

 * @author

Embedded constants should be avoided. A class constant should be preferred, but otherwise, an inline comment should be attached.
An example is provided below.

```java
  someMethod(affectedVariable, 5 /* explain why this parameter is 5 */);
```

Lines should be longer than 100 characters long.

Bracketing should be as follows:

 * All constructs (e.g. `for`, `if` or `while`) should have brackets
 * Brackets should be opened on the same line, and closed on a line by itself

Tab indentation should be used with a tab width of 4.
Alignment should still be done with spaces.

```java
	/**
	* Documentation here!
	*/
	public int randomSamples(int x, int y) {
		for (int i = 0; i < x; i++) {
			System.out.println(i);
		}

		for (int j = 0; j < y; j++) {
			System.out.println("Hello! I am Elder " + j + "! Look at this book!");
		}

		if (x < y) {
			int k = x + y;
			System.out.println("x + y = " + (x + y));
		}
		else {
			System.out.println(x + " >= " + y);
		}
		return 42;
	}
```


