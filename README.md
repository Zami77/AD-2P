# AD-2P
AD2P is the Automated Detection of the year 2038 Problem. The purpose is to have a CLI tool that can statically analyze source code (currently using Libclang) and detect any potential vulnerabilities related to the year 2038 problem.

If you are unfamiliar with the year 2038 problem, please check the [2038 wikipedia](https://en.wikipedia.org/wiki/Year_2038_problem). It essentially involves 32-bit systems having time integer overflow occur in the year 2038. For further details on my project implementation please check out the [AD-2P SDD wiki](https://github.com/Zami77/AD-2P/wiki/Software-Design-Documentation).

2038 C Time References JSON file is from [y2038.com](https://y2038.com/c-review/)
