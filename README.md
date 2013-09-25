secure-psychic-ninja
====================

SnP Project for 2013

Notes on style

Every method should have documentation. This includes

 * @param
 * @return
 * @throws

Each class should have

 * @author

Every time a method is invoked with a constant, should have an inline comment.
An example is provided below.

```java
  someMethod(affectedVariable, 5 /* explain why this parameter is 5 */);
```

No line should be more than 80 characters long.

Bracketing should be as follows:

 * For a construct (e.g. `for`, `if` or `while`) with one instruction in it
 ..* if loop + instruction is less than 80 characters keep it all on one line
 ..* if loop + instruction is more than 80 characters, move instruction onto a
 new line
 * Otherwise bracketing should open the bracket on the same line, and close on a
 separate line

Use a tab-size of 2 spaces and use tabs over spaces.

```java
  /**
    documentation here!
   */
  public int randomSamples(int x, int y) {
    for (int i = 0; i < x; i++) System.out.println(i);

    for (int j = 0; j < y; j++)
      System.out.println("Hello! I am Elder " + j + "! Look at this book!";

    if (x < y) {
      int k = x + y;
      System.out.println("x + y = " + (x + y));
    } else {
      System.out.println(x + " >= " + y);
    }
    return 42;
  }
```
