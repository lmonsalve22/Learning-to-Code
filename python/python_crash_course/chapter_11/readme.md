# Some notes about the chapter

- A **unit test** verifies that one specific aspect of a function's behavior is correct
- A **test case** is a collection of unit tests that together prove that a function behaves as it's supposed to, within the full range of situations you expect it to handle.

<center>

|        **Method**         |              **Use**              |
| :-----------------------: | :-------------------------------: |
|     assertEqual(a, b)     |        Verify that a == b         |
|    assertNoEqual(a, b)    |        Verify that a != b         |
|       assertTrue(x)       |       Verify that x is True       |
|      assertFalse(x)       |      Verify that x is False       |
|  assertIn(item, *list*)   |   Verify that item is in *list*   |
| assertNotIn(item, *list*) | Verify that item is not in *list* |

</center>

- Exercise **11-1** and **11-2** are included in `city_functions.py` and `test_cities.py`
- Exercise **11-3** is included in `test_employee.py` and `employee_functions.py`