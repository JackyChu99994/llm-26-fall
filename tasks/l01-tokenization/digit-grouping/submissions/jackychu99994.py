"""

PREDICTIONS = {
    "3.14159": ["3", ".", "141", "59"],
    "Room 101": ["Room ", "101"],
    "2024-09-16": ["202", "4", "-", "09", "-", "16"],
}

MY_CASES = [
    ("007哈吉米00114514", ["007", "哈吉米", "001", "145", "14"]),
    ("\n335没问\t题", ["\n", "335", "没问\t题"]),
]



def solve(text: str) -> list[str]:
    """原样保留非数字段，把连续十进制数字从左向右按三位分组。"""
    chunks = []
    i = 0
    while i < len(text):
        start = i
        is_digit = text[i].isdecimal()
        # 找到同一类别的整段字符，空格和换行也属于非数字。
        while i < len(text) and text[i].isdecimal() == is_digit:
            i += 1
        if is_digit:
            for position in range(start, i, 3):
                chunks.append(text[position:min(position + 3, i)])
        else:
            chunks.append(text[start:i])
    return chunks
