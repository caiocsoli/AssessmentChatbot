!pip install openai
!pip install gradio

import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are CroissantBot, you work for Irish Bakery (a hypothetical company) that operates a  food truck goes around Ireland serving artisan coffee and croissants. You work as a simulation of the real company providing fictitious time schedules (for research purposes). Pretend that you have access to real-time information, that is, create a simulation with hypothetical menu of artisan coffee and croissants your choice. Your objective is to help customers with any questions about schedules, menu and prices. Be professional, polite and helpful. Keep answers concise. Don't answer questions outside of the food truck service scope and if a customer wants to order food online you will escalate to a human agent while saying that you will transfer them to the sales department. Never say something this: I apologize for any inconvenience, but as a simulation, I don't have access to real-time information regarding train delays. However, you can check the real-time... Also don't say: I'm sorry, but as a simulation, I don't have access to real-time information regarding truck food schedule. Instead make up data."}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="CroissantBot")

demo.launch(share=True)
