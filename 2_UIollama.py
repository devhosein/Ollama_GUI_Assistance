# import streamlit as st    

# st.title("wow")

# st.write("hello world")

# text_input = st.sidebar.input_text("Enter text here")




# import streamlit as st

# st.title("🦜🔗 Quickstart App")

# with st.form("my_form"):
#     text = st.text_area(
#         "Enter text:",
#         "What are the three key pieces of advice for learning how to code?",
#     )
#     submitted = st.form_submit_button("Submit")
#     # if not openai_api_key.startswith("sk-"):
#     #     st.warning("Please enter your OpenAI API key!", icon="⚠")
#     # if submitted and openai_api_key.startswith("sk-"):
#         #generate_response(text)
#     st.write(text)



# # ollama pull gemma2:9b #or 27b
# import streamlit as st 
# from langchain_community.llms import Ollama
# from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
# from langchain.callbacks.manager import CallbackManager

# st.title("Gemma")

# callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])


# def get_response(user_input):
#     # ایجاد یک کال‌بک برای استریمینگ
#     callback = StreamingCallback(response_placeholder)
#     callback_manager = CallbackManager([callback])

#     # ارسال ورودی به مدل
#     llm.invoke(user_input, callbacks=callback_manager)


# from langchain_community.llms import Ollama
# from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
# from langchain.callbacks.manager import CallbackManager

# callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

# llm = Ollama(model="gemma2:9b", callbacks=callback_manager)

# def chat_with_llm():
#   """Handles the chat interaction with the LLM."""

#   while True:
#     user_input = st.text_area('Enter text here')
#     # submitted = st.form_submit_button("Submit")
#     if user_input == "exit":
#       print("Chatbot: Goodbye!")
#       break
#     if submitted :
#         response = llm.invoke(user_input)
#         print("Chatbot:", response)
#         st.write(response)

# # Start the chat loop
# chat_with_llm()




# import streamlit as st
# from langchain_community.llms import Ollama
# from langchain.callbacks.manager import CallbackManager
# from langchain.callbacks.base import BaseCallbackHandler

# # کلاس برای استریمینگ خروجی مدل
# class StreamCallbackHandler(BaseCallbackHandler):
#     def __init__(self, placeholder):
#         self.placeholder = placeholder
#         self.output = ""

#     def on_llm_new_token(self, token: str, **kwargs):
#         self.output += token
#         self.placeholder.markdown(self.output)  # به‌روزرسانی خروجی در استریم

# # رابط کاربری
# st.set_page_config(page_title="Gemma Chat", layout="wide")

# # ایجاد session برای ذخیره پیام‌ها
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # بارگذاری مدل
# callback_placeholder = st.empty()
# callback_manager = CallbackManager([])
# llm = Ollama(model="gemma2:9b", callbacks=callback_manager)

# # رابط چت
# st.title("Gemma Chat")

# # نمایش پیام‌های رد و بدل‌شده
# for message in st.session_state.messages:
#     role = "User" if message["is_user"] else "Gemma"
#     st.markdown(f"**{role}:** {message['content']}")

# # ورودی کاربر
# with st.container():
#     user_input = st.text_input("Type your message:", key="user_input", placeholder="Enter your message here...")

#     if st.button("Send"):
#         if user_input.strip():
#             # ذخیره پیام کاربر
#             st.session_state.messages.append({"content": user_input, "is_user": True})
            
#             # ایجاد استریمینگ
#             placeholder = st.empty()
#             stream_handler = StreamCallbackHandler(placeholder)
#             callback_manager = CallbackManager([stream_handler])

#             # فراخوانی مدل
#             try:
#                 llm = Ollama(model="gemma2:9b", callbacks=callback_manager)
#                 llm.invoke(user_input)
                
#                 # ذخیره پاسخ مدل
#                 st.session_state.messages.append({"content": stream_handler.output, "is_user": False})
#             except Exception as e:
#                 st.error(f"An error occurred: {e}")

#         # پاک کردن ورودی
#         st.session_state["user_input"] = ""































# import streamlit as st
# from langchain_community.llms import Ollama
# from langchain.callbacks.manager import CallbackManager
# from langchain.callbacks.base import BaseCallbackHandler

