"""One Star, Five Stars for the Food.

Writes a single-sentence, one-star review of Earth from an alien tourist
who cannot help complimenting the food.
"""

import os

ENTRY = (
    "One star: your planet is overcrowded, overheating, and run by "
    "creatures who queue for brunch, but the nasi goreng alone nearly "
    "made me defect from my own species."
)


def main() -> None:
    # Guard the gate before writing: one sentence, 1-200 characters.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside gate"
    assert text.count(".") == 1, "entry must be exactly one sentence"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
