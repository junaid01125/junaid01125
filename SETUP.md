# Setup

This folder is your GitHub profile repository. It must be named exactly `junaid01125` and be **public**.

## First-time push

```bash
cd junaid01125
git init
git add .
git commit -m "Add profile README with animated player card"
git branch -M main
git remote add origin https://github.com/junaid01125/junaid01125.git
git push -u origin main
```

If you already created the repo on GitHub with a README, run `git pull origin main --allow-unrelated-histories` before pushing, and keep this version of `README.md` if Git asks.

## Turn on the contribution snake

1. On GitHub, open the repo, then **Settings → Actions → General**.
2. Under **Workflow permissions**, choose **Read and write permissions** and save.
3. Open the **Actions** tab, pick **Generate contribution snake**, and press **Run workflow**.
4. After it finishes, the snake shows on your profile (it can take a few minutes).

## Change the card

Edit the stats at the top of `tools/build_card.py`, then run:

```bash
python tools/build_card.py
```

The overall rating is the average of the stats. To use a different picture, replace `tools/avatar.jpg` (a square image works best). Commit the new `card.svg` and push.

## Notes

- The card is a self-contained animated SVG, since GitHub does not run JavaScript. It spins open each time the profile loads.
- The stats and streak cards come from free public services that sometimes go down. If one shows as broken, delete its line in `README.md`.
- If you push a new `card.svg` and still see the old one, hard refresh the page (Ctrl+Shift+R).
