import nltk
from nltk.corpus import movie_reviews
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Step 1: Download the dataset
nltk.download('movie_reviews')

# Step 2: Load dataset
reviews = []
labels = []

for category in movie_reviews.categories():  # 'pos' and 'neg'
    for fileid in movie_reviews.fileids(category):
        reviews.append(movie_reviews.raw(fileid))
        labels.append(1 if category == 'pos' else 0)

# Step 3: Convert text to TF-IDF features
vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
X = vectorizer.fit_transform(reviews)

# Step 4: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, labels, test_size=0.2, random_state=42, shuffle=True
)

# Step 5: Train Naïve Bayes model
classifier = MultinomialNB()
classifier.fit(X_train, y_train)

# Step 6: Evaluate model
y_pred = classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}')

# Step 7: Test with new review
new_review = ["The movie was not much good, waste of time to watch"]
new_review_vectorized = vectorizer.transform(new_review)

prediction = classifier.predict(new_review_vectorized)
print('Sentiment Prediction:', 'Positive' if prediction[0] == 1 else 'Negative')

