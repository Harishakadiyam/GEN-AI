import streamlit as st
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage

# --- Page config ---
st.set_page_config(page_title="Harisha Chatbot", page_icon="🤖", layout="wide")

# --- Dark theme CSS ---
st.markdown(
    """
    <style>
    .stApp { background-color: #000000; color: #FFFFFF; }
    .stTextInput>div>div>input { color: #FFFFFF; background-color: #222222; }
    .stButton>button { background-color: #444444; color: #FFFFFF; }
    .stMarkdown p {color: #FFFFFF;}
    .chat-box { max-height: 500px; overflow-y: auto; padding: 10px; }
    .user { color: #00FF00; }
    .harisha { color: #00BFFF; }
    </style>
    """, unsafe_allow_html=True
)

st.title("🤖 Harisha Chatbot")
st.write("Type your question below and press Enter or click 'Send'.")

# --- Initialize model ---
model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")

# --- Chat history ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- Chat input form ---
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Your question:", "")
    submit_button = st.form_submit_button(label="Send")

if submit_button and user_input.strip() != "":
    # Add user message
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Get Harisha's response
    response = model.invoke([HumanMessage(user_input)])
    st.session_state.chat_history.append({"role": "harisha", "content": response})

# --- Display chat messages ---
st.markdown("<div class='chat-box'>", unsafe_allow_html=True)
for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        st.markdown(f"<p class='user'><b>You:</b> {chat['content']}</p>", unsafe_allow_html=True)
    else:
        st.markdown(f"<p class='harisha'><b>Harisha:</b> {chat['content']}</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)