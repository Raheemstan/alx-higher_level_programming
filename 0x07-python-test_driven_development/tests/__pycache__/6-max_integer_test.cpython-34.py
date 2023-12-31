�
���\p  �               @   sW   d  Z  d d l Z e d � j Z Gd d �  d e j � Z e d k rS e j �  n  d S)z$Unittest for the max_integer module
�    Nz6-max_integerc               @   s�   e  Z d  Z d Z d d �  Z d d �  Z d d �  Z d d	 �  Z d
 d �  Z d d �  Z	 d d �  Z
 d d �  Z d d �  Z d d �  Z d S)�TestMaxIntegerz&TestCase for the max_integer function.c             C   s5   d d d d d g } t  | � } |  j | d � d S)z>Test with a regular list of ints: should return the max result�   �   �   �   �   N)�max_integer�assertEqual)�self�l�result� r   �v/home/vagrant/holbertonschool-higher_level_programming/0x07-python-test_driven_development/tests/6-max_integer_test.py�test_regular   s    zTestMaxInteger.test_regularc             C   s&   d d d g } |  j  t t | � d S)zQTest with a list of non-ints and ints:
        should raise a TypeError exception�a�b�	   N)�assertRaises�	TypeErrorr   )r
   r   r   r   r   �test_not_int   s    zTestMaxInteger.test_not_intc             C   s&   g  } t  | � } |  j | d � d S)z+Test with an empty list: should return NoneN)r   r	   )r
   r   r   r   r   r   �
test_empty   s    zTestMaxInteger.test_emptyc             C   s/   d d d g } t  | � } |  j | d � d S)	z:Test with a list of negative values: should return the maxr   �   r   N�����i���������r   )r   r	   )r
   r   r   r   r   r   �test_negative   s    zTestMaxInteger.test_negativec             C   s/   d d d g } t  | � } |  j | d � d S)z@Test with a list of mixed ints and floats: should return the maxr   g      @r   N)r   r	   )r
   r   r   r   r   r   �
test_float$   s    zTestMaxInteger.test_floatc             C   s   |  j  t t d � d S)zATest with a parameter that's not a list: should raise a TypeError�   N)r   r   r   )r
   r   r   r   �test_not_list*   s    zTestMaxInteger.test_not_listc             C   s)   d g } t  | � } |  j | d � d S)z@Test with a list of one int: should return the value of this int�-   N)r   r	   )r
   r   r   r   r   r   �test_unique.   s    	zTestMaxInteger.test_uniquec             C   s5   d d d d d g } t  | � } |  j | d � d S)z=Test with a list of identical values: should return the value�   N)r   r	   )r
   r   r   r   r   r   �test_identical4   s    zTestMaxInteger.test_identicalc             C   s,   d d g } t  | � } |  j | d � d S)z;Test with a list of strings: should return the first string�hiZhelloN)r   r	   )r
   r   r   r   r   r   �test_strings:   s    zTestMaxInteger.test_stringsc             C   s   |  j  t t d � d S)z7Test with a None as parameter: should raise a TypeErrorN)r   r   r   )r
   r   r   r   �	test_none@   s    zTestMaxInteger.test_noneN)�__name__�
__module__�__qualname__�__doc__r   r   r   r   r   r   r   r!   r#   r$   r   r   r   r   r   	   s   r   �__main__)r(   Zunittest�
__import__r   �TestCaser   r%   �mainr   r   r   r   �<module>   s
   ;