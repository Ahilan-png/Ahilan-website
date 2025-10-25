import google.generativeai as genai
import tkinter as tk
from tkinter import scrolledtext, messagebox

import os
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel("models/gemini-2.5-flash")


def ask_gemini():
    user_input = user_entry.get("1.0", tk.END).strip()
    if not user_input:
        messagebox.showwarning("Warning", "Please enter a question.")
        return

    chat_area.insert(tk.END, f"You: {user_input}\n", "user")

    try:
        response = model.generate_content(user_input)
        answer = response.text.strip()
        chat_area.insert(tk.END, f"Gemini: {answer}\n\n", "gemini")
        chat_area.yview(tk.END)
    except Exception as e:
        chat_area.insert(tk.END, f"Error: {e}\n", "error")

    user_entry.delete("1.0", tk.END)



window = tk.Tk()
window.title("Ahilan's AI Chatbot")
window.geometry("700x600")
window.config(bg="#f4f4f4")


chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, font=("Consolas", 12))
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_area.tag_config("user", foreground="blue")
chat_area.tag_config("gemini", foreground="green")
chat_area.tag_config("error", foreground="red")


label = tk.Label(window, text="Enter your question below", font=("Arial", 12, "bold"), bg="#f4f4f4")
label.pack(pady=5)


user_entry = tk.Text(window, height=3, font=("Consolas", 12), wrap=tk.WORD)
user_entry.pack(padx=10, pady=5, fill=tk.X)


ask_button = tk.Button(window, text="Ask Axioms", command=ask_gemini, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
ask_button.pack(pady=10)


window.mainloop()

