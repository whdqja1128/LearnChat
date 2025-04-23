from typing import Iterator
from llama_cpp import Llama


class Generator:
    def __init__(self) -> None:
        pass

    def generate(self, prompt: str) -> Iterator[str]:
        llm = Llama.from_pretrained(
            repo_id="bartowski/DeepSeek-R1-Distill-Qwen-1.5B-GGUF",
            filename="DeepSeek-R1-Distill-Qwen-1.5B-IQ2_M.gguf"
        )
        stream = llm(prompt, max_tokens=80, stream=True)

        for chunk in stream:
            if chunk["choices"][0]["finish_reason"] == "stop":
                break
            yield chunk["choices"][0]["text"]


if __name__ == "__main__":
    generator = Generator()
    for text in generator.generate("Hello, how are you?"):
        print(text, end="")
    print()
