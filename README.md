🧮 Python Web Calculator

Flask-based Web Application | Portfolio Project

A lightweight Python web application demonstrating backend API development, frontend integration, and clean software structure.
Built to showcase practical skills relevant to junior Python / software / IT support roles.

🎯 Project Objective

This project was developed to demonstrate:

Real-world Python + Flask usage

REST-style API design

Frontend–backend communication using JSON

Input validation and error handling

Clean, readable, and maintainable code

🚀 Key Features

Basic arithmetic operations (add, subtract, multiply, divide)

Interactive calculator interface (buttons + display)

Keyboard support for faster input

Backend JSON API (/api/calc)

Graceful error handling (invalid input, division by zero)

Modern UI using vanilla HTML, CSS, and JavaScript

Ready for cloud deployment

🧰 Technical Skills Demonstrated
Backend

Python programming

Flask web framework

API endpoint design

JSON request/response handling

Error and edge-case handling

Frontend

Semantic HTML

CSS layout and styling

JavaScript event handling

Fetch API (AJAX)

Software Practices

Project structuring

Separation of concerns

Virtual environments

Version control (Git)

📂 Project Structure
py-calculator/
│
├── app.py              # Flask app & API logic
├── templates/
│   └── index.html      # UI + JavaScript logic
└── README.md

⚙️ How It Works

User interacts with the calculator UI (buttons or keyboard)

Frontend sends calculation data as JSON to the Flask API

Flask validates inputs and performs the calculation

Result or error message is returned and displayed instantly

This design mirrors real production systems where frontend and backend communicate through APIs.

▶️ Running the Project Locally
git clone https://github.com/your-username/python-web-calculator.git
cd python-web-calculator

python -m venv venv
venv\Scripts\activate   # Windows
pip install flask

python app.py


Access the app at:

http://127.0.0.1:5000

📡 API Example

POST /api/calc

{
  "a": "8",
  "b": "4",
  "op": "÷"
}


Response

{
  "ok": true,
  "result": 2
}

💼 Why This Project Matters

This project shows my ability to:

Build a complete end-to-end web application

Work comfortably with Python web frameworks

Handle user input safely and correctly

Write code that is easy for others to understand and maintain

Apply concepts that scale to larger systems

🔮 Possible Enhancements

Calculation history storage

Unit testing (pytest)

Scientific calculator mode

Dockerization

Cloud deployment (Render / Fly.io)

👤 Author

Siboniso
Aspiring Python Developer | Web Developer | IT Support Technician

📍 South Africa
