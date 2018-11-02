# Trollo

Trollo is a Python module for interacting with Trello.  It is a fork
of TrelloPy.

## Getting Started
Setting up your connection is simple (TODO: make it simpler):
```
from trollo import TrelloApi

#
# Visit: https://trello.com/app-key  to obtain your key
trello = TrelloApi(TRELLO_KEY)

# Visit: https://trello.com/1/authorize?expiration=never&
#        scope=read,write&response_type=token&name=<my_project>'
#         'key=' + TRELLO_KEY)
trello.set_token(TOKEN)
```

If your code already uses the old Trello module, you can simply
change it to use Trollo:
```
-import trello
+import trollo
```
### Prerequisites

Trollo requires Requests 2.0.0 or later.

### Installing
Trollo is available on PyPI; it can be installed by running:
```
pip install trollo
```
Alternatively, one could simply clone this repository and run:
```
python setup.py install
```

## Documentation

The documentation for hacking (e.g. implementing new Trello APIs) is
[here](https://developers.trello.com/reference/).

## Contributing

Please fork and issue pull requests.

## Authors
* **Fog Creek Software** - *Initial Work*
* **John Trowbridge** - *Bugfixes*
* **Lon Hohberger** - *Bugfixes, pypi packaging*

## License

This project is licensed under the BSD 2-clause license - see the [LICENSE.txt](LICENSE.txt) file for details

## Acknowledgements

The original source code for TrelloPy is [here](https://developers.kilnhg.com/Code/Trello/Group/TrelloPy).
