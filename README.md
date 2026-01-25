# pullobj
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/cvisinoni/pullobj/blob/master/LICENSE)

pullobj is a Python library for building clients that connect to a generic remote server 
(databases, cloud storage, object collections) and synchronize all remote objects to a local directory.
It provides a simple abstraction to keep a local mirror always up to date with the remote source.


## Features
- Generic client for remote servers
- Full download of remote objects to local storage
- On-demand synchronization (remote → local)
- Supports heterogeneous objects (JSON, Excel, images, code, etc.)
- Extensible design for custom backends


## Installation
```bash
pip install pullobj
```

## Core Concept
- A Client represents a remote source
- The client knows how to list and fetch remote objects
- pullobj handles local storage and synchronization logic


## Contributing
If you'd like to contribute to pullobj, feel free to fork this repository, 
make your changes, and submit a pull request. 
We welcome contributions of all kinds, whether it's fixing a bug, 
adding a new feature, or improving documentation.


## License
This project is MIT licensed. See the [LICENSE](LICENSE) file for details.


## Support
If you have any questions, issues, or suggestions regarding pullobj, 
please [open an issue](https://github.com/cvisinoni/pullobj/issues) on GitHub.
We'd love to hear from you!
