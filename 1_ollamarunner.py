# from langchain_community.llms import Ollama
# from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
# from langchain.callbacks.manager import CallbackManager

# callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

# llm = Ollama(model="gemma2:9b", callbacks=callback_manager)

# response = llm.invoke("prompt here")

# print(response)






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
#     user_input = input("You: ")
#     if user_input == "exit":
#       print("Chatbot: Goodbye!")
#       break
#     response = llm.invoke(user_input)
#     print("Chatbot:", response)

# # Start the chat loop
# chat_with_llm()






########

# ollama pull gemma2:9b #or 27b
import streamlit as st 
from langchain_community.llms import Ollama
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.callbacks.manager import CallbackManager

st.title("Gemma")

callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])


def get_response(user_input):
    # ایجاد یک کال‌بک برای استریمینگ
    callback = StreamingCallback(response_placeholder)
    callback_manager = CallbackManager([callback])

    # ارسال ورودی به مدل
    llm.invoke(user_input, callbacks=callback_manager)


from langchain_community.llms import Ollama
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.callbacks.manager import CallbackManager

callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

llm = Ollama(model="gemma2:9b", callbacks=callback_manager)

def chat_with_llm():
  """Handles the chat interaction with the LLM."""

  while True:
    user_input = input("You: ")
    if user_input == "exit":
      print("Chatbot: Goodbye!")
      break
    response = llm.invoke(user_input)
    print("Chatbot:", response)

# Start the chat loop
chat_with_llm()


########







# import streamlit as st
# from langchain_community.llms import Ollama
# from langchain.callbacks.manager import CallbackManager
# import threading

# # تنظیمات استریملیت
# st.title("Real-time Chat with LLM")

# # متغیر و فضای خالی برای استریمینگ
# response_placeholder = st.empty()

# # تنظیمات کال‌بک برای استریمینگ
# class StreamingCallback:
#     def __init__(self, response_placeholder):
#         self.response_placeholder = response_placeholder
#         self.response_text = ""

#     def on_new_token(self, token: str):
#         # دریافت هر توکن جدید از مدل و بروزرسانی در استریملیت
#         self.response_text += token
#         self.response_placeholder.text(self.response_text)

# # مدل LLM
# llm = Ollama(model="gemma2:9b")

# # فراخوانی مدل و ارسال خروجی به استریملیت
# def get_response(user_input):
#     # ایجاد یک کال‌بک برای استریمینگ
#     callback = StreamingCallback(response_placeholder)
#     callback_manager = CallbackManager([callback])
    
#     # ارسال ورودی به مدل
#     llm.invoke(user_input, callbacks=callback_manager)

# # بخش چت
# def chat_with_llm():
#     """Handles the chat interaction with the LLM."""
    
#     user_input = st.text_input("You:", key="input")
    
#     if user_input:
#         # استفاده از thread برای پردازش و ارسال به صورت همزمان
#         threading.Thread(target=get_response, args=(user_input,)).start()

# # اجرای چت
# if __name__ == "__main__":
#     chat_with_llm()