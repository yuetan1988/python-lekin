[license-image]: https://img.shields.io/badge/License-Apache%202.0-blue.svg
[license-url]: https://opensource.org/licenses/Apache-2.0
[pypi-image]: https://badge.fury.io/py/tfts.svg
[pypi-url]: https://pypi.python.org/pypi/tfts
[build-image]: https://github.com/LongxingTan/python-lekin/actions/workflows/test.yml/badge.svg?branch=master
[build-url]: https://github.com/LongxingTan/python-lekin/actions/workflows/test.yml?query=branch%3Amaster
[lint-image]: https://github.com/LongxingTan/python-lekin/actions/workflows/lint.yml/badge.svg
[lint-url]: https://github.com/LongxingTan/python-lekin/actions/workflows/lint.yml
[docs-image]: https://readthedocs.org/projects/python-lekin/badge/?version=latest
[docs-url]: https://python-lekin.readthedocs.io/en/latest/

<h1 align="center">
<img src="./docs/source/_static/logo.svg" width="490" align=center/>
</h1><br>

--------------------------------------------------------------------

[![LICENSE][license-image]][license-url]
[![PyPI Version][pypi-image]][pypi-url]
[![Build Status][build-image]][build-url]
[![Lint Status][lint-image]][lint-url]
[![Docs Status][docs-image]][docs-url]

python-lekin is a **Flexible Job Shop Scheduler Library**, named after and inspired by [Lekin](https://web-static.stern.nyu.edu/om/software/lekin/).
As a core function in **APS (advanced planning and scheduler)**, it helps to improve factory efficiency.

## Tutorial

**Install**
``` shell
$ pip install python-lekin
```

**Usage**

``` python
from lekin import Heuristics, Genetics
from lekin import Scheduler

solver = Heuristics()
scheduler = Scheduler(solver)
scheduler.solve(jobs, machines)

scheduler.draw()
```

## Examples

## Citation
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