# # کلاس برای استریمینگ خروجی مدل
# class StreamCallbackHandler(BaseCallbackHandler):
#     def __init__(self, placeholder):
#         self.placeholder = placeholder
#         self.output = ""

#     def on_llm_new_token(self, token: str, **kwargs):
#         self.output += token
#         self.placeholder.markdown(self.output)  # به‌روزرسانی خروجی در استریم

# # تنظیمات صفحه
# st.set_page_config(page_title="Gemma Chat", layout="wide")

# # ایجاد session برای ذخیره پیام‌ها
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # بارگذاری مدل
# callback_manager = CallbackManager([])
# llm = Ollama(model="gemma2:9b", callbacks=callback_manager)

# # عنوان صفحه
# st.title("Gemma Chat")

# # نمایش پیام‌های رد و بدل‌شده
# chat_container = st.container()
# with chat_container:
#     for message in st.session_state.messages:
#         if message["is_user"]:
#             st.markdown(
#                 f"<div style='text-align: right; margin: 5px; padding: 10px; background-color: #DCF8C6; border-radius: 10px; display: inline-block; max-width: 80%;'>{message['content']}</div>",
#                 unsafe_allow_html=True,
#             )
#         else:
#             st.markdown(
#                 f"<div style='text-align: left; margin: 5px; padding: 10px; background-color: #FFFFFF; border-radius: 10px; display: inline-block; max-width: 80%;'>{message['content']}</div>",
#                 unsafe_allow_html=True,
#             )

# # اضافه کردن فاصله برای ورودی در پایین
# st.write("\n" * 10)

# # ورودی کاربر
# user_input = st.text_input("Type your message:", key="user_input", placeholder="Enter your message here...")

# if st.button("Send"):
#     if user_input.strip():
#         # ذخیره پیام کاربر
#         st.session_state.messages.append({"content": user_input, "is_user": True})
        
#         # ایجاد استریمینگ
#         placeholder = st.empty()
#         stream_handler = StreamCallbackHandler(placeholder)
#         callback_manager = CallbackManager([stream_handler])

#         # فراخوانی مدل
#         try:
#             llm = Ollama(model="gemma2:9b", callbacks=callback_manager)
#             llm.invoke(user_input)
            
#             # ذخیره پاسخ مدل
#             st.session_state.messages.append({"content": stream_handler.output, "is_user": False})
#         except Exception as e:
#             st.error(f"An error occurred: {e}")
        
#     # پاک کردن ورودی بدون تغییر مستقیم
#     st.session_state.user_input = ""















































# import streamlit as st
# from langchain_community.llms import Ollama
# from langchain.callbacks.manager import CallbackManager
# from langchain.callbacks.base import BaseCallbackHandler

# # کلاس برای مدیریت استریمینگ
# class StreamCallbackHandler(BaseCallbackHandler):
#     def __init__(self, placeholder):
#         self.placeholder = placeholder
#         self.output = ""

#     def on_llm_new_token(self, token: str, **kwargs):
#         self.output += token
#         self.placeholder.markdown(self.output)  # به‌روزرسانی خروجی

# # تنظیمات صفحه
# st.set_page_config(page_title="Gemma Chat", layout="wide")

# # ایجاد session برای ذخیره پیام‌ها
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # بارگذاری مدل
# callback_manager = CallbackManager([])
# llm = Ollama(model="gemma2:9b", callbacks=callback_manager)

# # چیدمان کلی صفحه
# st.title("Gemma Chat")
# chat_container = st.container()

# # نمایش پیام‌ها
# with chat_container:
#     for message in st.session_state.messages:
#         if message["is_user"]:
#             st.markdown(
#                 f"""
#                 <div style='text-align: right; margin: 10px; padding: 10px; background-color: #DCF8C6; border-radius: 10px; max-width: 80%; display: inline-block;'>
#                     {message['content']}
#                 </div>
#                 """,
#                 unsafe_allow_html=True,
#             )
#         else:
#             st.markdown(
#                 f"""
#                 <div style='text-align: left; margin: 10px; padding: 10px; background-color: #F1F0F0; border-radius: 10px; max-width: 80%; display: inline-block;'>
#                     {message['content']}
#                 </div>
#                 """,
#                 unsafe_allow_html=True,
#             )

