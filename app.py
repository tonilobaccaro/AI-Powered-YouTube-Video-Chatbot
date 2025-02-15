import streamlit as st
from video_processor import extract_video_identifier, fetch_transcript, retrieve_metadata, get_thumbnail
from content_analyzer import chat_interface
import os

def launch_application():
    # App title and branding
    app_title = "AI-Powered YouTube Video Chatbot"
    brand_logo = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/YouTube_Logo_2017.svg/2560px-YouTube_Logo_2017.svg.png"
    st.set_page_config(page_title=app_title, page_icon=brand_logo)
    st.title(app_title)
    st.image(brand_logo, width=200)

    # User input
    video_url = st.text_input("Enter YouTube Video URL:")

    if video_url:
        try:
            video_id = extract_video_identifier(video_url)
            transcript = fetch_transcript(video_id)
            metadata = retrieve_metadata(video_url)

            # Display video thumbnail
            thumbnail_path = get_thumbnail(video_id)
            st.image(thumbnail_path, caption=metadata['title'], use_column_width=True)

            # Video information
            st.subheader("Video Information")
            st.write(f"**Title:** {metadata['title']}")
            st.write(f"**Channel:** {metadata['channel']}")
            st.write(f"**Views:** {metadata['views']}")
            st.write(f"**Upload Date:** {metadata['upload_date']}")

            # Chat interface
            st.subheader("Chat about the Video")
            chat_interface(transcript)

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    launch_application()
