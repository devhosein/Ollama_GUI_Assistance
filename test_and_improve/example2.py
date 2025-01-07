def extract_code(text):
    start_trigger = text.find("run this code!")
    if start_trigger == -1:
        return None  # "run this code!" not found

    start = text.find("```", start_trigger)
    if start == -1:
        return None  # No opening triple quotes found

    start += 3  # Move past the opening triple quotes
    end = text.find("```", start)
    if end == -1:
        return None  # No closing triple quotes found

    return text[start:end].strip()

# Example Usage
my_text = """
... some text ...
run this code!
```def hello():
    print("Hello world!")

```
... more text ...
"""

# my_text = """
# run this code!

# ```python
# print("Hello, world!")
# ```

# این کد ساده است و به این صورت کار می کند:

# * **`print()`**: این یک تابع در زبان پایتون است که استفاده می شود برای نمایش متن روی صفحه.
# * **`"Hello, world!"`**:  این متنی است که می خواهیم نمایش داده شود.   باید با  引ک ها (" ") احاطه شود تا Python آن را به عنوان یک رشته در نظر بگیرد.

# """

extracted_code = extract_code(my_text)
if extracted_code:
    print(extracted_code)
else:
    print("No code block found.")
