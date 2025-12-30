import customtkinter as ctk
import requests

def send_search(event=None):
    query = entry.get()
    if query:
        # This calls your 'app.py' server we built earlier!
        try:
            response = requests.get(f"http://127.0.0.1:8000/search?query={query}")
            result = response.json()['answer']
            result_label.configure(text=result, text_color="white")
        except:
            result_label.configure(text="❌ Python Server is not running!", text_color="red")

# UI Setup
root = ctk.CTk()
root.title("Nebula Search")
root.geometry("500x150")
root.attributes("-topmost", True)  # Keeps it on top

# Styling it like a Mac bar
entry = ctk.CTkEntry(root, placeholder_text="🔍 Search your documents...", width=450, height=40, font=("Helvetica", 18))
entry.pack(pady=20)
entry.bind("<Return>", send_search)

result_label = ctk.CTkLabel(root, text="", font=("Helvetica", 12))
result_label.pack()

root.mainloop()
