import streamlit as st
import cv2
import glob
import os
import shutil

from streamlit_extras.no_default_selectbox import selectbox


st.set_page_config(page_title="Animal Recongition", page_icon="./Image/vitou logo.png")

page_bg_img = f"""
<style>

[data-testid="block-container"] {{
    margin-top:0px;
    padding-top:0px;
}}

</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

css_file = "./styles/main.css"
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

categoris_name = os.listdir("./Predicted")

result = selectbox(
    "Select an option with different label",
    categoris_name,
    no_selection_label=" % All Categories",
)

# List of image paths
image_paths = glob.glob("./Predicted/*/*.jpg")

# Calculate the number of columns based on the length of the image list
num_columns = 3
num_rows = -(-len(image_paths) // num_columns)  # Round up division

# Create the columns
columns = st.columns(num_columns)
check_name_category = []
for i in range(len(image_paths)):
    check_name_category.append(image_paths[i].split("\\")[1])


if result is not None:
    index_name_of_img = 0
    # Iterate over the image paths and display the images in the columns
    for i, image_path in enumerate(image_paths):
        if check_name_category[i] == result:
            with columns[index_name_of_img % 3]:
                index_name_of_img += 1
                img = cv2.imread(image_path)
                img = cv2.resize(img, (200, 150))
                st.image(img, width=200)
                # Extract the filename from the image path
                filename = os.path.basename(image_path)

                # Write the filename below the image
                st.write(f"{index_name_of_img} - {filename[:-4]}")
else:
    for i, image_path in enumerate(image_paths):
        with columns[i % 3]:
            img = cv2.imread(image_path)
            img = cv2.resize(img, (200, 150))
            st.image(img, width=200)
            # Extract the filename from the image path
            filename = os.path.basename(image_path)

            # Write the filename below the image
            st.write(f"{i + 1} - {filename[:-4]}")
            
user_input = st.text_input("Enter Delete name", "")

if user_input != "":
    img_path = f"./Predicted/{user_input[:-1]}/{user_input}.jpg"
    if os.path.exists(img_path):
        os.remove(img_path)
        st.write(f"Image '{img_path}' has been successfully removed.")
    else:
        st.write(f"Image '{img_path}' does not exist.")
else:
    st.write("Message")



if st.button("Clear all Images"):
    directory_path = './Predicted'

    # Get a list of all items within the directory
    items = os.listdir(directory_path)

    # Iterate over the items
    for item in items:
        item_path = os.path.join(directory_path, item)

        # Check if the item is a subfolder
        if os.path.isdir(item_path):
            try:
                shutil.rmtree(item_path)
                print(f"Subfolder '{item_path}' removed successfully.")
            except OSError as e:
                print(f"Error: {str(e)}")

