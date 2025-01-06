def extract_code(text):
    start_trigger = text.find("run this code!")
    if start_trigger == -1:
        return None  # "run this code!" not found

    start = text.find("'''", start_trigger)
    if start == -1:
        return None  # No opening triple quotes found

    start += 3  # Move past the opening triple quotes
    end = text.find("'''", start)
    if end == -1:
        return None  # No closing triple quotes found

    return text[start:end].strip()

# Example Usage
my_text = """
... some text ...
run this code!
'''
def hello():
    print("Hello world!")

'''
... more text ...
"""

extracted_code = extract_code(my_text)
if extracted_code:
    print(extracted_code)
else:
    print("No code block found.")
