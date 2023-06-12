.. python-lekin documentation master file, created by
   sphinx-quickstart on Fri Sep 30 17:57:17 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

python-lekin documentation
========================================
.. raw:: html

   <a class="github-button" href="https://github.com/LongxingTan/python-lekin" data-icon="octicon-star" data-size="large" data-show-count="true" aria-label="Star LongxingTan/python-lekin on GitHub">GitHub</a>


**python-lekin** 是一个工厂智能排产调度工具，名字来源于`Lekin <https://web-static.stern.nyu.edu/om/software/lekin/>`_.

快速入门
---------

排产是一个分配任务，将有限的资源分配给需求。因此需求需要有优先级，约束主要有产能约束与物料约束。产能约束，将订单中的成品按工艺路线分解为工序，而每一道工序有对应的生产机器；物料约束，将订单的成品按BOM(bill of materials)展开为原材料需求，每一道工序开始前需要对应原材料齐套。


Finite Capacity Planning

.. toctree::
   :maxdepth: 5
   :caption: Contents:

   tutorials
   models
   constraints
   application
   api
   CHANGELOG
   GitHub <https://github.com/LongxingTan/python-lekin>



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
