# facesent - *face detecting sentinel*

**facesent** is a facial recognition sentinel and notifier for the desktop

![](https://img.shields.io/badge/python-3.3,%203.4,%203.5,%203.6-blue.svg)
![](https://img.shields.io/badge/license-GPLv2-lightgrey.svg)

```TEXT





Image placeholder





```

Build with **Python 3** and **OpenCV**

Start **facesent** by running `python3 facesent.py`.

## Usage

```
$ python3 facesent.py --help
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

### Gmail troubleshooting

If the authentication is failing with a gmail email address. Try following the link [https://accounts.google.com/DisplayUnlockCaptcha](https://accounts.google.com/DisplayUnlockCaptcha), click Continue and then retry the script.

## Contribute

We accept Pull requests!

Pull requests that are not ready to be merged should have a title starting with `[WIP]`.

Not necessary but suggested to pass your code from the pep8 check.

## License

All files in this repository are Copyright (c) 2018 **facesent author list**.

Code in this repository is licensed under [GNU General Public License v2.0](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html).

Data in this repository is licensed under the
[Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).

Exception are the files that contain other copyright notice.

**facesent author list** can be determined via `git shortlog -sne`.
