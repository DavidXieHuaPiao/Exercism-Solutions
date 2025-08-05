def is_paired(input_string):
    """
    Verifies that all brackets, braces, and parentheses in a string are
    correctly matched and nested. Ignores all other characters.

    Args:
        input_string: The string to be checked for paired brackets.

    Returns:
        True if the string has correctly paired brackets, False otherwise.
    """
    
    # A list to act as a stack for opening brackets.
    stack = []
    
    # A dictionary to map opening brackets to their closing counterparts.
    bracket_map = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    
    # Iterate through each character of the string.
    for char in input_string:
        # If the character is an opening bracket, push it onto the stack.
        if char in bracket_map:
            stack.append(char)
        
        # If the character is a closing bracket, process it.
        elif char in bracket_map.values():
            # If the stack is empty, there is no opening bracket for this
            # closing bracket, so it's not paired correctly.
            if not stack:
                return False
            
            # Pop the last opening bracket from the stack.
            last_opening = stack.pop()
            
            # Check if the closing bracket matches the last opening bracket.
            # We use the bracket_map to find the correct match.
            if bracket_map[last_opening] != char:
                return False
                
        # Any other characters are ignored.

    # After the loop, the stack must be empty for the brackets to be paired.
    # If it's not empty, it means there are unclosed opening brackets.
    return not stack