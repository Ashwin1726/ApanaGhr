import csv

def load_profiles(csv_path):
    profiles = []
    with open(csv_path, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            profiles.append({
                "name": row["name"],
                "sleep_time": row["sleep_time"],
                "cleanliness": row["cleanliness"],
                "work_schedule": row["work_schedule"],
                "food_habits": row["food_habits"]
            })
    return profiles