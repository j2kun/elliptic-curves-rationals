def test(expected, actual, epsilon=0.0000001):
   if isinstance(expected, float) and isinstance(actual, float) and abs(expected-actual) < epsilon:
      return

   if expected != actual:
      import sys, traceback
      (filename, lineno, container, code) = traceback.extract_stack()[-2]
      print("Test: %r failed on line %d in file %r.\nExpected %r but got %r\n" %
         (code, lineno, filename, expected, actual))

