import streamlit as st
import pickle
import  string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)
Tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))
st.title("Email/SMS Classifier")
input_sms=st.text_area("Enter the SMS/Email")
if st.button("Predict"):

# 1 preprocess
# 4 Display
    transform_sms = transform_text(input_sms)
# 2 vectorize
    vector_input = Tfidf.transform([transform_sms])
# 3 predict
    result=model.predict(vector_input)[0]
# 4. Result
    if result ==1:

       st.header("This message is a SPAM ")
    else:

        st.header("This is not SPAM")
