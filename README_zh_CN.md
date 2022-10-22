[license-image]: https://img.shields.io/badge/License-Apache%202.0-blue.svg
[license-url]: https://opensource.org/licenses/Apache-2.0
[pypi-image]: https://badge.fury.io/py/python-lekin.svg
[pypi-url]: https://pypi.python.org/pypi/python-lekin
[build-image]: https://github.com/LongxingTan/python-lekin/actions/workflows/test.yml/badge.svg?branch=master
[build-url]: https://github.com/LongxingTan/python-lekin/actions/workflows/test.yml?query=branch%3Amaster
[lint-image]: https://github.com/LongxingTan/python-lekin/actions/workflows/lint.yml/badge.svg?branch=master
[lint-url]: https://github.com/LongxingTan/python-lekin/actions/workflows/lint.yml?query=branch%3Amaster
[docs-image]: https://readthedocs.org/projects/python-lekin/badge/?version=latest
[docs-url]: https://python-lekin.readthedocs.io/en/latest/
[coverage-image]: https://codecov.io/gh/longxingtan/python-lekin/branch/master/graph/badge.svg
[coverage-url]: https://codecov.io/github/longxingtan/python-lekin?branch=master

<h1 align="center">
<img src="./docs/source/_static/logo.svg" width="490" align=center/>
</h1><br>

[![LICENSE][license-image]][license-url]
[![PyPI Version][pypi-image]][pypi-url]
[![Build Status][build-image]][build-url]
[![Lint Status][lint-image]][lint-url]
[![Docs Status][docs-image]][docs-url]
[![Code Coverage][coverage-image]][coverage-url]

**[Documentation](https://python-lekin.readthedocs.io)** | **[Tutorials](https://python-lekin.readthedocs.io/en/latest/tutorials.html)** | **[Release Notes](https://python-lekin.readthedocs.io/en/latest/CHANGELOG.html)** | **[中文](https://github.com/LongxingTan/python-lekin/blob/master/README_CN.md)**

**python-lekin**是一个数字化车间智能排产调度工具，名字来源于[教育工具Lekin](https://web-static.stern.nyu.edu/om/software/lekin/)


## 快速入门

### 安装

``` shell
$ pip install python-lekin
```

### 使用

``` python
from lekin import Heuristics, Genetics
from lekin import Scheduler

solver = Heuristics()
scheduler = Scheduler(solver)
scheduler.solve(jobs, machines)

scheduler.draw()
```
### 数据解释
- Job
- Task
- Machine
- Route

## 示例

## 引用
```
@misc{python-lekin2022,
  author = {Longxing Tan},
  title = {python lekin},
  year = {2022},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/longxingtan/python-lekin}},
}
```
