def make_shirt(size="L", message="I love Python"):
    print(f"Making a shirt of size {size}. Message on the shirt: '{message}'.")

# Make a large shirt with the default message
make_shirt()

# Make a medium shirt with the default message
make_shirt("M")

# Make a shirt of any size with a different message
make_shirt("S", "Code is Fun!")
