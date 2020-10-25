"""A utility file for helper functions for models module
"""

def to_lower_camel(string: str) -> str:
    """Convert snake_case to lowerCamelCase

    Convert snake_case variable name used for Python variables to
    lowerCamelCase more associated for JavaScript and JSON variables

    Args:
        string (str): an input string name as snake_case variable

    Returns:
        a lowerCamelCase version of the input string
    """
    return ''.join(
        word.capitalize() if i > 0 else word
        for i, word in enumerate(string.split('_'))
    )
