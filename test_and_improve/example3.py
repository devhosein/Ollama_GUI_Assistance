import os

def create_and_run_python_file(code):
    # نام فایل جدید
    file_name = "generated_script.py"

    # ایجاد و نوشتن کد در فایل جدید
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(code)

    print(f"File '{file_name}' created successfully.")

    # اجرای فایل جدید
    os.system(f"python {file_name}")

# نمونه کد که به عنوان ورودی داده می‌شود
code_to_write = """
print('Hello, World!')
for i in range(5):
    print(f'Iteration {i}')
"""

# فراخوانی تابع
create_and_run_python_file(code_to_write)
