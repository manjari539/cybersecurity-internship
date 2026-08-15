from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

emails = [
    "Verify your account now or it will be suspended",
    "Click here to claim your prize immediately",
    "Team standup at 3pm, agenda attached",
    "Your invoice for Q2 is ready for review",
    "Urgent: update your bank details to avoid closure"
]

labels = [1, 1, 0, 0, 1]

pipe = Pipeline([
    ("vec", CountVectorizer()),
    ("clf", MultinomialNB())
])

pipe.fit(emails, labels)

tests = [
    "Please verify your PayPal login",
    "Meeting notes from yesterday"
]

print("===== DAY 12 PHISHING EMAIL DETECTION =====")

for text in tests:
    pred = pipe.predict([text])[0]
    print(f"{'PHISHING' if pred else 'LEGIT'}: {text}")
