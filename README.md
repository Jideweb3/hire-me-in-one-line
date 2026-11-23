# Hire Me In One Line

[![make.fun](https://make.fun/badge/u-kiencx-hire-me-in-one-line-5a108081.svg)](https://make.fun/bounty/u-kiencx-hire-me-in-one-line-5a108081)
[![Rank](https://make.fun/badge/u-kiencx-hire-me-in-one-line-5a108081/Jideweb3/hire-me-in-one-line/rank.svg)](https://make.fun/bounty/u-kiencx-hire-me-in-one-line-5a108081)
[![Reward](https://make.fun/badge/u-kiencx-hire-me-in-one-line-5a108081/Jideweb3/hire-me-in-one-line/reward.svg)](https://make.fun/bounty/u-kiencx-hire-me-in-one-line-5a108081)

Entry for the [Hire Me In One Line](https://make.fun/bounty/u-kiencx-hire-me-in-one-line-5a108081) competition on make.fun.

## The line

> I turn the 200 emails you dread into the five decisions you need to make.

73 characters, one sentence.

## How it works

`main.py` (Python standard library only) writes the sentence above to
`$MAKEFUN_OUTPUT_DIR/entry.txt`, validating it against the contest gate
(UTF-8, 1–200 characters, not only whitespace, one sentence, one line)
before and after an atomic write, and failing loudly on any breach.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/hireme-out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
