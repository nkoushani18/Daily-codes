# --- Python Text Translator using Pattern Matching ---
# Learning Objective: This tutorial will teach you how to use Python's
# simple pattern matching capabilities (introduced in Python 3.10)
# to build a basic translator between different programming language
# syntaxes. We'll focus on translating common code structures like
# variable declarations and simple print statements.

# --- Core Concept: Pattern Matching in Python ---
# Pattern matching allows us to check the structure of an object
# against a series of patterns and execute code based on which pattern matches.
# It's similar to switch statements in other languages but much more powerful
# as it can inspect the *contents* of objects, not just their values.
# We will use `match` and `case` statements here.

def translate_code_snippet(code_line: str, target_language: str) -> str:
    """
    Translates a single line of code from a simplified syntax to a target language.

    Args:
        code_line: The string representing the code snippet to translate.
        target_language: The language to translate to (e.g., "javascript", "java").

    Returns:
        The translated code snippet as a string, or an error message if
        translation is not supported for the given input or target language.
    """

    # We'll define our translation rules within the match statement.
    # The `match` statement takes the input `code_line` and compares it
    # against the `case` patterns.

    match code_line.strip(): # .strip() removes leading/trailing whitespace for easier matching
        case f"let {variable_name} = {value}": # This pattern matches lines starting with "let"
            # The f-string pattern allows us to capture parts of the string.
            # Here, `variable_name` and `value` will be assigned the
            # corresponding parts of the `code_line`.
            # WHY: This captures the name and the assigned value.

            if target_language == "javascript":
                # WHY: JavaScript uses 'let' for variable declaration, so it's a direct translation.
                return f"let {variable_name} = {value};"
            elif target_language == "java":
                # WHY: Java requires explicit type declaration. For simplicity, we'll assume string.
                # In a real translator, you'd need type inference.
                return f"String {variable_name} = {value};"
            elif target_language == "python":
                # WHY: Python uses direct assignment without keywords like 'let'.
                return f"{variable_name} = {value}"
            else:
                # WHY: Handle cases where the target language is not supported.
                return f"Translation to {target_language} not supported for 'let' declaration."

        case f"print {message}": # This pattern matches lines starting with "print"
            # WHY: Captures the message to be printed.
            if target_language == "javascript":
                # WHY: JavaScript uses console.log() for printing.
                return f"console.log({message});"
            elif target_language == "java":
                # WHY: Java uses System.out.println() for printing.
                return f"System.out.println({message});"
            elif target_language == "python":
                # WHY: Python's print function is directly compatible.
                return f"print({message})"
            else:
                # WHY: Handle unsupported target languages.
                return f"Translation to {target_language} not supported for 'print' statement."

        case _: # The underscore `_` acts as a wildcard or default case.
            # WHY: This case matches anything that didn't match the previous patterns.
            # It's essential for handling unexpected input.
            return f"Unsupported code syntax or unknown line: '{code_line.strip()}'"

# --- Example Usage ---

print("--- Python to JavaScript Translation ---")
print(f"Input: let count = 10")
print(f"Output: {translate_code_snippet('let count = 10', 'javascript')}\n")

print(f"Input: print \"Hello, World!\"")
print(f"Output: {translate_code_snippet('print \"Hello, World!\"', 'javascript')}\n")

print("\n--- Python to Java Translation ---")
print(f"Input: let name = \"Alice\"")
print(f"Output: {translate_code_snippet('let name = \"Alice\"', 'java')}\n")

print(f"Input: print 123")
print(f"Output: {translate_code_snippet('print 123', 'java')}\n")

print("\n--- Python to Python Translation (for demonstration) ---")
print(f"Input: let language = \"Python\"")
print(f"Output: {translate_code_snippet('let language = \"Python\"', 'python')}\n")

print(f"Input: print 'Python is fun'")
print(f"Output: {translate_code_snippet('print \'Python is fun\'', 'python')}\n")

print("\n--- Handling Unsupported Cases ---")
print(f"Input: def my_func():")
print(f"Output: {translate_code_snippet('def my_func():', 'javascript')}\n")

print(f"Input: let x = 5")
print(f"Output: {translate_code_snippet('let x = 5', 'ruby')}\n")