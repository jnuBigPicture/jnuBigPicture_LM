import os
from openai import OpenAI
import streamlit as st
# from langchain_community.llms import OpenAI
token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

st.title('🍎🍐🍊 나의 AI Chat 🥝🍅🍆')
github_api_key = st.sidebar.text_input('GitHub API Key')
def generate_response(input_text):
#  llm = OpenAI(temperature=0.7, github_api_key=openai_api_key)
#  st.info(llm(input_text))

  response = client.chat.completions.create(
    messages=[
      {
        "role": "system",
        "content": "You are a helpful assistant.",
      },
      {
        "role": "user",
        #"content": "What is the capital of France?",
        "content": input_text,
      }
    ],
    temperature=1.0,
    top_p=1.0,
    model=model
  )

  # print(response.choices[0].message.content)
  st.info(response.choices[0].message.content)
with st.form('my_form'):
  text = st.text_area('Enter text:', '무엇을 도와드릴까요?')
  submitted = st.form_submit_button('Submit')
  # if not openai_api_key.startswith('sk-'):
  #   st.warning('OpenAI API 인증키를 입력해 주세요!', icon='⚠')
  # if submitted and openai_api_key.startswith('sk-'):

  if not github_api_key.startswith('ghp_'):
    st.warning('GitHub API 인증키를 입력해 주세요!', icon='⚠')
  if submitted and github_api_key.startswith('ghp_'):
    generate_response("너는 수학과 관련해서만 말할 수 있어\n질문:"+text)
