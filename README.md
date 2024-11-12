# HausaNum2Words

**HausaNum2Words** is a Python package designed to convert numerical values into their equivalent word representations in the Hausa language. This is particularly useful for applications requiring localization in Hausa, financial documentation, and educational tools that teach number comprehension.

## Features
* Converts numbers into Hausa words.
* Supports large numbers (e.g., millions, billions).
* Easy to integrate with existing Python applications.

# Installation
Install via pip
```bash
pip install HausaNum2Words
```

Or, install from source:
```
git clone https://github.com/yourusername/HausaNum2Words.git
cd HausaNum2Words
python setup.py install
```
## Usage

To start converting numbers to Hausa words, import the `HausaNumConverter` class from `HausaNum2Words`, then use the `to_words` method to convert your number.

```
from HausaNum2Words import HausaNumConverter

# Initialize the converter
converter = HausaNumConverter()

# Convert a number to Hausa words
result = converter.to_words(12345)
print(result)  # Example output: "dubu goma sha biyu da dari uku da arba'in da biyar"
```

## Example Output
* Input: `converter.to_words(123)`
* Output: `"dari da ashirin da uku"`

## License
This project is licensed under the MIT License. See the LICENSE file for more details.