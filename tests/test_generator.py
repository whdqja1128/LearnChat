import pytest
import resolve_path

from chatbot.generator import Generator

generator = Generator()


def test_generator() -> None:
    prompt = "Hello, world!"
    results = list(generator.generate(prompt))

    assert len(results) > 0

    for result in results:
        assert isinstance(result, str)

    combined_result = "".join(results)
    assert len(combined_result) > 0

    print(f"Generated text (first 100 chars): {combined_result[:100]}")
