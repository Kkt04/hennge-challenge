# HENNGE Coding Challenge

## Project Structure

```
hennge-challenge/
├── main.py          ← Mission 1: Algorithm solution (UPLOAD THIS TO GITHUB GIST)
├── submit.py        ← Mission 3: Submission script  (RUN LOCALLY, DO NOT SHARE)
├── test_main.py     ← Local test runner             (for your own testing only)
└── README.md        ← This file
```

---

## Step-by-Step Guide

### STEP 1 — Test main.py locally

```bash
cd hennge-challenge

# Run the automated tests
python test_main.py

# Or test manually with the sample input
echo "2
4
3 -1 1 10
5
9 -5 -5 -10 10" | python main.py
# Expected output:
# 1
# 11250
```

---

### STEP 2 — Publish as a Secret GitHub Gist (Mission 2)

1. Go to https://gist.github.com
2. Log in to your GitHub account
3. In the filename box, type exactly: `main.py`
4. Paste the ENTIRE contents of `main.py` into the code box
5. Click the dropdown arrow next to "Create gist" → select **"Create secret gist"**
6. Copy the URL from your browser — it looks like:
   `https://gist.github.com/yourusername/abc123def456`

---

### STEP 3 — Submit via HTTP POST (Mission 3)

1. Open `submit.py`
2. Fill in the top 2 variables:
   ```python
   GITHUB_URL = "https://gist.github.com/YOUR_ACCOUNT/YOUR_GIST_ID"
   EMAIL      = "your@email.com"
   ```
3. Run it:
   ```bash
   python submit.py
   ```
4. You should see: `✓ SUCCESS! Status: 200`

> **If you get 401 Unauthorized**: The TOTP token is time-based (30-second window).
> Just run `python submit.py` again immediately.

---

## How the Algorithm Works (main.py)

**Problem:** For each test case, raise each number to the power of 4,
but EXCLUDE positive numbers. Sum the results. Print -1 if count mismatches.

**Constraints obeyed:**
- No `for` or `while` loops → uses recursion instead
- No list/set/dict comprehensions → uses recursive accumulator functions
- Single file with a `main()` function
- Only standard library (`sys`)

**Example walkthrough:**
```
Input:  4 numbers → 3 -1 1 10
Filter positives → keep only: -1
Calculate: (-1)^4 = 1
Output: 1

Input:  5 numbers → 9 -5 -5 -10 10
Filter positives → keep: -5 -5 -10
Calculate: (-5)^4 + (-5)^4 + (-10)^4 = 625 + 625 + 10000 = 11250
Output: 11250
```

## How the TOTP Works (submit.py)

Per RFC 6238 with these custom settings:
- Hash: HMAC-SHA-512 (not the default SHA-1)
- Step: 30 seconds, T0 = 0
- Secret: `your@email.com` + `HENNGECHALLENGE004`
- Output: 10-digit code used as the HTTP Basic Auth password# hennge-challenge
