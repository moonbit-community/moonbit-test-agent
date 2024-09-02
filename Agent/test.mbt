```moonbit
pub fn hello() -> String {
  "nihao!"
}

test "hello" {
  if hello() != "nihao!" {
    raise "hello() != \"nihao!\""
  }
}

pub fn fib(n : Int) -> Int {
  match n {
    0 => 0
    1 => 1
    _ => fib(n - 1) + fib(n - 2)
  }
}

fn assert_eq[T: Show + Eq](lhs: T, rhs: T) -> Unit {
  if lhs != rhs {
    abort("assert_eq failed.\n    lhs: \(lhs)\n    rhs: \(rhs)")
  }
}

test {
  assert_eq(fib(1), 1)
  assert_eq(fib(2), 1)
  assert_eq(fib(3), 2)
  assert_eq(fib(4), 3)
  assert_eq(fib(5), 5)
}

pub fn fib2(num : Int) -> Int {
  fn aux(n, acc1, acc2) {
    match n {
      0 => acc1
      1 => acc2
      _ => aux(n - 1, acc2, acc1 + acc2)
    }
  }

  aux(num, 0, 1)
}

test {
  assert_eq(fib(1), 1)
  assert_eq(fib2(2), 1)
  assert_eq(fib(3), 2)
  assert_eq(fib2(4), 3)
  assert_eq(fib(5), 5)
}
```
