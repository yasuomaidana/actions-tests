"""Simple calculator module for testing GitHub Actions."""


def add(a, b):
    """
    Add two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Sum of a and b
    """
    return a + b


def add_multiple(*args):
    """
    Add multiple numbers together.
    
    Args:
        *args: Variable number of arguments to add
        
    Returns:
        Sum of all arguments
    """
    return sum(args)
