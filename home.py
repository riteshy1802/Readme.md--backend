import streamlit as st

# Set the page configuration
st.set_page_config(page_title="GeneRead.me", page_icon=":book:", layout="wide")

# Custom CSS to center text and layout
st.markdown("""
    <style>
        .main {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }
        .section {
            display: flex;
            justify-content: center;
            gap:2%;
            align-items: center;
            width: 80%;
            margin-top: 50px;
        }
        .right {
            width: 48%;
            margin-top:20%
        }
        .left{
            width:100%
        }
        .github-button {
            display: flex;
            align-items: center;
            justify-content:center;
            padding: 10px;
            font-size:1.2rem;
            border-radius: 5px;
            background-color: #000;
            color: #fff;
            width:100%;
            text-align:center;
            text-decoration: none !important;
        }
        .github-button::hover{
            color:grey;
        }
        .github-button img {
            margin-right: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Header section
st.markdown("<h1 style='text-align: center;'>GeneRead.me</h1>", unsafe_allow_html=True)

# Central section layout
left, right = st.columns([1, 1])

with left:
    # st.markdown("<p style='font-size: 18px;'>Make your projects more <span style='color: blue; font-weight: bold;'>Expressive</span></p>", unsafe_allow_html=True)
    st.image("documents2.png", width=450)

with right:
    st.markdown("<p style='font-size: 18px; text-align: center; margin-bottom: 20px;'>Make your projects more Expressive</p>", unsafe_allow_html=True)
    st.markdown("""
        <a href="https://github.com/login/oauth/authorize?client_id=YOUR_CLIENT_ID" class="github-button">
            <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub Logo" style="width: 40px; height: 40px;border-radius:50%" />
            Authorize with GitHub
        </a>
    """, unsafe_allow_html=True)
