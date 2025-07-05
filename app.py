import streamlit as st
import os

# Set page config
st.set_page_config(
    page_title="TNG Soundboard",
    page_icon="🎵",
    layout="wide"
)

# Initialize session state for tracking playing state
if 'playing' not in st.session_state:
    st.session_state.playing = None

def toggle_sound(sound_file):
    if st.session_state.playing == sound_file:
        # Stop the sound
        st.session_state.playing = None
    else:
        # Start the new sound
        st.session_state.playing = sound_file

# Get all sound files
sound_files = [f for f in os.listdir('sound_files') if f.endswith('.mp3')]

# Create a grid of buttons
st.title("TNG Soundboard")
st.write("Click on any sound to play/stop it")

# Create columns for the grid
cols = st.columns(4)

# Add buttons to the grid
for idx, sound_file in enumerate(sound_files):
    col = cols[idx % 4]
    with col:
        # Create a button with the sound file name (without extension)
        button_label = os.path.splitext(sound_file)[0].replace('_', ' ').title()
        if st.button(button_label, key=sound_file):
            toggle_sound(sound_file)

# Display the currently playing sound
if st.session_state.playing:
    sound_path = os.path.join('sound_files', st.session_state.playing)
    st.audio(sound_path, format='audio/mp3', autoplay=True) 