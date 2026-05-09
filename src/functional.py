def format_text(text: str, style: str) -> str:
    if style == "upper":
        return text.upper()
    elif style == "lower":
        return text.lower()
    elif style == "title":
        return text.title()
    elif style == "reverse":
        return text[::-1]
    else:
        raise ValueError(f"Unknown style: {style}")
