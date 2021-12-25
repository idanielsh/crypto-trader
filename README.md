# crypto-trader

## Installation

To install packages using a linux terminal:
```
pip3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

## Simulation Mode

- Clone repo from https://github.com/binance/binance-public-data/

- Create new folder for holding data:

```
mkdir data/simulation_data
```

- In the cloned repo, download data to the newly created folder:

```
python3 download-kline.py -s ETHUSDT -startDate 2021-11-25 -i 15m -folder '/path/to/repo/crypto-trader/data/simulation_data'
```
- Extract downloaded data, and paste the folder path of the data in `simulation.py`.

- Run `simulation.py`, which starts with 100$, and prints the final amount of money at the end of the trading script.