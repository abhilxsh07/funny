"""Demonstrates a simple infinite loop without unbounded recursion."""


def run():
    """Continuously print a message with an incrementing counter."""
    count = 0
    try:
        while True:
            print("Hello World!", count)
            count += 1
    except KeyboardInterrupt:
        # Allow the user to exit cleanly with Ctrl+C
        pass


if __name__ == "__main__":
    run()


