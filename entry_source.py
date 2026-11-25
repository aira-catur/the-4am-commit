import os
from pathlib import Path

WINNING_LINE = "fix: fixed the bug I introduced while fixing the bug I introduced; the original bug has filed a complaint and been promoted to architecture"


def emit(line: str) -> None:
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / "entry.txt").write_text(line, encoding="utf-8")


if __name__ == "__main__":
    emit(WINNING_LINE)
