from groq import Groq

GROQ_API_KEY = "YOUR GROQ IP KEY"
client = Groq(api_key=GROQ_API_KEY)

class Chatbot:

    def get_response(self, user_input):
        completion_response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": user_input}],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )

        # Iterate over the streamed response and accumulate content
        completion_content = ""
        for chunk in completion_response:
            if chunk.choices and chunk.choices[0].delta.content:
                completion_content += chunk.choices[0].delta.content

        return completion_content

if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("What are snakes.")
    print(response)
