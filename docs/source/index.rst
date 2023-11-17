.. python-lekin documentation master file, created by
   sphinx-quickstart on Fri Sep 30 17:57:17 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

python-lekin documentation
========================================
.. raw:: html

   <a class="github-button" href="https://github.com/LongxingTan/python-lekin" data-icon="octicon-star" data-size="large" data-show-count="true" aria-label="Star LongxingTan/python-lekin on GitHub">GitHub</a>


**python-lekin** 是一个工厂智能排产调度工具，名字来源于`Lekin <https://web-static.stern.nyu.edu/om/software/lekin/>`_.

组合优化基础
-------------

- 装箱问题(Bin Packing, BP)
- 背包问题(Knapsack Problem, KP)
- 车间调度问题(Job-shop Scheduling Problem, JSP)
- 整数规划问题(Integer Programming, IP)

- 旅行商问题(Traveling Salesman Problem, TSP)
- 车辆路径问题(Vehicle Routing Problem, VRP)
- 图着色问题(Graph Coloring, GC)
- 图匹配问题(Graph Matching, GM)


- 精确算法：分支定界法(Branch and Bound)和动态规划法(Dynamic Programming)

- 近似算法：近似算法(Approximate Algorithms)和启发式算法(Heuristic Algorithms)
   - 贪心算法、局部搜索算法、线性规划、松弛算法、序列算法
   - 模拟退火算法、禁忌搜索、进化算法、蚁群优化算法、粒子群算法、迭代局部搜索、变邻域搜索


车间排产快速入门
---------------

排产是一个分配任务，将有限的资源分配给需求。因此需求需要有优先级，约束主要有产能约束与物料约束。产能约束，将订单中的成品按工艺路线分解为工序，而每一道工序有对应的生产机器；物料约束，将订单的成品按BOM(bill of materials)展开为原材料需求，每一道工序开始前需要对应原材料齐套。

下标，机器k kk加工为任务i ii后加工任务j jj

其中，:math:`A_\text{c} = (\pi/4) d^2`


subject to:

.. math:: \alpha{}_t(i) = P(O_1, O_2, … O_t, q_t = S_i \lambda{})

Flexible Job-Shop Scheduling problem（FJSP）包含两个任务
- Machine assignment: 选择机器
- Operation sequencing：工序顺序


Finite Capacity Planning

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   rules
   heuristics
   rl
   application
   demand
   api
   GitHub <https://github.com/LongxingTan/python-lekin>


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
