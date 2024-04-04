# ŮŢƑ-Ⅷ (UTF-8)


## Background Context

Just like the title, this is a UTF-8 validation project. Have you ever wondered how some websites can display different languages? Or how you can send emojis through text messages? Well, wonder no more! This project will help you understand how characters are represented in a computer and help you understand how to validate UTF-8 data.


## Introduction

UTF-8 is a variable-width character encoding capable of encoding all 1,112,064 valid code points in Unicode using one to four one-byte (8-bit) code units. 

## Description

In this project, we will write a function that determines if a given data set represents a valid UTF-8 encoding. We will be given an array of integers where each integer represents a byte of data. Each byte may be between 0 and 255. You will need to determine whether the data set represents a valid UTF-8 encoding according to the following rules:

- A character in UTF-8 can be from 1 to 4 bytes long.
- Each integer represents 1 byte of data.
- The data set can contain multiple characters.


## Explanation

For a `1-byte character`, the first bit is a `0`, followed by its unicode code.
For an `n-byte character`, the first n bits are all `1`s, the `n+1` bit is `0`, followed by `n-1` bytes with most significant 2 bits being `10` that are the continuation bytes.

### Example

```python
data = [197, 130, 1]

# 197 = 1100 0101
# 130 = 1000 0010
# 1 = 0000 0001

# 11000101 10000010 00000001
```

1. The first byte is 11000101, which is a 2-byte sequence  because it begins with 110.
2. The second byte is 10000010, which is a valid continuation byte because it begins with 10.
3. The third byte is 00000001, which is a valid ASCII byte because it begins with 0.
Since all 3 bytes are valid, this data set is valid and the unicode representation is `A` after removing the leading bits.
Check out the file [0-validate_utf8.py](0-validate_utf8.py) for the function that validates the UTF-8 encoding.

## Requirements

To accomplish this task in python, you need to understand the following concepts:

- Bitwise operations (AND, OR, XOR, NOT, etc.) and how to use them.
- UTF-8 encoding rules so as to understand how characters are encoded.
- How to manipulate bits in a byte to extract information about the byte.
- How to use bitwise operations to determine if a byte is a continuation byte or a start byte.
- List operations such as accessing elements in a list and iterating through a list.
- Boolean logic to make decisions based on the results of bitwise operations.

## Resources

- [UTF-8 Encoding](https://en.wikipedia.org/wiki/UTF-8)
- [Bitwise Operators in Python](https://wiki.python.org/moin/BitwiseOperators)
- [Characters, Symbols and the Unicode Miracle](https://www.youtube.com/watch?v=MijmeoH9LT4)
- [The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)
- [Python Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

