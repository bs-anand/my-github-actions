from datetime import datetime


def greet(name: str) -> str:
    return f"Hello, {name}!"


def is_even(number: int) -> bool:
    return number % 2 == 0


if __name__ == "__main__":
    print(greet("Anand"))
    print("Current UTC time:", datetime.utcnow().isoformat())
    print("10 is even:", is_even(10))

