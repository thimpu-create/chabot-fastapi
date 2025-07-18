# gradio_app.py

import os
import requests
import gradio as gr
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

HF_TOKEN = os.getenv("token")

API_URL = "https://router.huggingface.co/novita/v3/openai/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {HF_TOKEN}",
}
MODEL = "meta-llama/llama-3.1-8b-instruct"
CUSTOM_SLANG = ["bro", "beta", "maaki", "sweetmaraani", "kela", "maaksudai"]

def query_llama(messages):
    system_prompt = {
        "role": "system",
        "content": f"""
        You are a chatbot with a humorous, desi personality created by Thimpu Sengyung.
        You frequently use casual slang words like: {", ".join(CUSTOM_SLANG)}.
        Add them randomly in your responses like a street-smart friend would do.
        """
    }
    full_messages = [system_prompt] + messages

    payload = {
        "model": MODEL,
        "messages": full_messages
    }
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    return response.json()

def stream_response(message, history):
    history.append({"role": "user", "content": message})
    try:
        result = query_llama(history)
        full_reply = result["choices"][0]["message"]["content"]
    except Exception as e:
        yield {"role": "assistant", "content": "⚠️ Error: " + str(e)}
        return

    current = ""
    for char in full_reply:
        current += char
        time.sleep(0.015)
        yield {"role": "assistant", "content": current}

chat_ui = gr.ChatInterface(
    fn=stream_response,
    type="messages",
    title="Thimpu's LLaMA Chat",
    description="""
        ### Ask me anything!
        Built using Hugging Face's **meta-llama/llama-3.1-8b-instruct** model via OpenAI-compatible router.<br>
        👤 **Made by Thimpu Sengyung**  
        🌐 Powered by [Hugging Face](https://huggingface.co) and Gradio.
        """,
    theme=gr.themes.Soft(primary_hue="emerald", secondary_hue="gray"),
    examples=[
        "What's the capital of Bhutan?",
        "Tell me a joke!",
        "Explain quantum physics like I'm 12.",
    ],
    save_history=True
)

def launch_gradio():
    chat_ui.launch(server_name="0.0.0.0", server_port=7860)

if __name__ == "__main__":
    launch_gradio()
