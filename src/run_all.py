"""Single entry point for this submission (Python teams).

Running `python src/run_all.py` from the repo root must rebuild every
file listed under `outputs:` in manifest.yml, using only the data the
organizers give you and mention any other data you have used.

Rules this file is set up to follow:
  - Read the dataset from ./data/ (git-ignored, never commit the data).
  - Use paths relative to the repo root, not absolute machine paths.
  - Fix a random seed for anything that uses randomness, so your metrics reproduce.
  - Do not download data or models while the code runs; the judging run is offline.

R teams: delete this file and add src/run_all.R plus renv.lock (or install.R)
instead. Our pipeline will run whichever entry point it finds.
"""
import random
from pathlib import Path

SEED = 42
random.seed(SEED)

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"       # organizer dataset lives here (git-ignored)
OUTPUTS = REPO_ROOT / "outputs"


def main() -> None:
    OUTPUTS.mkdir(exist_ok=True)
    
    import subprocess
    cleaning_notebook = REPO_ROOT / "Cleaning_PD.ipynb"
    analysis_notebook = REPO_ROOT / "Data_Analysis.ipynb"
    
    print(f"Executing {cleaning_notebook.name} to reproduce merged data...")
    try:
        subprocess.run([
            "jupyter", "nbconvert", "--to", "notebook", "--execute",
            "--inplace", str(cleaning_notebook)
        ], check=True)
        print(f"{cleaning_notebook.name} executed successfully. Merged data saved.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing cleaning notebook: {e}")
        raise

    print(f"Executing {analysis_notebook.name} to reproduce outputs...")
    try:
        subprocess.run([
            "jupyter", "nbconvert", "--to", "notebook", "--execute",
            "--inplace", str(analysis_notebook)
        ], check=True)
        print("Execution complete. Outputs reproduced successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing analysis notebook: {e}")
        raise


if __name__ == "__main__":
    main()
