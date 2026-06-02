import joblib
from resolution_engine import get_resolution
from severity_engine import get_severity

model = joblib.load("complaint_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

while True:

    complaint = input("\nEnter Complaint: ")

    if complaint.lower() == "exit":
        break

    complaint_vector = vectorizer.transform([complaint])

    prediction = model.predict(complaint_vector)[0]

    severity = get_severity(complaint)

    print("\nPredicted Category:")
    print(prediction)

    print("\nSeverity Level:")
    print(severity)

    print("\nSuggested Resolution:")
    print(get_resolution(prediction))