from flask import Flask, render_template, request
from scorer.model import score_profiles
from scorer.utils import load_profiles

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    if request.method == "POST":
        user = {
            "sleep_time": request.form["sleep_time"],
            "cleanliness": request.form["cleanliness"],
            "work_schedule": request.form["work_schedule"],
            "food_habits": request.form["food_habits"]
        }
        profiles = load_profiles("data/profiles.csv")
        for profile in profiles:
            score = score_profiles(user, profile)
            results.append((profile["name"], score))
        results.sort(key=lambda x: x[1], reverse=True)

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)