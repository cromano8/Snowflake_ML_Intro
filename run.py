import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(override=True)

notebooks = sorted(
    Path("notebooks").glob("*.ipynb"), key=lambda f: int(f.name.split("_")[0])
)

for notebook in notebooks:
    with open(notebook) as f:
        nb = nbformat.read(f, as_version=4)
    ep = ExecutePreprocessor().preprocess(nb, {"metadata": {"path": "notebooks/"}})
