from flask import Flask, render_template, request
import google.generativeai as genai

app = Flask(__name__)

# Configure your Gemini API key
genai.configure(api_key="AIzaSyBU-C46JDt-kuf7lxf5u2YbDI7JCC43Aoo")
model = genai.GenerativeModel("models/gemini-2.5-flash")

@app.route("/", methods=["GET", "POST"])
def chatbot():
    answer = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        if user_input.strip():
            try:
                response = model.generate_content(user_input)
                answer = response.text
            except Exception as e:
                answer = f"Error: {e}"
    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
