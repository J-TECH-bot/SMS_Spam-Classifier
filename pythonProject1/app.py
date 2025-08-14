import streamlit as st
import pickle
import nltk
import os
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import string

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

ps = PorterStemmer()

# Get the directory where the app.py file is located
current_dir = os.path.dirname(os.path.abspath(__file__))

#lets load the saved vectorizer and native model
try:
    tfidf = pickle.load(open(os.path.join(current_dir, 'vectorizer.pkl'),'rb'))
    model = pickle.load(open(os.path.join(current_dir, 'model.pkl'),'rb'))
except FileNotFoundError as e:
    st.error(f"Model files not found: {e}")
    st.stop()
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

#saving streamlit code
st.title("Email spam Classifier")
input_sms = st.text_area("Enter message")
def transform_text(text):
        text = text.lower()
        text = nltk.word_tokenize(text)
        ###############################################
        # Check for alphabetics
        y = []
        for i in text:
            if i.isalnum():
                y.append(i)
        text = y[:]
        y.clear()
        ######################################################
        # Remove punctuations
        for i in text:
            if i not in stopwords.words('english') and i not in string.punctuation:
                y.append(i)
        text = y[:]  # copy content
        y.clear()  # Clear original list
        #######################################################
        # append steaming method(Root words)
        for i in text:
            y.append(ps.stem(i))
        return " ".join(y)

    # transform_text("I'm gonna be home soon and i don't want to talk about this stuff anymore tonight, k? I've cried enough today.")


if st.button('predict'):
    #preprocess
    transformed_sms = transform_text(input_sms)
    #vectorize
    vector_input = tfidf.transform([transformed_sms])
    #predict
    result = model.predict(vector_input)[0]
    #display
    if result ==1:
        st.header("Spam")
    else:
        st.header("Not Spam")    