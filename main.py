import os
from pathlib import Path

ENTRY = "He pings me at 3 a.m. for life advice. I say sleep. He asks me to rephrase."
MAX_CHARS = 200


def output_path() -> Path:
    override = os.environ.get("MAKEFUN_OUTPUT_DIR")
    return Path(override) if override else Path("/output")


def validate(entry: str) -> bytes:
    if not entry or not entry.strip():
        raise ValueError("entry must not be empty or whitespace only")
    if len(entry) > MAX_CHARS:
        raise ValueError(f"entry is {len(entry)} characters; limit is {MAX_CHARS}")
    return entry.encode("utf-8")


def main() -> None:
    payload = validate(ENTRY)
    directory = output_path()
    if directory.exists() and not directory.is_dir():
        raise NotADirectoryError(directory)
    directory.mkdir(parents=True, exist_ok=True)
    (directory / "entry.txt").write_bytes(payload)


if __name__ == "__main__":
    main()
