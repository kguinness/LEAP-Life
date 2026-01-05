import csv
import os
import json

input_filename = "test_scores.csv"
output_filename = "output.json"

if os.path.exists(output_filename):
    os.remove(output_filename)

average_final = 0.0
unique_students = 0

running_sum = 0.0
count = 0
seen_students = set()

with open(input_filename, mode='r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    reader.fieldnames = [name.strip() for name in reader.fieldnames]

    for row in reader:
        row = {k.strip(): v for k, v in row.items()}
        try:
            val = float(row["score"])
            running_sum += val
            count += 1
        except ValueError:
            continue
        seen_students.add(row["student_id"])

if count > 0:
    average_final = running_sum / count

result = {
    "average_final": average_final,
    "unique_students": len(seen_students),
}

with open(output_filename, "w") as out:
    json.dump(result, out, indent=2)

print(f"Success! Processed {count} scores.")
print(f"Average Score: {average_final}")
print(f"Unique Students: {len(seen_students)}")
