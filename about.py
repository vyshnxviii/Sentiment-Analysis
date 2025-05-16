import streamlit as st

def app():
      
    st.header('MoodMatrix: Your Community Sentiment Hub')

    text ="\nMoodMatrix is a platform designed to foster open communication and analyze the emotional undercurrents of online discussions. We empower you to:"
    st.write(text)
    st.markdown('   **Express yourself:** Share your thoughts and feelings in a safe and supportive environment.')
    st.markdown('   **Gain insights:** Understand the overall sentiment of a topic by analyzing the collective mood of the community.')
    st.markdown('   **Connect with others:** Discover people with similar perspectives and engage in meaningful conversations.')

    st.subheader('\nOur Mission!')

    test="MoodMatrix believes that understanding sentiment goes beyond simply identifying positive or negative opinions. We aim to:"
    st.write(text)
    st.markdown('**Uncover the nuances:** We employ advanced sentiment analysis tools to reveal the spectrum of emotions within a conversation.')
    st.markdown('**Promote empathy:** By analyzing sentiment, we encourage users to consider the emotional impact of their words.')
    st.markdown('**Build a positive community:** By fostering understanding and empathy, we strive to create a more constructive and engaging online space.')

    st.subheader('\nHow It Works?')
    st.markdown('**Post Your Thoughts:** Share your comments on various topics within the community.')
    st.markdown('**Analyze Sentiment:** Our sentiment analysis engine automatically analyzes the emotional tone of your post.')
    st.markdown('**See the Mood:** Visualizations and summaries provide insights into the overall sentiment of the discussion.')
    st.markdown('**Engage with Others:** Discover diverse perspectives, participate in respectful discussions, and build connections.')

    st.subheader('\nJoin the Conversation!')

    text="MoodMatrix welcomes you to join our vibrant community of individuals passionate about exploring the emotional landscape of online interactions. We encourage you to:"
    st.write(text)
    st.markdown('Share your opinions respectfully and considerately.')
    st.markdown('Be open to different perspectives.')
    st.markdown('Engage in constructive dialogue.')
    text="\nTogether, let's create a space where meaningful conversations and emotional understanding go hand in hand."
    st.write(text)
