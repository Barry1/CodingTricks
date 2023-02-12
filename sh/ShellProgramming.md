---
title: Hints and Ideal for Shell Programming
author: Dr. Bastian Ebeling
date: 06.01.2023
---

### single or double bracket

When to use `[` or `[[`? And what is the difference?
First to mention: `type [` says it is a shell internal function while `type [[` says that it is a keyword.
While `[` is POSIX-compliant, `[[` is not, but sometimes it makes live easier.
Simple example

```bash
[[ 1 < 3 ]]
```

is true while

```bash
[ 1 < 3 ]
```

interprets the `<` to be a file redirection operator and thus you need to quote is as

```bash
[ 1 \< 3 ]
```

You can read more details [here](https://www.baeldung.com/linux/bash-single-vs-double-brackets).
To make sure archived also [here](https://web.archive.org/web/https://www.baeldung.com/linux/bash-single-vs-double-brackets) and [here](https://archive.ph/bcpgl).
