import streamlit as st
from github import Github
import google.generativeai as genai
import os
import logging

# Define constants
IGNORE_DIRS = {'node_modules', 'vendor', '.git', 'docs'}
IGNORE_FILES = {'README.md', 'package-lock.json', 'package.json', 'reportWebVitals.js', 'setupTests.js', 'manifest.json', 'robots.txt', 'index.js'}
IGNORE_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.gif', '.svg', '.ico', '.css'}

# Set the API key for Google Gemini
api_key = "AIzaSyAzCjpm-mY4WCfkZnyj5V9NladpSrs3QvQ"

# Check if API key is provided
if not api_key:
    raise ValueError("API key not found. Please set the API_KEY environment variable.")

# Configure logging
logging.basicConfig(level=logging.DEBUG)

try:
    # Configure the API key
    genai.configure(api_key=api_key)
    logging.debug("API key configured successfully.")
except Exception as e:
    st.error(f"Error configuring API key: {e}")
    logging.error(f"Error configuring API key: {e}")

# Function to authenticate to GitHub
def authenticate_github(token):
    if not token:
        st.error("Please provide a GitHub token.")
        return None
    return Github(token)

# Function to get repository
def get_repository(g, user, repo_name):
    try:
        repo = g.get_repo(f"{user}/{repo_name}")
        return repo
    except Exception as e:
        st.error(f"Error fetching repository: {e}")
        return None

# Function to get file content
def get_file_content(repo, file_path):
    try:
        file_content = repo.get_contents(file_path)
        return file_content.decoded_content.decode()
    except Exception as e:
        st.error(f"Error reading file {file_path}: {e}")
        return None

# Function to recursively fetch all files
def fetch_files(repo, contents, path=""):
    files = []
    for content_file in contents:
        if content_file.type == "dir":
            if content_file.name not in IGNORE_DIRS:
                files.extend(fetch_files(repo, repo.get_contents(content_file.path), path=content_file.path))
        else:
            if content_file.name not in IGNORE_FILES and not any(content_file.path.endswith(ext) for ext in IGNORE_EXTENSIONS):
                file_content = get_file_content(repo, content_file.path)
                if file_content:
                    files.append((content_file.path, file_content))
    return files

def get_gemini_response(prompt):
    try:
        # Initialize the model
        model = genai.GenerativeModel('gemini-1.5-flash')
        logging.debug("Model initialized successfully.")

        # Generate content
        response = model.generate_content(prompt)
        logging.debug("Content generated successfully.")
        return response.text
    except Exception as e:
        st.error(f"Error generating response: {e}")
        logging.error(f"Error generating response: {e}")
        return None

def generate_readme(prompt, code):
    """
    Generate the README based on the code and prompt.
    """
    try:
        prompt_template = f"""
        I am creating a README file for my project, which is an expense tracker application.
        Below is the code for the project.
        Please generate the content for each section based on the code provided:
        
        1. Project Title and Description
        2. Features
        3. Installation Instructions
        4. Usage Instructions
        5. Contributing Guidelines
        6. License Information
        7. Contact Information

        Here is the code:
        {code}
        """

        response = get_gemini_response(prompt_template)
        return response
    except Exception as e:
        st.error(f"Error generating README: {e}")
        return None

# Streamlit UI
st.set_page_config(page_title="GeneReadme.md", page_icon='🤖', layout='wide')

# Sidebar for recent README files
st.sidebar.header("Recent README Files")
recent_readme = ["README1.md", "README2.md", "README3.md"]

# Display recent README files in the sidebar as clickable links
for readme in recent_readme:
    link = f'<a href="#" class="left--links" style="text-decoration:none;color:white">{readme}</a>'
    st.sidebar.markdown(link, unsafe_allow_html=True)

# Main section with form
st.header("Generate Readme.md 🤖")

# Create form for user input
with st.form(key='form'):
    access_token = st.text_input("Access Token")
    repo_name = st.text_input("Repository Name")
    username_github = st.text_input("GitHub Username")
    submit = st.form_submit_button("Generate")

# Initialize variables for readme content and buttons
readme_content = ""
show_buttons = False

# Generate response
if submit:
    if access_token and repo_name and username_github:
        github_instance = authenticate_github(access_token)
        if github_instance:
            repo = get_repository(github_instance, username_github, repo_name)
            if repo:
                st.write("Fetching files...")
                contents = repo.get_contents("")

                all_files = fetch_files(repo, contents)
                combined_contents = "\n".join(content for _, content in all_files)
                
                # Generate README
                readme_content = generate_readme("Generate the README for the project", combined_contents)
                show_buttons = True
    else:
        st.error("Please provide valid GitHub credentials.")

# Display the generated README and buttons if available
if show_buttons:
    st.write("### Generated README")
    st.text_area("Generated Documentation", value=readme_content, height=600, key="readme_content")

    # Container for buttons aligned to the right
    col1, col2 = st.columns([3, 1])
    with col1:
        st.download_button(
            label="Download README",
            data=readme_content,
            file_name="README.md",
            mime="text/markdown",
            key="download-readme"
        )
    # with col2:
    #     # Copy to clipboard functionality using JavaScript
    #     st.markdown("""
    #     <script>
    #     function copyToClipboard() {
    #         const textArea = document.getElementById('readme-content');
    #         textArea.select();
    #         document.execCommand('copy');
    #     }
    #     </script>
    #     <button onclick="copyToClipboard()">Copy to Clipboard</button>
    #     """, unsafe_allow_html=True)