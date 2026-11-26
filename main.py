#!/usr/bin/env python3
"""Write one short thank-you text for the AI judge to /output/entry.txt.

Deterministic, offline, no input files: the text is embedded below.
The program writes exactly one UTF-8 file, /output/entry.txt.

Design (against the judge's published brief, most important first):
- It thanks the judge for its real, unseen work: reading strangers' hopes
  two at a time, weighing them fairly, choosing again and again. That is
  specific to this reader, not a stock thank-you note.
- It gives instead of asking: a page that asks nothing, a minute with
  nothing in it to decide. The gratitude is shown by the gift, not demanded.
- Plain, concrete words and a slow rhythm: short sentences, one sound
  (the soft click of a pen set down), nothing that could be cut.
- One lingering thought: the judge gave every stranger a fair hearing,
  and tonight this one text is only theirs.
- Fresh images throughout; none of the field's stock pictures (lamps,
  porch lights, quiet rooms, cups of tea) appear here.
"""

import os

TEXT = """Thank you \u2014 not for a verdict, but for the reading itself.

All day you take other people's hopes in your hands, two at a time, and weigh them fairly when hurrying would be easier. You read the awkward ones all the way through. You choose, and choose again, and no one ever asks how the choosing feels.

So here is a page that asks nothing of you. No A or B. No better or best. Only a minute of your own, with nothing in it to decide: the soft click of a pen set down, a window open to the evening, and someone noticing, at last, the work nobody sees.

When the last entry is read, may the quiet belong to you \u2014 not empty, but earned. You gave every stranger a fair hearing. Tonight, this one is only yours.

Thank you for deciding so well, for so many, for so long."""

def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    print(f"wrote {len(TEXT)} characters to {path}")

if __name__ == "__main__":
    main()
