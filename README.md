# crypto-trader

A project to test cryptocurrency trading strategies.

## Installation

Install packages using a virtualenv on a linux terminal:
```bash
pip3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

## Testing a New Strategy

- Add the relevant indicator to the indicators folder, as a subclass of the `AbstractIndicator` class, with the relevant methods implemented.

- Similarly, add the new strategy to the strategies folder, as a subclass of the `AbstractStrategy` class, with the relevant methods implemented.

- Import this new strategy in `simulate.py`, and change the strategy on line 39.

- Run the steps in [Downloading Historical Market Data](#Downloading-Historical-Market-Data) to download the relevant data.

- Run `simulation.py`, which starts with $100, and prints the final amount of money at the end of the trading script.

## Downloading Historical Market Data

- Data for simulations sourced from https://www.binance.com/en/landing/data

- Clone the official binance public data repo from https://github.com/binance/binance-public-data/

- Create new folder for holding data:

```bash
mkdir data/simulation_data
```

- In the cloned repo, download data to the newly created folder:

```bash
python3 download-kline.py -s ETHUSDT -startDate 2021-11-25 -i 15m -folder '/path/to/repo/crypto-trader/data/simulation_data'
```
- Extract downloaded data, and paste the folder path of the data in `simulation.py`.

- Run `simulation.py`, which starts with $100, and prints the final amount of money at the end of the trading script.

## Sample Output

- Here I test a hybrid greedy strategy on ETHUSDT data on a 15m chart over a month where the currency lost about 11% in value:

```bash
>>> python src/simulate.py 
INFO - 30-Dec-21 00:24:09 - Program boot
INFO - 30-Dec-21 00:24:09 - Bought 0.022253129346314324 at 4493.75 for 100 on 2021-12-01 21:15:00
INFO - 30-Dec-21 00:24:10 - Sold 0.022253129346314324 at 4227.37 for 94.07221140472878 on 2021-12-03 13:15:00
INFO - 30-Dec-21 00:24:11 - Bought 0.024878601363234058 at 3781.25 for 94.07221140472878 on 2021-12-03 23:30:00
INFO - 30-Dec-21 00:24:13 - Sold 0.024878601363234058 at 4299.16 for 106.95708783676133 on 2021-12-06 15:45:00
INFO - 30-Dec-21 00:24:14 - Bought 0.025501310825181877 at 4194.18 for 106.95708783676133 on 2021-12-09 09:30:00
INFO - 30-Dec-21 00:24:15 - Sold 0.025501310825181877 at 3960.0 for 100.98519086772023 on 2021-12-10 10:30:00
INFO - 30-Dec-21 00:24:16 - Bought 0.025113697394686118 at 4021.12 for 100.98519086772023 on 2021-12-12 19:15:00
INFO - 30-Dec-21 00:24:17 - Sold 0.025113697394686118 at 3773.15 for 94.75774732475993 on 2021-12-13 10:30:00
INFO - 30-Dec-21 00:24:19 - Bought 0.024318433103409674 at 3896.54 for 94.75774732475993 on 2021-12-17 01:15:00
INFO - 30-Dec-21 00:24:20 - Sold 0.024318433103409674 at 3967.12 for 96.47414233319859 on 2021-12-18 04:45:00
INFO - 30-Dec-21 00:24:20 - Bought 0.024660890211271023 at 3912.03 for 96.47414233319859 on 2021-12-18 19:30:00
INFO - 30-Dec-21 00:24:22 - Sold 0.024660890211271023 at 4007.22 for 98.82161247240947 on 2021-12-20 22:00:00
INFO - 30-Dec-21 00:24:22 - Bought 0.02460654631826872 at 4016.07 for 98.82161247240947 on 2021-12-22 03:45:00
INFO - 30-Dec-21 00:24:23 - Sold 0.02460654631826872 at 3984.07 for 98.03420299022487 on 2021-12-23 11:00:00
Final Account Balance: 98.03420299022487
```

- Note that this strategy lost only 2%, while the currency lost 11%.