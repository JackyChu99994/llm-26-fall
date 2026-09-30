
import re

PREDICTIONS = {
    "don't stop": ["don", "'t", " stop"],
    "x2 + 3x = 0": ["x", "2", " +", " 3", "x", " =", " 0"],
    "It's 3.14": ["It", "'s", " 3", ".", "14"],
}

MY_CASES = [
    ("  I'm\tready!", [" ", " I", "'m", "\t", "ready", "!"]),
    ("we'RE x²_½ ００7", ["we", "'", "RE", " x²", "_", "½", " ００7"]),
]

PATTERN = re.compile(
    r"'s|'t|'re|'ve|'m|'ll|'d"
    r"| ?[^\W\d_]+"
    r"| ?\d+"
    r"| ?(?:(?![^\W\d_]|\d)\S)+"
    r"|\s+(?!\S)"
    r"|\s+"
)


def solve(text: str) -> list[str]:

    return PATTERN.findall(text)
