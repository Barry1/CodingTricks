---
title: Tipps and Tricks for using Git and REpos
author: Dr. Bastian Ebeling
date: 26.03.2023
---

[ghtokens]: https://github.com/settings/tokens
[ghcredstore]: https://git-scm.com/docs/git-credential-store

## Authentification for CLI

If acceptable for your environment, run

```sh
git config --global credential.helper store
```

to enable storing of passwords.

### For usin GitHub

The open the [URL][ghtokens] to create a token.
After logging in the first time with you Username and the Token as Password, you will no longer be asked for login credentials.

For further details see [here][ghcredstore].
