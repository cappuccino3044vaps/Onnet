from llama_cpp import Llama

llm = Llama(model_path="../models/ELYZA-japanese-Llama-2-7b-instruct-q2_K.gguf", n_gpu_layers=30)

while True:
    user_input=input("You:")
    if user_input.lower()in["q"]:
        break
    response=llm(user_input,max_tokens=128)
    text=response['choices'][0]['text']
    print(f"LLM:{text}")