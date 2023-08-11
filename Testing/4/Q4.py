from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
import nltk


def tagging(text):
    tokens = word_tokenize(text)
    tags = pos_tag(
        tokens,
    )
    name_lists = []
    index = 0
    while index < len(tags):
        if tags[index][1] == "NNP":
            temp_name = tags[index][0] + " "
            index += 1
            while tags[index][1] == "NNP":
                temp_name += tags[index][0] + " "
                index += 1
            name_lists.append(temp_name.strip())
        else:
            name_lists.append(tags[index][0])
            index += 1
    return name_lists


print((f"{tagging('Robert Langdon is a famous singer')=}"))


# Path: Testing\4\Q5.py
