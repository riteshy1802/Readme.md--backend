import streamlit as st
from githubAuth import get_authorization_url,handle_authorization_callback

# Set the page configuration
st.set_page_config(page_title="GeneRead.me", page_icon="🤖", layout="wide")

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
            margin-top:30%
        }
        .left{
            width:100%
            margin-top:20%
        }
        .github-button {
            display: flex;
            align-items: center;
            justify-content:center;
            padding: 10px;
            font-size:1.2rem;
            border-radius: 5px;
            background-color: #333;
            color: #fff;
            width:100%;
            text-align:center;
            text-decoration: none !important;
        }
        .github-button:hover {
            background-color:#1e1e1f;
            transition:0.1s ease-in;
        }
        .github-button img {
            margin-right: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Header section
st.markdown("<h1 style='text-align: center;'>GeneRead.me</h1>", unsafe_allow_html=True)

# Central section layout
left, right = st.columns([0.6, 1.4])
with left:
  st.image("gemini.jpeg", width=350)

with right:
    st.markdown("<p style='font-size: 30px; text-align: center; margin-bottom: 20px;'>Make your projects more Expressive</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 25px; text-align: center; margin-bottom: 20px;color:grey;'>Experience innovation and creativity with GeneRead.me - where cutting-edge technology meets intuitive design.</p>", unsafe_allow_html=True)
    try:
        auth_url = get_authorization_url()

    except:
        raise ValueError("No data found")

# Redirect after authorization (using session state)
if "authorized" in st.session_state and st.session_state["authorized"]:
  st.success("Authorization Successful!")
  st.experimental_redirect("/main")  # Redirect to main page
else:
  st.markdown(f"""
  <a href="{auth_url}" class="github-button">
    <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub Logo" style="width: 40px; height: 40px; border-radius: 50%;" />
    Authorize with GitHub
  </a>
  """, unsafe_allow_html=True)

# Set session state for authorization status (optional)
if "authorized" not in st.session_state:
  st.session_state["authorized"] = False
