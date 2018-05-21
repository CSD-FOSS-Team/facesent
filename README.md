# facesent - *face detecting sentinel*

**facesent**  is a facial recognition sentinel and notifier for the desktop

```TEXT





Image placeholder





```

Build with **Python 3** and **OpenCV**

## Usage

```
usage: facesent [-h] [-d S] [-u S] [-p P] [-i F] [-c F]

facesent - face detecting sentinel

optional arguments:
  -h, --help            show this help message and exit
  -d S, --delay S       delay before start (default 3s)
  -u S, --unlock-period S
                        period before locking (default 5s)
  -p P, --password P    delay before start (default "asdf")
  -i F, --image F       file name of the output image (default "tmpimage.jpg")
  -c F, --classifier F  file name of the classifier (default
                        "haarcascade_frontalface_alt.xml")
```

## Contribute

We accept Pull requests!

Pull requests that are not ready to be merged should have a title starting with `[WIP]`.

Not necessary but suggested to pass your code from the pep8 check.

## License

All files in this repository are Copyright (c) 2018 **sentinel author list**.

Code in this repository is licensed under ?

Data in this repository is licensed under the
[Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).

**sentinel author list** can be determined via `git shortlog -sne`.
