import streamlit as st
from PIL import Image
from markdownlit import mdlit




page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
  background-image: url("https://img.rawpixel.com/s3fs-private/rawpixel_images/website_content/rm218batch7-katie-58a-job597.jpg?w=800&dpr=1&fit=default&crop=default&q=65&vib=3&con=3&usm=15&bg=F4F4F3&ixlib=js-2.2.1&s=060c6c2fc22754a570e8f94e2e704667");
  background-size: 100%;
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


css_file = "./styles/main.css"

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


colum1, colum2, colum3 = st.columns(3)
with colum1:
    img = Image.open("./Image/rupp_logo.png")
    st.image(img, width=170)
    st.write("### RUPP")
with colum3:
    img = Image.open("./Image/FE's logo.png")
    st.image(img, width=170)
    st.write("### ITE")
    


st.write("### Animals Recognition")


css = f"""



"""

st.markdown(css, unsafe_allow_html=True)



mdlit("""Image recognition, also known as computer vision, is a field of [red]artificial intelligence[/red] (AI)
      that focuses on teaching computers to interpret and understand visual data in the form 
      of images or videos. It involves developing algorithms
and models that can analyze and extract meaningful information from visual content.
Image recognition has a wide range of applications and offers significant utility in
various fields. One of its essential uses is object recognition and classification,
enabling automatic identification and categorization of objects within images or videos.
This capability finds practical applications in content-based image retrieval, product
identification, and sorting objects on assembly lines. Facial recognition, another 
prominent application, utilizes image recognition to authenticate individuals based 
on their facial features, leading to applications in security systems, access control, and identity verification.
In the medical field, image recognition plays a crucial role in interpreting medical
imaging such as X-rays, MRIs, CT scans, and pathology slides. It aids in disease detection,
diagnosis, surgical planning, and treatment monitoring. Image recognition is also 
integral to autonomous vehicles, where it identifies and tracks objects on the road,
such as pedestrians, vehicles, traffic signs, and lane markings, enabling safe navigation and decision-making.
""")







sokchea_info = """

<h4>Mr. Sokchea KOR</h4> <h5>Possition : Advisor<h5>
"""

st.markdown(sokchea_info, unsafe_allow_html=True)
    
    
    
    
st.write("#### Here is Members")
    
    
    
col1, col2= st.columns(2, gap="small")
with col1:
    img = Image.open("./Image/vitou.jpg")
    img = img.resize((200, 200))
    st.image(img, width=200)
    st.write("1. Member : Vitou Soy")
with col2:
    img = Image.open("./Image/Y kimly.jpg")
    img = img.resize((200, 200))
    st.image(img, width=200)
    st.write("2. Member : Kimly Y")
    
col1, col2= st.columns(2, gap="small")
with col2:
    img = Image.open("./Image/malis.jpg")
    img = img.resize((200, 200))
    st.image(img, width=200)
    st.write("3. Member : Malis Lany")
with col1:
    img = Image.open("./Image/vimean.jpg")
    img = img.resize((200, 200))
    st.image(img, width=200)
    st.write("4. Member : Reachvimean Borin")


social_media = {
    "⭕ Vitou Soy": "https://github.com/SoyVitou2019",
    "⭕ Kimly Y": "https://github.com/Kimlly",
    "⭕ Malis Lany": "https://github.com/lanymalis",
    "⭕ Reachvimean Borin": "https://github.com/Reachvimean"
}

st.write("#")
cols = st.columns(len(social_media))
i = 0
for project, link in social_media.items():
    i+=1
    st.write(f"{i}. Link Github : {project} : {link}")