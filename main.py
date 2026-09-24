from flask import Flask, render_template, request
import platform
import json
import os

app = Flask(__name__)


def get_system_info():
    return {
        "Operating System": platform.system(),
        "OS Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "Architecture": platform.architecture()[0],
        "Hostname": platform.node()
    }


def save_system_report(filename="system_report.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(get_system_info(), f, indent=4)


def compare_systems(system_a, system_b):
    comparison = {}

    all_keys = set(system_a.keys()) | set(system_b.keys())

    for key in sorted(all_keys):
        value_a = system_a.get(key, "Not Available")
        value_b = system_b.get(key, "Not Available")

        if value_a == value_b:
            comparison[key] = "Match"
        else:
            comparison[key] = (
                f"Difference - System A: {value_a} | "
                f"System B: {value_b}"
            )

    return comparison


@app.route("/", methods=["GET", "POST"])
def index():
    system_info = get_system_info()
    system_b = None
    comparison = None
    error = None

    if request.method == "POST":
        file = request.files.get("system_b")

        if not file:
            error = "Please select a JSON file."

        elif not file.filename.lower().endswith(".json"):
            error = "Only JSON files are allowed."

        else:
            try:
                system_b = json.load(file)

                if not isinstance(system_b, dict):
                    raise ValueError("JSON must contain an object.")

                comparison = compare_systems(
                    system_info,
                    system_b
                )

            except json.JSONDecodeError:
                error = "Invalid JSON file."
            except Exception as e:
                error = f"Error: {e}"

    return render_template(
        "index.html",
        system_info=system_info,
        system_b=system_b,
        comparison=comparison,
        error=error
    )


if __name__ == "__main__":
    # Automatically generate local system report
    save_system_report()

    print("System report generated: system_report.json")
    print("Starting Flask application...")

    app.run(host="0.0.0.0", port=5000, debug=True)
`