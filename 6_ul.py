import streamlit as st
from langchain_community.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.base import BaseCallbackHandler
import os

# کلاس مدیریت استریمینگ
class StreamCallbackHandler(BaseCallbackHandler):
    def __init__(self, placeholder):
        self.placeholder = placeholder
        self.output = ""

    def on_llm_new_token(self, token: str, **kwargs):
        self.output += token
        self.placeholder.markdown(self.output, unsafe_allow_html=True)

# تنظیمات صفحه
st.set_page_config(page_title="Gemma Chat", layout="wide")

# بارگذاری مدل
callback_manager = CallbackManager([])
llm = Ollama(model="gemma2:9b", callbacks=callback_manager)

# ذخیره پیام‌ها
if "messages" not in st.session_state:
    st.session_state.messages = []

# استایل CSS برای نمایش زیبا
st.markdown("""
    <style>
    .chat-message {
        margin: 10px 0;
        padding: 10px 15px;
        border-radius: 15px;
        max-width: 80%;
        display: inline-block;
        animation: slideUp 0.5s ease-out;
    }
    .user-message {
        background-color: #DCF8C6;
        text-align: right;
        float: right;
        clear: both;
        animation: slideUp 0.5s ease-out
    }
    .bot-message {
        background-color: #F1F0F0;
        text-align: left;
        float: left;
        clear: both;
        animation: slideUp 0.5s ease-out
    }
    .message-container {
        margin-bottom: 50px;
    }
    @keyframes slideUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    </style>
""", unsafe_allow_html=True)

# تابع دریافت پاسخ
def get_response(context, user_input, placeholder):
    full_input = "\n".join([f"You: {msg['content']}" if msg['is_user'] else f"Gemma: {msg['content']}" for msg in context])
    full_input += f"\nYou: {user_input}\nGemma:"
    
    stream_handler = StreamCallbackHandler(placeholder)
    callback_manager = CallbackManager([stream_handler])
    
    llm.callbacks = callback_manager
    llm.invoke(full_input)

    return stream_handler.output

# نمایش پیام‌ها
st.title("Gemma Chat")
chat_container = st.container()
with chat_container:
    for message in st.session_state.messages:  # پیام‌ها به ترتیب اصلی نمایش داده می‌شوند
        if message["is_user"]:
            st.markdown(f"<div class='chat-message user-message'>{message['content']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='chat-message bot-message'>{message['content']}</div>", unsafe_allow_html=True)

# ورودی کاربر
user_input = st.text_input("Type your message:", value="", key="user_input")

if st.button("Send"):
    if user_input.strip():
        # افزودن پیام کاربر
        st.session_state.messages.append({"content": user_input, "is_user": True})
        
        # نمایش پیام با افکت
        placeholder = st.empty()
        response = get_response(st.session_state.messages, user_input, placeholder)
        st.session_state.messages.append({"content": response, "is_user": False})
        
        ### getting the chat resulte
        text_watcher = response
        print(text_watcher)
        
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
        my_text = text_watcher

        extracted_code = extract_code(my_text)
        if extracted_code:
            # print(extracted_code)
            code_to_write = extracted_code  # the exact code that we want to run it automatically in another code. 
            def create_and_run_python_file(code):
                if code.startswith("python"):
                    code = code.split("\n", 1)[1]  # خط اول را حذف می‌کند

                # نام فایل جدید
                file_name = "generated_script.py"

                # ایجاد و نوشتن کد در فایل جدید
                with open(file_name, "w", encoding="utf-8") as file:
                    file.write(code)

                print(f"File '{file_name}' created successfully.")

                # اجرای فایل جدید
                os.system(f"python {file_name}")

            create_and_run_python_file(code_to_write)
        else:
            print("\nNo code block found.")

        # #####
        # #####
        # # run the code that it wants
        # def create_and_run_python_file(code):
        #     # نام فایل جدید
        #     file_name = "generated_script.py"

        #     # ایجاد و نوشتن کد در فایل جدید
        #     with open(file_name, "w", encoding="utf-8") as file:
        #         file.write(code)

        #     print(f"File '{file_name}' created successfully.")

        #     # اجرای فایل جدید
        #     os.system(f"python {file_name}")



        #####

        # حذف مقدار ورودی از st.session_state
        st.session_state.pop("user_input", None)
        st.experimental_rerun()



