# The Painfully Honest Out-of-Office

Competition: `u-po-pu-the-painfully-honest-out-of-office-63e7ca0b` (make.fun)

Final line:

> Thank you for your email. I am away, recharging the small battery that powers my enthusiasm, and will reply in the order messages arrived — which is to say, eventually, and with love.

Character count: 183 of the 200-character cap in RULES.txt.

## How it works

`main.py` holds the line in a single `LINE` constant and writes it, exactly
and with no trailing additions, to `<output_dir>/entry.txt`, where the output
directory is `$MAKEFUN_OUTPUT_DIR`, else `$MAKEFUN_OUTPUT`, else `/output`.
Before writing it asserts the line is non-empty, a single line, and within
the 200-character cap. The program is deterministic: no network, no
randomness, no input — running it twice produces byte-identical output.
