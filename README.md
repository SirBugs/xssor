# xssor
xssor is a Python tool that tests for cross-site scripting (XSS) vulnerabilities by sending payloads through the parameters in URLs.

It can be used for single URL testing using the -u or --url option, or for testing multiple URLs using the -l or --list option.

# Installation
To install xssor, clone the repository and run the following command:
```pip install -r requirements.txt```

# Usage
xssor takes four arguments:
```
    -u or --url: the URL to test for XSS vulnerabilities.
    -l or --list: a file containing a list of URLs to test for XSS vulnerabilities.
    -t or --threads: the number of threads to use for testing.
    -o or --output: the name of the file to save the results to.
```
Usage:
```xssor.py [-h] -u URL [-l LIST] [-t THREADS] [-o OUTPUT]```

# Examples
To test a single URL using four threads and save the results to a file named results.txt, run the following command:

```python xssor.py -u http://example.com -t 4 -o results.txt```

To test a list of URLs contained in a file named urls.txt using eight threads and save the results to a file named results.txt, run the following command:

```python xssor.py -l urls.txt -t 8 -o results.txt```

# Coder
Written in python3, By @SirBagoza

Made with love, In Egypt <3
