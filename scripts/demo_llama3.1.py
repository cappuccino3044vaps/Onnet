from llama_cpp import Llama

llm = Llama(model_path="../models/Meta-Llama-3-8B-Instruct.Q6_K.gguf", n_gpu_layers=10)


out=llm("Q:朝は四本足、昼は二本足、夕は三本足。この生き物は何か？ A: ")

print(out)