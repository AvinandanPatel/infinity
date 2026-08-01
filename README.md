# Team Name: Infinity

This repository contains Team Infinity's data analysis, predictive modeling, and policy recommendations for the Datathon.

## Team

- Team name: Infinity
- Members: 3 (Avinandan Patel, Aman Rajput, Me Me Khaing)
- Track(s) addressed: Data Insights & Visualization / Predictive Analytics / Policy & Intervention Design
- Contact email: avinandan.patel@iiitb.ac.in
- Language used: Python

## AI and LLM use is restricted

AI or LLM tools (ChatGPT, Claude, Copilot, Gemini, and so on) must not be used
to generate your analysis, findings, report, slides, or policy recommendations.
The analytical and written work must be your team's own.

The only tolerated use is basic coding assistance, such as editor autocomplete
or looking up syntax and error messages. It must not extend to producing the
analysis or the written deliverables.

Reports and notes are checked for signs of AI generation, and all numbers are
independently fact-checked. Submissions that appear substantially AI-generated
may be disqualified.

## What's in this repo

| File / folder | Purpose |
|---|---|
| `report.pdf` | Main findings report (replace the placeholder) |
| `slides.pptx` | Your filled-in 12-slide solution deck |
| `docs/policy_note.pdf` | Recommendations note |
| `src/run_all.py` | Single entry point. Running this reproduces everything in `outputs/` by executing our main notebook |
| `requirements.txt` | Python packages needed to run our analysis |
| `Data_Analysis.ipynb` | Our main Jupyter Notebook containing the data analysis and modeling |
| `data/` | Where the organizer dataset goes. Git-ignored, never commit data |
| `manifest.yml` | Lists every file your submission produces |
| `claims.json` | Every factual or numeric claim in your report, with how it can be checked |
| `outputs/` | Generated tables, figures, dashboard, and predictions |
| `Dockerfile` | Optional. Containerizes your entry point for a reproducibility bonus |

## How to run this

**Python teams:**

```bash
pip install -r requirements.txt
python src/run_all.py
```

