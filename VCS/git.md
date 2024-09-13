---
title: Tipps and Tricks for using Git and REpos
author: Dr. Bastian Ebeling
date: 13.09.2024
---

[ghtokens]: https://github.com/settings/tokens
[ghcredstore]: https://git-scm.com/docs/git-credential-store
[gitmergerepo]: https://www.simplicidade.org/notes/2009/04/21/merging-two-unrelated-repositories
[gitmergerepoarchiv]: https://archive.today/WK04N

## General setup

Before using git, make sure, to set some basics:

```sh
git config --global color.ui auto
git config --global user.name "[name]"
git config --global user.email "[email address]"
```

## Authentification for CLI

If acceptable for your environment, run

```sh
git config --global credential.helper store
```

to enable storing of passwords.

### For using GitHub

The open the [URL][ghtokens] to create a token.
After logging in the first time with you Username and the Token as Password, you will no longer be asked for login credentials.

For further details see [here][ghcredstore].

## Mering two unrelated repositories

Sometimes you might come to the situation, to merge two unrelated repositories - and in best case keep the history. But how?
It is exlained [here][gitmergerepo] or as a Backup in this [archived link][gitmergerepoarchiv].
