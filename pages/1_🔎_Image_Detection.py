import streamlit as st
from PIL import Image
from Models.XG_VGG import XG_boosting_prediction
# from gradioss import XG_boosting_prediction

    
    
    

st.set_page_config(
    page_title="Animal Recognition",
    page_icon="👾",
)
st.sidebar.success("select A page above.")


colum1, colum2 = st.columns(2)

with colum1:
    img = Image.open("./Image/FE's logo.png")
    st.image(img, width=100)

with colum2:
    title = f"<h2 style='color: white'>IT- Engineering G8</h2>"
    st.markdown(title, unsafe_allow_html=True)
    
# with colum3:
#     img = Image.open("./Image/rupp_logo.png")
#     st.image(img, width=100)


page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
  background-image: url("https://wallpapercave.com/wp/wp2665743.jpg");
  background-size: 160%;
  background-position: top left;
  background-repeat: repeat-y;
  background-attachment: local;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}



</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)




# Upload the image
uploaded_file = st.file_uploader("Drag and drop an image here or click to upload.", type=["jpg", "jpeg", "png"], key="image_uploader")

# Check if an image was uploaded
if uploaded_file is not None:
    #import tempfile library
    import tempfile
    import os
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(uploaded_file.read())
    temp_file.close()
    # Read basic information of img
    file_id = uploaded_file.file_id
    file_type = uploaded_file.type
    file_name = uploaded_file.name
    file_size = uploaded_file.size
    file_url = temp_file.name
    print(file_url)
    # Save the uploaded file to a temporary location
    
    image = Image.open(uploaded_file)
    col1, col2 = st.columns(2)
    
    with col1:
        st.image(image, width=300)
        
    pred_text = XG_boosting_prediction(file_url)
    with col2:
        st.header("Basic Information ")
        id_code = f"<h5 style='color: white'>*  Img_ID :<span style='color: cyan'> {file_id[0:6]}...{file_id[-7:-1:1]}</span></h5>"
        pred_code = f"<h5 style='color: white'>*  Prediction :<span style='color: cyan'> {pred_text}</span></h5>"
        type_code = f"<h5 style='color: white'>*  Img_type :<span style='color: cyan'> {file_type}</span></h5>"
        name_code = f"<h5 style='color: white'>*  Img_name :<span style='color: cyan'> {file_name}</span></h5>"
        size_code = f"<h5 style='color: white'>*  Img_size :<span style='color: cyan'> {file_size}</span> pixels</h5>"
        st.markdown(id_code, unsafe_allow_html=True)
        st.markdown(pred_code, unsafe_allow_html=True)
        st.markdown(type_code, unsafe_allow_html=True)
        st.markdown(name_code, unsafe_allow_html=True)
        st.markdown(size_code, unsafe_allow_html=True)
        

    










