.. description: 
.. tags: NeuronalNet, KIT, mathjax
.. date: 2013/09/17 16:35
.. title: Elias Code Generation
.. slug: 


Simple python script for generating elias-:math:`\gamma`, :math:`\delta`, unary and golomb codes.
Here is an example output with :math:`\gamma`, :math:`\delta`, and golomb-code.

.. code::

    $ python elias.py 
    0: 0          : 0          : 0000000   
    1: 100        : 1000       : 0000001   
    2: 1100       : 11000      : 0000010   
    3: 1101       : 11001      : 0000011   
    4: 111000     : 110100     : 0000100   
    5: 111001     : 110101     : 0000101   
    6: 111010     : 110110     : 0000110   
    7: 111011     : 110111     : 0000111   
    8: 11110000   : 111000000  : 0001000   
    9: 11110001   : 111000001  : 0001001   

.. listing:: elias.py python


