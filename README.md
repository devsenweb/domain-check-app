# 4-Letter Domain Name Generator

This tool generates all possible 4-letter domain name combinations and filters them using customizable rules to identify catchy, pronounceable, and brandable names. It is designed for entrepreneurs, product builders, domain investors, and branding professionals seeking short and memorable domain names, especially in tech and AI-related spaces.

---

## Features

- Generates all 456,976 possible 4-letter combinations (A–Z)
- Filters results based on:
  - Presence of at least one vowel
  - No repeating characters (e.g., no "zz", "aa", etc.)
  - Preferred endings such as `x`, `z`, `o`, `n`, `r`
  - Optional GenAI-style patterns like "ai", "ml", "nn"
- Saves two output files:
  - `all_4_letter_names.txt`: Full list (comma-separated)
  - `cooler_4_letter_names.txt`: Filtered list (line-separated)
- Easily extensible for adding domain availability checks

---

## Sample Output

**cooler_4_letter_names.txt**
```
vaix
gair
zuno
ymox
givo
fayo
nilo
xair
```

---

## Getting Started

### Clone the repository

```bash
git clone https://github.com/devsenweb/domain-name-generator-app.git
cd domain-name-generator-app
```

### Ensure you have Python 3.7+

You can check your Python version with:

```bash
python --version
```

If Python is not installed, [download it here](https://www.python.org/downloads/).

---

## How to Run the App

### Step 1: From the root folder, run the script

```bash
python -m src.main
```

This will generate two files in your project root:

- `all_4_letter_names.txt`
- `cooler_4_letter_names.txt`

Each time you run the script, it will overwrite these files with fresh output.

---

## Project Structure

```
domain-name-generator-app/
├── src/
│   └── main.py
├── all_4_letter_names.txt
├── cooler_4_letter_names.txt
├── README.md
```

---

## Git Commands to Push Changes (PowerShell Friendly)

Use this to stage, commit, and push your changes:

```powershell
git add .; git commit -m "Update: refined filters and README"; git push origin main
```

To push only if commit succeeds:

```powershell
git add .; if (git commit -m "Update filters") { git push origin main }
```

---

## Future Enhancements

- Add API-based domain availability checks
- Add CLI options for filters and output formats
- Add web interface to view and explore results
- Add scoring and ranking logic for brand appeal

---

## License

This project is licensed under the MIT License.
