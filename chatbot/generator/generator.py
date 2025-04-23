from typing import Iterator


class Generator:
    def __init__(self) -> None:
        # ###
        # 주석을 지우고 __init__ 을 자유롭게 활용하자.
        # ###
        pass

    def generate(self, prompt: str) -> Iterator[str]:
        # ###
        # 주석을 지우고 다음 기능을 완성하자.
        # generate 는 단순 prompt 뒤에 이어질 "자연스러운" 말을 리턴하면 된다.
        # 단, 토큰을 하나하나 출력하기 위해서는 Iterator 로 리턴해야한다.
        # yield 개념을 모른다면 공부해보자!
        #
        # 예시 1:
        # prompt: I want
        # @return: " to be a doctor"
        #
        # 예시 2:
        # prompt: Pizza is
        # @return: " so delicious"
        # ###

        text = "This is a sample answer. Replace this with your answer"
        from time import sleep

        for chunk in text.split():
            sleep(0.1)
            yield chunk
            yield " "
