from typing import (
    List, Tuple, Set, Dict, Union, Optional,
    Any, Callable, Iterable, Literal
)

# ---------- BASIC TYPES ----------
age: int = 21
price: float = 99.99
name: str = "Harry"
is_active: bool = True

# ---------- NONE TYPE ----------
result: None = None

# ---------- LIST ----------
numbers: List[int] = [1, 2, 3, 4]
names: List[str] = ["Alice", "Bob"]

# ---------- TUPLE ----------
point: Tuple[int, int] = (10, 20)
person: Tuple[str, int, bool] = ("Harry", 21, True)

# ---------- SET ----------
unique_ids: Set[int] = {1, 2, 3}
unique_ids1: Set[str] = {"Sumit","Sohini","Susmita"}


# ---------- DICTIONARY ----------
student: Dict[str, Union[str, int]] = {
    "name": "Harry",
    "age": 21
}

student: Dict[str, Union[str, int,bool]] = {
    "name": "Harry",
    "age": 21,
    "isMarried": False
}


# ---------- UNION ----------
value: Union[int, str] = 10
value = "Ten"

# ---------- OPTIONAL (Union with None) ----------
email: Optional[str] = None
email = "abc@gmail.com"

# ---------- ANY ----------
data: Any = 10
data = "Hello"
data = [1, 2, 3]

# ---------- FUNCTION RETURN TYPES ----------
def add(a: int, b: int) -> int:
    return a + b
add(9,5)

def greet(name: str) -> None:
    print("Hello", name)
greet("sumit")
# ---------- FUNCTION WITH UNION ----------
def square(num: Union[int, float]) -> float:
    return num * num
square(6.087)

def rectangle(num1: Union[int, float], num2: Union[int, float]) -> float:
    return num1 * num2
rectangle(6.087, 5.0)

# ---------- CALLABLE ----------
def apply_operation(x: int, y: int, op: Callable[[int, int], int]) -> int:
    return op(x, y)
print(apply_operation(2, 3, add))


# ---------- ITERABLE ----------
def print_items(items: Iterable[str]) -> None:
    for item in items:
        print(item)
print_items(["Python", "Java", "C++",89,98,98])


# ---------- LITERAL ----------
status: Literal["SUCCESS", "FAILED"] = "SUCCESS"

# ---------- TYPE ALIAS ----------
Vector = List[int]
vector: Vector = [1, 2, 3]

# ---------- CLASS WITH TYPE HINTS ----------
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

    def info(self) -> str:
        return f"{self.name} is {self.age} years old"
p = Person("Sumit", 21)
print(p.info())

