import streamlit as st
from textblob import TextBlob
import pandas as pd
import altair as alt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from firebase_admin import firestore


if 'db' not in st.session_state:
    st.session_state.db = ''
   
db=firestore.client()
st.session_state.db=db
   
            
# Function to convert sentiment dictionary to DataFrame (optional)
def convert_to_df(sentiment):
    sentiment_dict = {'polarity': sentiment.polarity, 'subjectivity': sentiment.subjectivity}
    sentiment_df = pd.DataFrame(sentiment_dict.items(), columns=['metric', 'value'])
    return sentiment_df


# Function to analyze sentiment of individual tokens (optional)
def analyze_token_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    pos_list, neg_list, neu_list = [], [], []
    for word in text.split():
        res = analyzer.polarity_scores(word)['compound']
        if res > 0.1:
            pos_list.append(word)
            pos_list.append(res)
        elif res <= -0.1:
            neg_list.append(word)
            neg_list.append(res)
        else:
            neu_list.append(word)
    result = {'positives': pos_list, 'negatives': neg_list, 'neutral': neu_list}
    return result


def main():
    st.subheader("Sentiment Analysis")

    try:
        
        with st.form(key='nlpForm'):
            raw_text = st.text_area("Enter Text Here")
            # Add a submit button for analysis
            analyze_button = st.form_submit_button(label='Analyze')

        # Layout
        col1, col2 = st.columns(2)

        if analyze_button:
            if raw_text!='':
                        
                info = db.collection('Posts').document(st.session_state.username).get()
                if info.exists:
                    info = info.to_dict()
                    if 'Content' in info.keys():
                    
                        pos=db.collection('Posts').document(st.session_state.username)
                        pos.update({u'Content': firestore.ArrayUnion([u'{}'.format(raw_text)])})
                        st.write('Post uploaded!!')
                    else:
                        
                        data={"Content":[raw_text],'Username':st.session_state.username}
                        db.collection('Posts').document(st.session_state.username).set(data)
                else:
                    data={"Content":[raw_text],'Username':st.session_state.username}
                    db.collection('Posts').document(st.session_state.username).set(data)
                        
                    st.success('Post uploaded!!')

                
                with col1:
                    st.info("Results")
                    sentiment = TextBlob(raw_text).sentiment
                    st.write(sentiment)

                    # Emoji
                    if sentiment.polarity > 0:
                        st.markdown("Sentiment:: Positive :smiley: ")
                    elif sentiment.polarity < 0:
                        st.markdown("Sentiment:: Negative :angry: ")
                    else:
                        st.markdown("Sentiment:: Neutral  ")

                    # Dataframe (optional)
                    result_df = convert_to_df(sentiment)
                    st.dataframe(result_df)

                    # Visualization (optional)
                    c = alt.Chart(result_df).mark_bar().encode(
                        x='metric',
                        y='value',
                        color='metric'
                    )
                    st.altair_chart(c, use_container_width=True)

                with col2:
                    st.info("Token Sentiment")

                    token_sentiments = analyze_token_sentiment(raw_text)
                    st.write(token_sentiments)

                    
        st.header(' :violet[Latest Posts] ')
    except:
        if st.session_state.username=='':
            st.text('Please Login first')      
        
        
        
    docs = db.collection('Posts').get()
            
    for doc in docs:
        d=doc.to_dict()
        try:
            st.text_area(label=':green[Posted by:] '+':orange[{}]'.format(d['Username']),value=d['Content'][-1],height=20)
        except: pass



        


if __name__ == '__main__':
    main()
