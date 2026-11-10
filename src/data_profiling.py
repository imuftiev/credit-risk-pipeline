from pathlib import Path
import pandas as pd
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
sh = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s - %(message)s')
sh.setFormatter(formatter)
log.addHandler(sh)


def ingest_data(path: Path) -> None:
    data = pd.read_csv(path)
    print(data)

ingest_data(Path('data/raw/credit_risk_dataset.csv'))
