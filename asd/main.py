# SPDX-FileCopyrightText: © 2021 Author <email>
# SPDX-License-Identifier: GPL-3.0-only

r"""
Main Module
===========
"""

def lonely_function():
    r"""
    As promised, what follows is a demonstration of docstring
    documentation.

    You can add **bold** and *italic* text, text with `math 
    typesetting` and ``source code``.
    You can cite your sources either in text, such as :cite:t:`Tedrake`,
    or in parenthetic fashion :cite:p:`di2020software`,

    - Bullet points work as well

    and so does LaTeX math, unlabeled and labeled,
    as you can see in :eq:`test`!

    .. math::

        f(n) =
        \begin{cases}
        n/2,  & \text{if $n$ is even} \\
        3n+1, & \text{if $n$ is odd}
        \end{cases}

    .. math::
        :label: test

        f(n) =
        \begin{cases}
        n/2,  & \text{if $n$ is even} \\
        3n+1, & \text{if $n$ is odd}
        \end{cases}

    Table syntax is rather weird but manageable.

    .. _table2:
    .. list-table:: Example table.
        :widths: auto
        :header-rows: 1
        :align: center

        * - **Header 1**
          - **Header 2**
          - **Header 3**
          - **Header 4**
        * - A
          - B
          - C
          - D

    You can add pictures if you want too. Importantly, when you
    are generating documentation from your code:
    
    - Place your figures in the **docs/source/figures directory**.
    - Include them with their path relative to the source. That is,
      **figures/<your figure>.<ext>**.

    Unfortunately the figure doesn't nicely fit in this page. Fortunately,
    we can break page to try and have our discourse flow anyway.

    .. raw:: latex

        \clearpage

    Check it:

    .. _figure2:
    .. figure:: figures/demo.png
        :width: 50%
        :align: center

        You're free to set alignment, figure width relative to the text's, etc. 
        Don't trust Sphinx to go too far. 
        
        If you need something complex use proper
        LaTeX code inside a ``.. raw:: latex`` block.

    .. _figure3:
    .. figure:: figures/demo.png
        :width: 50%
        :align: center

        Adding a cross-reference to :numref:`table1` or :numref:`figure1` works 
        much as it would in LaTeX.

    .. raw:: latex

        \clearpage

    """
    pass