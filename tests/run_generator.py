import resolve_path

from chatbot.generator import Generator

generator = Generator()

sentence_part = "Pizza is originated from "
stream = generator.generate(sentence_part)


# Test 1. test generated
print(f"Test 1. below is a generated text from a text ({sentence_part})")
for chunk in stream:
    print(chunk, flush=True, end="")
