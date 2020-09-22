import textwrap

COL_WIDTH = 20


def text_to_columns(text):
    """Split text (input arg) to columns, the amount of double
       newlines (\n\n) in text determines the amount of columns.
       Return a string with the column output like:
       line1\nline2\nline3\n ... etc ...
       See also the tests for more info."""
    lines = [line.strip() for line in text.splitlines() if line.strip() != ""]
        
    wrapped_lines = [textwrap.wrap(line, COL_WIDTH) for line in lines]
    
    max_lines = 0
    
    for multiline in wrapped_lines:
        max_lines = max(max_lines, len(multiline))
        
    for multiline in wrapped_lines:
        if len(multiline) < max_lines:
            current_len = len(multiline)
            multiline += [""]*(max_lines - current_len)
    
    print(wrapped_lines)
    print(max_lines)
    pass

text = """My house is small but cosy.

    It has a white kitchen and an empty fridge."""

text_to_columns(text)