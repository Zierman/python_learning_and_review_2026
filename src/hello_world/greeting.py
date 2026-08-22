def get_message(to: str | None = None) -> str:

  # Check that the argument is typed correctly
  if to is not None and not isinstance(to, str):
    raise TypeError("argument `to` must be of type str or None")

  name = to.strip() if to is not None else "World"

  return f"Hello, {name}!" if len(name) > 0 else "Hello!"

def main():
  print("Demonstration of get_message function:")
  print(f'get_message() outputs "{get_message()}"')
  print(f'get_message("John") outputs "{get_message("John")}"')

if __name__ == "__main__":
  main()