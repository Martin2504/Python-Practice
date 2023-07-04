def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function")
    return wrapper

@announce       # Wrapping the hello function inside of the announce decorator.
def hello():
    print("Hello, world!")

hello()