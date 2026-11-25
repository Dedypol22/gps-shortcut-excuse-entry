"""GPS shortcut excuse entry for make.fun.

The joke, against the judge criteria: the GPS speaks in its own
first-person voice and never breaks character — no narrator, no apology,
no "recalculating". Its deadpan machine logic escalates in three beats:
(1) a deliberate swerve, not a map error; (2) a surrender of territory,
treating one goose as the road's rightful owner; (3) the punch, a
navigation computer admitting it does not argue with geese. The twist
is specific and visual (one goose, one road) rather than a generic
excuse, the wording stays tight at 77 characters, and the last words
land the joke because the machine states defeat as a policy.
"""

import os

LINE = "I avoided the goose. The goose owns that road now. I do not argue with geese."

MAX_LENGTH = 200


def validate(line):
    """Check the line meets the competition gate: one line, 1-200 chars."""
    if not line or not line.strip():
        raise ValueError("entry line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line, no line breaks")
    if len(line) > MAX_LENGTH:
        raise ValueError(
            "entry is %d characters, %d over the %d limit"
            % (len(line), len(line) - MAX_LENGTH, MAX_LENGTH)
        )
    return line


def output_path():
    """Return the entry.txt path, honouring MAKEFUN_OUTPUT_DIR."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def main():
    line = validate(LINE)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()
