from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# OpenAI API 키 설정
openai.api_key = 'YOUE_OPENAIAPI_KEY'

def generate_text(prompt):
    # GPT-3.5를 사용하여 텍스트 생성
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=1000  # 생성할 텍스트의 최대 길이 설정
    )
    return response.choices[0].text.strip()

def generate_image(prompt):
    # DALL·E 3를 사용하여 이미지 생성
    response = openai.Image.create(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response.data[0].url
    return image_url

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if request.method == 'POST':
        user_input = request.form['topic']
        
        # 텍스트 생성
        generated_text = generate_text(user_input)
        
        # 이미지 생성
        generated_image_url = generate_image(user_input)
        
        return render_template('result.html', text=generated_text, image_url=generated_image_url)

if __name__ == '__main__':
    app.run(debug=True)
