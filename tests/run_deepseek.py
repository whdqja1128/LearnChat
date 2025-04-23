import resolve_path
from llama_cpp import Llama
from typing import Iterable


def generate(prompt: str) -> Iterable:

    llm = Llama.from_pretrained(
        repo_id="bartowski/DeepSeek-R1-Distill-Qwen-1.5B-GGUF",
        filename="DeepSeek-R1-Distill-Qwen-1.5B-IQ2_M.gguf",
    )
    stream = llm(prompt, max_tokens=80, stream=True)

    for chunk in stream:
        yield chunk["choices"][0]["text"]


if __name__ == "__main__":
    sentence_part = "I want to be a doctor because"
    stream = generate(sentence_part)

    # Test 1. test generated
    print(f"Test 1. below is a generated text from a text ({sentence_part})")
    for chunk in stream:
        print(chunk, flush=True, end="")
    print()
