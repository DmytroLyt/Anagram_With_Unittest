def reverse_word(word: str):
    remove_symbols = [symbol for symbol in word if symbol.isalpha()]
    reversed_word = []
    for symbol in word:
        if symbol.isalpha():
            reversed_word.append(remove_symbols.pop())
        else:
            reversed_word.append(symbol)
    reversed_sent = ''.join(reversed_word)
    return reversed_sent


def reverse_sentence(text: str):
    if not isinstance(text, str):
        raise AttributeError("Text must be a string")

    text_list = text.split(' ')
    reversed_text = []
    for word in text_list:
        reversed_text.append(reverse_word(word))
    reverse_text = ' '.join(reversed_text)
    return reverse_text


if __name__ == '__main__':
    user_text = "Her1e is4 my! t!ext"
    print(reverse_sentence(user_text))
