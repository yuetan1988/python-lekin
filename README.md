# python-lekin

[license-image]: https://img.shields.io/badge/License-Apache%202.0-blue.svg
[license-url]: https://opensource.org/licenses/Apache-2.0

[![LICENSE][license-image]][license-url]

Python-lekin is a **Flexible Job Shop Scheduler Library**, named after and inspired by [Lekin](https://web-static.stern.nyu.edu/om/software/lekin/).
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
