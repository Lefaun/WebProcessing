import streamlit as st

# Set Streamlit page configuration
st.set_page_config(
    page_title="OpenProcessing Background",
    layout="wide"
)

# Define the CSS to hide Streamlit UI elements and set the background iframe
custom_css = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp {
        background: transparent;
    }
    .background {
        position: fixed;
        top: 0;
        left: 0%;
        height: 100%;
        width: 100%;
        z-index: -1;
        overflow: hidden;
    }
    .foreground {
        position: relative;
        z-index: 1;
    }
    .iframe {
        position: fixed;
        top: 0;
        left:0;
        height: 100%;
        width: 100%;
        border: none;
        z-index: -1;
    }
    </style>
"""
# <iframe src="https://openprocessing.org/sketch/2065046/embed/"    width="100%" height="100%"></iframe>
#<iframe src="https://openprocessing.org/sketch/2065046/embed/"    width="100%" height="100%"></iframe>
#<iframe src="https://openprocessing.org/sketch/2284187/embed/" width="100%" height="100%"></iframe>
# HTML to embed the OpenProcessing iframe
openprocessing_iframe = """
    <div class="background">
        <iframe src="https://openprocessing.org/sketch/2257597/embed/" width="100%" height="100%"></iframe>
    </div>
"""

# Inject the CSS and HTML into the Streamlit app
st.markdown(custom_css, unsafe_allow_html=True)
st.markdown(openprocessing_iframe, unsafe_allow_html=True)

# Wrap your Streamlit content inside a div with the 'foreground' class
st.markdown('<div class="foreground">', unsafe_allow_html=True)

# Add your Streamlit menu here
st.title("O Meu Portefolio")
st.write("DSIGN | WEB | 3D | GAME DESIGN | PYTHON")

# Create a sidebar menu
menu = st.sidebar.radio("Menu", ["Gallery 1", "Gallery 2", "Gallery 3"])

# Depending on the menu selection, show different galleries
if menu == "Gallery 1":
    st.header("Gallery 1")
    cols = st.columns(3)
    with cols[0]:
         st.title("DSIGN")
    with cols[1]:
         st.title("WEB")
    with cols[2]:
         st.title("3D")
        
    with cols[0]:
        st.image("5.png", caption="Image 1")
    with cols[1]:
        st.image("4.png", caption="Image 2")
    with cols[2]:
        st.video("7.mp4", caption="Image 3")

        st.header("Gallery 1")
    cols = st.columns(3)
    with cols[0]:
         st.title("DSIGN")
    with cols[1]:
         st.title("WEB")
    with cols[2]:
         st.title("3D")
        
    with cols[0]:
        st.image("2.png", caption="Image 1")
    with cols[1]:
        st.image("3.png", caption="Image 2")
    with cols[2]:
        st.image("2.png", caption="Image 3")
elif menu == "Gallery 2":
    st.header("Gallery 2")
    cols = st.columns(3)
    with cols[0]:
        st.image("3.png", caption="Image 4")
    with cols[1]:
        st.image("2.png", caption="Image 5")
    with cols[2]:
        st.image("3.png", caption="Image 6")
elif menu == "Gallery 3":
    st.header("Gallery 3")
    cols = st.columns(3)
    with cols[0]:
        st.image("2.png", caption="Image 7")
    with cols[1]:
        st.image("3.png", caption="Image 8")
    with cols[2]:
        st.image("2.png", caption="Image 9")

# Additional content can be added below
st.write("You can add more content and interactive elements here.")

# Close the 'foreground' div
st.markdown('</div>', unsafe_allow_html=True)
