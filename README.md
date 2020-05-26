# Password generator

by Tim Degold

It's pretty simple to use. To see how it works run 

```
$ python randpass.py -h
usage: randpass.py [-h] [-l] [-c] [-n] [-s]

generate a random password

optional arguments:
  -h, --help            show this help message and exit
  -l , --length         number of characters in the password
  -c, --capital         exclude capital letters
  -n, --numbers         exclude numbers
  -s, --special_characters
                        exclude special characters

```

By default the password length is 14 characters and capital letters, numbers and special characters are included. Use the respective arguments to exclude them.

If default values need to be changed, do so via the `config.json` file.

# Sources

[1] *official documentation on argparse* https://docs.python.org/2.7/library/argparse.html (Accesses on May 26th 2020)
