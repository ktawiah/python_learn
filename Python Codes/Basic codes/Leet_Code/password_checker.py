import re


def verify_sentence(sentence: str) -> str:
    sentence_regex = (
        r"^[a-zA-Z0-9]+(\s)?[+-/*%]+(\s)?[a-zA-Z0-9]+(\s)?[<=<]+(\s)?[a-zA-Z0-9]+"
    )
    if re.fullmatch(sentence_regex, sentence):
        return "Success"
    return "Failure"


print(verify_sentence("x - y = 4"))
