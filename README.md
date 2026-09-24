# System Configuration Comparison Tool

A lightweight Flask web application that automatically retrieves the host system's hardware and operating system specifications and allows users to upload a JSON report from another machine to run side-by-side spec comparisons.

---

## Features

- **Automated Host System Inspection**: Automatically extracts system details including OS, OS Version, Machine architecture, Processor, and Hostname using Python's `platform` module.
- **JSON Report Export**: Generates a local `system_report.json` file when launching via `main.py`.
- **Side-by-Side Comparison**: Upload a configuration JSON file from a second system to identify matching and differing parameters instantly.
- **Responsive Web Interface**: Features a clean, responsive UI styled with CSS for viewing specifications on mobile or desktop devices.
- **Input Validation**: Verifies file formats and JSON integrity before parsing to ensure robust performance.

---

## Project Structure

```text
.
├── app.py              # Main Flask application entry point
├── main.py             # Alternative entry point with auto JSON export
├── static/
│   └── style.css       # Frontend styling and layout
└── templates/
    └── index.html      # HTML interface template

Requirements
 * Python 3.7+
 * Flask
Installation & Setup
 * Clone or download the repository:
   git clone <repository-url>
cd <repository-directory>

 * Set up a virtual environment (optional but recommended):
   python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

 * Install dependencies:
   pip install flask

How to Run
You can run the application using either app.py or main.py:
Option A: Using main.py (Recommended for generating local reports)
Running main.py will automatically create/update a system_report.json file in the project directory before starting the server.
python main.py

Option B: Using app.py
To start the application directly without creating a local export file:
python app.py

Once started, open your web browser and navigate to:
[http://127.0.0.1:5000](http://127.0.0.1:5000)

Usage Guide
 * View Current System Specs: Upon opening the application, System A will display the live system configuration of the computer running the server.
 * Export Local Specs: If launched using main.py, you can use the generated system_report.json to transfer and compare against another instance.
 * Compare Systems:
   * Scroll to the Upload System B section.
   * Choose a valid .json configuration file exported from another machine.
   * Click Compare Systems.
   * Review the Comparison Results table at the bottom to easily spot matches and discrepancies between the two systems.
JSON Format Example
To compare a secondary system, ensure the uploaded JSON file follows this structure:
{
    "Operating System": "Windows",
    "OS Version": "10.0.19045",
    "Machine": "AMD64",
    "Processor": "Intel64 Family 6 Model 158 Stepping 10, GenuineIntel",
    "Architecture": "64bit",
    "Hostname": "DESKTOP-EXAMPLE"
}
