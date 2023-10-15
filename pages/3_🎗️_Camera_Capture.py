

import cv2
import streamlit as st
from glob import glob
import os



page_bg_img = f"""
<style>

[data-testid="block-container"] {{
    margin-top:0px;
    padding-top:0px;
    color:green;
}}

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


cap = cv2.VideoCapture(0)
start_button = True
write_text_predicted = []
img_data_predicted = []
st.write("### Video Capture with OpenCV")

frame_placeholder = st.empty()

css_file = "./styles/main.css"

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

def capture_image(img):
    lengthofImg = len(glob("./capture_img/*jpg"))
    cv2.imwrite(f"./capture_img/captured_image{lengthofImg+1}.jpg", img)  

colum1 , colum2, colum3 = st.columns(3)
with colum1:
    start_button =st.button("Start", type="secondary", use_container_width=4)
    if start_button:
        clear_img_path = glob("./capture_img/*jpg")
        for i in range(len(clear_img_path)):
            if os.path.exists(clear_img_path[i]):
                os.remove(clear_img_path[i])
with colum2:
    capture_button = st.button("Capture", type="secondary", use_container_width=4)
with colum3:
    stop_button = st.button("Stop", type="secondary", use_container_width=4)
                

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        st.write("#### The video capture has ended.")
        break

    # Convert the frame from BGR to RGB format
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    if capture_button:
        capture_image(frame)
        capture_button = False
        
    # Display the frame using Streamlit's st.image
    frame_placeholder.image(frame, channels="RGB")
    if cv2.waitKey(1) & 0xFF == ord("q") or stop_button: 
        break

cap.release()
cv2.destroyAllWindows()


from Models.XG_VGG import XG_boosting_prediction
from PIL import Image


uploaded_file = "./capture_img/*jpg"
img_path = glob(uploaded_file)
for i in range(len(img_path)):
    image = Image.open(img_path[i])
    col1, col2 = st.columns(2)

    with col1:
        st.image(image, width=300)
        
    pred_text = XG_boosting_prediction(img_path[i])
    write_text_predicted.append(pred_text[0])
    img_data_predicted.append(cv2.imread(img_path[i]))
    with col2:
        st.header("Basic Information ")
        pred_code = f"<h5 style='color: white'>*  Prediction :<span style='color: cyan'> {pred_text[0]}</span></h5>"
        st.markdown(pred_code, unsafe_allow_html=True)
        
        
        
predicted_file = "./Predicted"
predicted_folder = os.listdir(predicted_file)
if len(predicted_folder) < 1:
    os.makedirs(f"./Predicted/{write_text_predicted[0]}")
predicted_folder = os.listdir(predicted_file)
for i_txt in range(len(write_text_predicted)):
    if write_text_predicted[i_txt] not in predicted_folder:
        os.makedirs(f"./Predicted/{write_text_predicted[i_txt]}")
        predicted_folder = os.listdir(predicted_file)
    for index in range(len(predicted_folder)):
        if write_text_predicted[i_txt] == predicted_folder[index]:
            img_count_path = glob(f"./Predicted/{predicted_folder[index]}\*.jpg")
            cv2.imwrite(f"./Predicted/{predicted_folder[index]}/{write_text_predicted[i_txt]}{len(img_count_path)+1}.jpg", img_data_predicted[i_txt])
            for re_name_i in range(len(img_count_path)):
                cv2.imwrite(f"./Predicted/{predicted_folder[index]}/{write_text_predicted[i_txt]}{re_name_i}.jpg", cv2.imread(img_count_path[re_name_i]))
            break
    

   
                
        
            
    









    
















