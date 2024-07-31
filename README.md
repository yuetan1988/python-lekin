[license-image]: https://img.shields.io/badge/License-Apache%202.0-blue.svg
[license-url]: https://opensource.org/licenses/Apache-2.0
[pypi-image]: https://badge.fury.io/py/lekin.svg
[pypi-url]: https://pypi.python.org/pypi/lekin
[pepy-image]: https://pepy.tech/badge/lekin/month
[pepy-url]: https://pepy.tech/project/lekin
[build-image]: https://github.com/LongxingTan/python-lekin/actions/workflows/test.yml/badge.svg?branch=master
[build-url]: https://github.com/LongxingTan/python-lekin/actions/workflows/test.yml?query=branch%3Amaster
[lint-image]: https://github.com/LongxingTan/python-lekin/actions/workflows/lint.yml/badge.svg?branch=master
[lint-url]: https://github.com/LongxingTan/python-lekin/actions/workflows/lint.yml?query=branch%3Amaster
[docs-image]: https://readthedocs.org/projects/python-lekin/badge/?version=latest
[docs-url]: https://python-lekin.readthedocs.io/en/latest/
[coverage-image]: https://codecov.io/gh/longxingtan/python-lekin/branch/master/graph/badge.svg
[coverage-url]: https://codecov.io/github/longxingtan/python-lekin?branch=master
[codeql-image]: https://github.com/longxingtan/python-lekin/actions/workflows/codeql-analysis.yml/badge.svg
[codeql-url]: https://github.com/longxingtan/python-lekin/actions/workflows/codeql-analysis.yml

<h1 align="center">
<img src="./docs/source/_static/logo.svg" width="490" align=center/>
</h1><br>

[![LICENSE][license-image]][license-url]
[![PyPI Version][pypi-image]][pypi-url]
[![Download][pepy-image]][pepy-url]
[![Build Status][build-image]][build-url]
[![Lint Status][lint-image]][lint-url]
[![Docs Status][docs-image]][docs-url]
[![Code Coverage][coverage-image]][coverage-url]
[![CodeQL Status][codeql-image]][codeql-url]

**[Documentation](https://python-lekin.readthedocs.io)** | **[Tutorials](https://python-lekin.readthedocs.io/en/latest/tutorials.html)** | **[Release Notes](https://python-lekin.readthedocs.io/en/latest/CHANGELOG.html)** | **[中文](https://github.com/LongxingTan/python-lekin/blob/master/README_zh_CN.md)**

**python-lekin** is a rapid-to-implement and easy-to-use Flexible Job Shop Scheduler Library, named after and inspired by [Lekin](https://web-static.stern.nyu.edu/om/software/lekin/). As a core function in **APS (advanced planning and scheduler)**, it helps manufacturers optimize the allocation of materials and production capacity optimally to balance demand and capacity.

- accelerate by 
- Changeover Optimization
- Ready for demo, research and maybe production

# **DEVELOPING - NOT FINISHED AND DON'T USE IT NOW!**

## Feature

- constrained optimization
  - route
  - production
  - material kit
  - together

- soft constrained optimization
  - objective


## Tutorial

**Installation**

``` shell
$ pip install lekin
```

**Usage**

``` python
from lekin import Heuristics, Rule
from lekin import Scheduler

solver = Rule('SPT')
scheduler = Scheduler(solver)
scheduler.solve(job_list, machine_list)

scheduler.draw()
```

## Examples

In real world, Lekin integrates with MES to deploy production plans on the shop floor. Integration with ERP system is also required to exchange information on demand, inventory, and production

- Exhaustive search
  - branch and bound

- Construction heuristics
    - [SPT]()
    - [critical path]()

- Meta heuristics
    - [local search]()
      - [hill climbing]()
      - [tabu search]()
    - [evolutionary algorithms]()
      - [genetic algorithms]()

- Operation search
    - [or-tools]()

- Reinforcement learning

Metaheuristics combined with Construction
Heuristics to initialize is the recommended choice.

## Citation
```
@misc{python-lekin2022,
  author = {Yue Tan},
  title = {python lekin},
  year = {2022},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/yuetan1988/python-lekin}},
}
```
