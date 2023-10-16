import streamlit as st
from PIL import Image
import glob
import os
from streamlit_extras.let_it_rain import rain

st.set_page_config(page_title="Animal Recongition", page_icon="./Image/vitou logo.png")


rain(
    emoji="🌿",
    font_size=15,
    falling_speed=5,
    animation_length="infinite",
)



css_file = "./styles/main.css"

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
    
    
    
# List of image paths
image_paths = glob.glob("./animal_img/*")

# Calculate the number of columns based on the length of the image list
num_columns = 3
num_rows = -(-len(image_paths) // num_columns)  # Round up division

# Create the columns
columns = st.columns(num_columns)

# Iterate over the image paths and display the images in the columns
for i, image_path in enumerate(image_paths):
    with columns[i % num_columns]:
        img = Image.open(image_path)
        img = img.resize((200, 200))
        st.image(img, width=200)
        # Extract the filename from the image path
        filename = os.path.basename(image_path)

        # Write the filename below the image
        st.write(f"{i + 1} - {filename[:-4]}")