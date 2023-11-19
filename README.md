# python-challenge

The structure of the repository should be:
```
python-challenge
├── PyBank
│   ├── main.py
│   ├── analysis
│   │   └── output.txt
│   └── Resources 
│       └── budget_data.csv
└── PyBank
    ├── main.py
    ├── analysis
    │   └── output.txt
    └── Resources 
        └── election_data.csv
```
### Getting started
The script assumes the `python-challenge` folder as the working directory <br>
```commandline
cd python-challenge
```
To run the PyBank: `python PyBank/main.py` 
```
$ python PyBank/main.py
Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
```
To run PyPoll: `python PyPoll/main.py`
```
$ python PyPoll/main.py
Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham 23.05% (85213)
Diana DeGette 73.81% (272892)
Raymon Anthony Doane 3.14% (11606)
-------------------------
Winner: Diana DeGette
-------------------------
```

## References:
-`PyBank/main.py`:
  - `sum`: is a python built-in function, from the [documentation](https://docs.python.org/3/library/functions.html#sum), lines: 39
  - `"""`: string literals inside triple quotes can span multiple lines of text, from [Google for Education](https://developers.google.com/edu/python/strings), lines: 41-47


-`PyPoll/main.py`:
  - `sorted`: is a python built-in for sorting iterables, from the [documentation](https://docs.python.org/3/library/functions.html#sorted), lines: 21
  - `max(ballot, key=ballot.get)`:  gets key with largest value, from [stackoverflow](https://stackoverflow.com/a/280156), lines: 29
  - `"""`: string literals inside triple quotes can span multiple lines of text, from [Google for Education](https://developers.google.com/edu/python/strings), lines: 31-37

