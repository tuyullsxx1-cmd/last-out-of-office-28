from pathlib import Path

# The resignation, in four sips.
OPENING = "Thank you for your email. I have left the company to become a barista. "
MIDDLE = "Your ticket has been converted into a latte. "
DETAIL = "It has oat milk, a heart drawn in foam, and absolutely no SLA. "
CLOSING = "Please direct all further complaints to the tip jar."
MESSAGE = OPENING + MIDDLE + DETAIL + CLOSING

# One auto-reply, one line, no line breaks smuggled inside.
assert MESSAGE.count("\n") == 0
# Brief cap for this bounty: at most 280 characters.
assert 1 <= len(MESSAGE) <= 280
# The barista's exit has to mention the latte the ticket became.
assert "latte" in MESSAGE
# Second pass: the tip jar is the punchline, so the closing stays last.
assert MESSAGE.endswith("tip jar.")

Path("/output").mkdir(parents=True, exist_ok=True)
Path("/output/entry.txt").write_text(MESSAGE + "\n", encoding="utf-8")
