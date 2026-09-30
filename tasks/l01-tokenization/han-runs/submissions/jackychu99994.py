
PREDICTIONS = {
    "Kimi K2 的 tokenizer": ["Kimi", " ", "K2", " ", "的", " ", "tokenizer"],
    "2026年9月16日": ["2026", "年", "9", "月", "16", "日"],
    "GPT-4o很强": ["GPT", "-", "4o", "很强"],
}

MY_CASES = [
    ("用GPT和GPT用", ["用", "GPT", "和", "GPT", "用"]),
    ("㐀é🙂中A9\t\n１", ["㐀é🙂", "中", "A9", "\t\n", "１"]),
]


def solve(text: str) -> list[str]:

    def category(character: str) -> int:
        if "\u4e00" <= character <= "\u9fff":
            return 0
        if ("A" <= character <= "Z" or "a" <= character <= "z"
                or "0" <= character <= "9"):
            return 1
        if character.isspace():
            return 2
        return 3

    chunks = []
    i = 0
    while i < len(text):
        start = i
        current_category = category(text[i])
        while i < len(text) and category(text[i]) == current_category:
            i += 1
        chunks.append(text[start:i])
    return chunks
