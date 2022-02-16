# Linkedin Auto Connection Bot

This an Automation Bot build in python with selenium to connect in linkedin with any professional of your choice 

## Installation

To use this Bot you need to install Python first

```
https://www.python.org/downloads/
```
Then
```
pip install selenium
```
## Usage

Go to linkedin search for your interested people you will want to connect you

### Example
if url is https://www.linkedin.com/search/results/people/?keywords=senior%20quantity%20surveyor&network=%5B%22S%22%5D&origin=FACETED_SEARCH&page=1&position=1&searchId=9fc7e98e-4b71-4355-95a5-6a9a5e27a487&sid=Nia

Must search where this a page number in the url `SEARCH&page=1` and replace 1 with {w}

```python
n_pages = 40 # Maximum ranges of pages to connect
for n in range(1,n_pages):
    w = str(n)
    print(w)
    driver.get(f'https://www.linkedin.com/search/results/people/?keywords=senior%20quantity%20surveyor&network=%5B%22S%22%5D&origin=FACETED_SEARCH&page={w}&position=1&searchId=9fc7e98e-4b71-4355-95a5-6a9a5e27a487&sid=Nia')
    time.sleep(2)

```
