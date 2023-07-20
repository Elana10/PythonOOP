"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """This stores the start value into the the counter variable and saves it into an initial value to reference on reset"""
        self.num = start
        self.begin = start
    
    def __repr__(self):
        return f"SerialGenerator start = {self.begin} next = {self.num}"

    def reset(self):
        """Changes the count variable back to the initial value."""
        self.num = self.begin
    
    def generate(self):
        """Adds one to the count variable and returns what the number had been."""
        self.num = self.num + 1
        return self.num - 1
    
