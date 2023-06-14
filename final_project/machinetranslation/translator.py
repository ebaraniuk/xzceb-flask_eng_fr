from deep_translator import MyMemoryTranslator, GoogleTranslator


def english_to_french(english_text):
    """

    :param english_text:
    :return: french text
    """
    french_text = GoogleTranslator(source='english', target='french').translate(english_text)

    return french_text


def french_to_english(french_text):
    """

    :param french_text:
    :return: english text
    """
    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return english_text
