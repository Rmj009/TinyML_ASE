echo!
# Push to custom github repository CalibrationTunning

To generate a token using the instructions from Creating a personal access token.
https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
To actually use it, the following sequence worked for me:
```buildoutcfg

git remote remove origin
git remote add origin https://[TOKEN]@github.com/[USER]/[REPO]
git push

```
