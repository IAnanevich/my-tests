def add(a: int, b: int) -> int or str:
    if type(a) != int or type(b) != int:
        return "Bad value"
    return a + b
