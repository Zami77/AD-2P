# AD-2P
[AD-2P Web Interface](https://zami77.github.io/AD2P_Web/)

## About
AD2P is the Automated Detection of the year 2038 Problem. The purpose is to have a CLI tool that can statically analyze source code (currently using Libclang) and detect any potential vulnerabilities related to the year 2038 problem. A web GUI and desktop application have also been developed.

If you are unfamiliar with the year 2038 problem, please check the [2038 wikipedia](https://en.wikipedia.org/wiki/Year_2038_problem). It involves 32-bit Unix systems having time integer overflow occur in the year 2038. For further details on my project implementation please check out the [AD-2P SDD wiki](https://github.com/Zami77/AD-2P/wiki/Software-Design-Documentation).

## How To Use
### Web Interface
Select a file to upload and then select the scan button.

[AD-2P Web Interface](https://zami77.github.io/AD2P_Web/)
### CLI
If you clone this repo, you can use AD-2P as a CLI tool. Simply call AD-2P with a file or directory as the argument. It will output any potential vulnerabilities to the console.

```python AD2P.py sample.cpp```

### Desktop Application
Developed in Godot, the source code is in the repo below. Currently working on a way to host .exe files, but you can clone the repo and export the project in Godot.

[AD-2P UI Repository](https://github.com/Zami77/AD2P_UI)

### Backend API
Backend is created with FastAPI and hosted on an Azure app service. Anyone is free to use the API.

The base endpoint is ```https://ad2p.azurewebsites.net/```

Swagger documentation can be found at ```https://ad2p.azurewebsites.net/docs```

## External Repositories
[AD-2P Web Repository](https://github.com/Zami77/AD2P_Web)

[AD-2P UI Repository](https://github.com/Zami77/AD2P_UI)

## References
2038 C Time References JSON file is from [y2038.com](https://y2038.com/c-review/)
