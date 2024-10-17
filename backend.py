import openai

class ChatBot:
    def __init__(self):
        openai.api_key = "*****************"
        
    def get_response(self, user_input):
        response = openai.completions.create(
            model='gpt-3.5-turbo',
            prompt= user_input,
            max_tokens=2000,
            temperature=0.3
        ).choices[0].text
        
        return response
    
if __name__ == '__main__':
    chatbot = ChatBot()
    response = chatbot.get_response('Write a joke about birds')
    print(response)