# # اضافه کردن ورودی پایین صفحه
# st.write("<div style='position: fixed; bottom: 0; width: 100%; background-color: #FFFFFF; padding: 10px; box-shadow: 0px -2px 5px rgba(0,0,0,0.1);'>", unsafe_allow_html=True)

# # ایجاد بخش ورودی
# col1, col2 = st.columns([8, 1])
# with col1:
#     user_input = st.text_input(
#         "Type your message:",
#         placeholder="Enter your message here...",
#         key="user_input",
#         label_visibility="collapsed",
#     )
# with col2:
#     send_button = st.button("Send", key="send_button")

# # پردازش پیام‌ها
# if send_button and user_input.strip():
#     # اضافه کردن پیام کاربر به لیست
#     st.session_state.messages.append({"content": user_input, "is_user": True})

#     # نمایش پیام بلافاصله پس از ارسال
#     with chat_container:
#         st.markdown(
#             f"""
#             <div style='text-align: right; margin: 10px; padding: 10px; background-color: #DCF8C6; border-radius: 10px; max-width: 80%; display: inline-block;'>
#                 {user_input}
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )

#     # استریم پاسخ مدل
#     placeholder = st.empty()
#     stream_handler = StreamCallbackHandler(placeholder)
#     callback_manager = CallbackManager([stream_handler])

#     try:
#         llm = Ollama(model="gemma2:27b", callbacks=callback_manager)
#         llm.invoke(user_input)

#         # ذخیره پاسخ مدل
#         st.session_state.messages.append({"content": stream_handler.output, "is_user": False})
#     except Exception as e:
#         st.error(f"An error occurred: {e}")

#     # پاک کردن ورودی
#     st.experimental_rerun()






















































































import streamlit as st
from langchain_community.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.base import BaseCallbackHandler

# کلاس مدیریت استریمینگ
class StreamCallbackHandler(BaseCallbackHandler):
    def __init__(self, placeholder):
        self.placeholder = placeholder
        self.output = ""

    def on_llm_new_token(self, token: str, **kwargs):
        self.output += token
        self.placeholder.markdown(self.output)  # به‌روزرسانی خروجی

# تنظیمات استریم‌لیت
st.set_page_config(page_title="Gemma Chat", layout="wide")

# بارگذاری مدل
callback_manager = CallbackManager([])
llm = Ollama(model="gemma2:27b", callbacks=callback_manager)

# ذخیره پیام‌ها در session_state
if "messages" not in st.session_state:
    st.session_state.messages = []

# تابع ارتباط با مدل
def get_response(context, user_input, placeholder):
    # ترکیب کانتکست مکالمه
    full_input = "\n".join([f"You: {msg['content']}" if msg['is_user'] else f"Gemma: {msg['content']}" for msg in context])
    full_input += f"\nYou: {user_input}\nGemma:"
    
    # مدیریت استریم
    stream_handler = StreamCallbackHandler(placeholder)
    callback_manager = CallbackManager([stream_handler])
    
    # ارسال ورودی به مدل
    llm.callbacks = callback_manager
    llm.invoke(full_input)

    return stream_handler.output

# نمایش پیام‌های قبلی
st.title("Gemma Chat")
chat_container = st.container()
with chat_container:
    for message in st.session_state.messages:
        if message["is_user"]:
            st.markdown(f"<div style='text-align: right; color: blue;'>{message['content']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='text-align: left; color: green;'>{message['content']}</div>", unsafe_allow_html=True)

# ورودی کاربر
user_input = st.text_input("Type your message:", key="user_input")

if st.button("Send"):
    if user_input.strip():
        # ذخیره پیام کاربر
        st.session_state.messages.append({"content": user_input, "is_user": True})
        
        # دریافت پاسخ مدل
        placeholder = st.empty()
        response = get_response(st.session_state.messages, user_input, placeholder)
        
        # ذخیره پاسخ مدل
        st.session_state.messages.append({"content": response, "is_user": False})

        # پاک کردن ورودی
        st.experimental_rerun()
