from .generator import Generator
from .retrieval import Retrieval


class ChatBot:
    def __init__(self) -> None:
        self.retrieval = Retrieval()
        self.generator = Generator()

    def respond(self, query: str, debug: bool = False) -> str:

        retrieved = self.retrieval.retrieve(query)

        prompt: str = f"You are a helpful assistant.<｜User｜>{query}<｜Assistant｜>"

        if retrieved:
            prompt = f"<system> Use this information: {retrieved}\n\n" + prompt

        if debug:
            print("===prompt===")
            print(prompt)
            print("============")

        chunk_list: list[str] = []
        stream = self.generator.generate(prompt)

        print("------thinking--------\n", flush=True, end="")
        for chunk in stream:
            print(chunk, flush=True, end="")
            chunk_list.append(chunk)
        print("\r" + " " * 20 + "\r", end="", flush=True)

        return "".join(chunk_list)

    def converse(self) -> None:
        while True:
            query = input("<< ")
            answer = self.respond(query)
            print(f">> {answer}")
