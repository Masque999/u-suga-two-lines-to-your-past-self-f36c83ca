LINES = [
    "Do not send that email at 2 a.m. on the night before the launch; sleep on it, because you are about to quit over a typo.",
    "That unsent email was the moment I learned anger is a draft, not a decision, and every good job I have had since started with waiting until morning.",
]

# The entry must be exactly two lines, 1-280 characters in total.
TEXT = "\n".join(LINES)
assert 1 <= len(TEXT) <= 280, f"text is {len(TEXT)} chars"
assert TEXT.count("\n") == 1

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)

# Read it back: a silent short write must fail loudly instead of
# passing the gate with a stale or truncated file.
with open("/output/entry.txt", encoding="utf-8") as f:
    assert f.read() == TEXT, "entry.txt does not match TEXT after write"
