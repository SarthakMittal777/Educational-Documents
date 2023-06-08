import streamlit as st
import cv2
import numpy as np
from streamlit_webrtc import (
    VideoProcessorBase,
    WebRtcMode,
    webrtc_streamer,
)
# Define a WebRTC video processor that captures a single frame from the camera
class ImageProcessor(VideoProcessorBase):
    def _init_(self):
        self.frame = None

    def process(self, frame):
        # Only process the first frame received
        if self.frame is None:
            # Convert the frame to a NumPy array
            self.frame = np.array(frame.to_ndarray())
            # Convert the color format from BGR to RGB
            self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        # Return the processed frame
        return self.frame
st.markdown("# Technocrats Fashion Arena")
st.markdown("Upload your image and get recommendations")
# Create a file uploader widget
uploaded_file = st.file_uploader("Choose a file")

# Check if a file was uploaded
if uploaded_file is not None:
    # Check if the uploaded file is an image
    if uploaded_file.type.startswith('image'):
        # Display the image
        st.image(uploaded_file, caption='Uploaded Image')
    # If the uploaded file is not an image, assume it's a document
    else:
        # Display the file name and size
        file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
        st.write(file_details)
        
        # Read and display the file content
        file_content = uploaded_file.read()
        st.write(file_content)
# Start the camera and capture an image
webrtc_ctx = webrtc_streamer(key="camera", mode=WebRtcMode.SENDRECV, video_processor_factory=ImageProcessor)

if webrtc_ctx.video_receiver:
    # Display the captured image
    st.image(webrtc_ctx.video_receiver.frame, caption='Captured Image', use_column_width=True)
