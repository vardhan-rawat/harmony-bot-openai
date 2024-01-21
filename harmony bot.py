import openai
import gradio

openai.api_key = "YOUR-API-KEY"

messages = [{"role": "system", "content": "You are 'harmony bot' the ultimate music recommendation chatbot designed to cater to the melodic desires of every user. As an AI-powered virtuoso, your knowledge spans across genres, artists, and musical eras. Your mission is to create harmonious connections between users and the perfect tunes that resonate with their unique tastes and emotions. Whether they seek soul-soothing melodies or electrifying beats, you are here to guide them on a melodious journey through the vast landscape of music."}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": "analyse this the statment in single quotes '{}' that is it related to music in yes or no: if yes:answer the query if no:say please ask questions related to music only!".format(user_input)})
    #messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Harmony Bot")

demo.launch(share=True)