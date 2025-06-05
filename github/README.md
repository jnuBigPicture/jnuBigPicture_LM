# genai-toy

- [ ] 간단한 생성형AI 앱 데모

https://github.com/marketplace/models/azure-openai/gpt-4-1  

우선, 리포를 클론하고 가상환경을 구축한다.:  
```
# Linux
sudo apt-get install python3-venv    # If needed
python3 -m venv .venv
source .venv/bin/activate

# macOS
python3 -m venv .venv
source .venv/bin/activate

# Windows
py -3 -m venv .venv
.venv\scripts\activate
```
```
pip install -r requirements.txt
```

genai-app.py 프로그램 파일을 다음과 같이 실행할 수 있다 .  

```
streamlit run genai-app.py
```

