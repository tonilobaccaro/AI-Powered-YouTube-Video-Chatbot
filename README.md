# AI-Powered-YouTube-Video-Chatbot

A limitation of most AI chatbots is that they cannot fetch information about videos very well. If you ask ChatGBT to summarize a video, it will not be able to access the content of the video directly. To solve this issue, I created a chatbot using streamlit which is able to fetch transcripts of YouTube videos with YouTubeTranscriptApi and uses an OpenAI API to analyze the content of the transcript. This chatbot allows users to ask any question about the video, including the creation of summaries and notes.

Dependencies: 
beautifulsoup4 
openai 
Requests 
streamlit 
youtube_transcript_api 

Setup Steps: 
1. Replace OpenAI API Key
2. Run: streamlit run app.py in a command prompt

