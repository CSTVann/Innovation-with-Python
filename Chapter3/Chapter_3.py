{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "f54d28a5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome.\n",
      "Welcome.\n"
     ]
    }
   ],
   "source": [
    "def my_greeting(n):\n",
    "    for _ in range(n):\n",
    "        print(\"Welcome.\")\n",
    "my_greeting(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "e28095c9",
   "metadata": {},
   "outputs": [],
   "source": [
    "m, n, p = [int(a) for a in input(\"Enter three numbers :\").split()]\n",
    "def minmidmax2(m, n,p):\n",
    "    print(\"The greater of\", m, \"or\", n, \"is :\", max(m, n,p))\n",
    "    print(\"The smaller of\", m, \"or\", n, \"is :\", min(m, n,p))\n",
    "    if m < n < p or p < n < m:\n",
    "        print(n,\"is middle value\")\n",
    "    elif m < p < n or n < p < m:\n",
    "        print(p,\"is middle value\")\n",
    "    else:\n",
    "        print(m,\"is middle value\")\n",
    "minmidmax2(m, n, p)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5469117d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f528c847",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 mile = 1.61 kilometers\n",
      "2 mile = 3.22 kilometers\n",
      "3 mile = 4.83 kilometers\n",
      "4 mile = 6.44 kilometers\n",
      "5 mile = 8.05 kilometers\n"
     ]
    }
   ],
   "source": [
    "def mile2km(mi):\n",
    "    mile = mi * 1.61\n",
    "    print(n, \"mile =\", mile, \"kilometers\")\n",
    "for n in range(1,6):\n",
    "    mile2km(n)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8cfb9232",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10 degrees Celsius = 50.0 degrees Fahrenheit\n",
      "20 degrees Celsius = 68.0 degrees Fahrenheit\n",
      "30 degrees Celsius = 86.0 degrees Fahrenheit\n",
      "40 degrees Celsius = 104.0 degrees Fahrenheit\n",
      "50 degrees Celsius = 122.0 degrees Fahrenheit\n"
     ]
    }
   ],
   "source": [
    "def cel2fah(cel):\n",
    "    fah = cel * 9/5 + 32\n",
    "    print(n, \"degrees Celsius =\", fah, \"degrees Fahrenheit\")\n",
    "for n in range(10,60,10):\n",
    "    cel2fah(n)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "27519da5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter three numbers :9 2 6\n",
      "The average value of 9 2 6 is 5.666666666666667\n",
      "The miximum value of 9 2 6 is 9\n",
      "The minimum value of 9 2 6 is 2\n"
     ]
    }
   ],
   "source": [
    "a, b, c = [int(a) for a in input(\"Enter three numbers :\").split()]\n",
    "def mean3(a, b, c):\n",
    "    ave = (a + b + c)/3\n",
    "    print(\"The average value of\", a, b, c, 'is', ave)\n",
    "def max3(a, b, c):\n",
    "    print(\"The miximum value of\", a, b, c, 'is', max(a, b, c))\n",
    "def min3(a, b, c):\n",
    "    print(\"The minimum value of\", a, b, c, 'is', min(a, b, c))\n",
    "mean3(a, b, c)\n",
    "max3(a, b, c)\n",
    "min3(a, b, c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "54ccefa8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "675"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "max(3,21,1,54,5,675,4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5db619e8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter number : 10\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "55"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def sum1(n):\n",
    "    if n == 1:\n",
    "        return 1\n",
    "    else:\n",
    "        return n + sum1(n - 1)\n",
    "n = int(input(\"Enter number : \"))\n",
    "sum1(n)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "97806ec3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter x : 2\n",
      "Enter n : 10\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "1024"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def pow2(x,n):\n",
    "    if n == 0:\n",
    "        return 1\n",
    "    elif n == 1:\n",
    "        return x\n",
    "    else:\n",
    "        return x * (pow2(x, n-1))\n",
    "x = int(input(\"Enter x : \"))\n",
    "n = int(input(\"Enter n : \"))\n",
    "pow2(x, n)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3c57d4d4",
   "metadata": {},
   "outputs": [],
   "source": [
    "def pow2(x, n)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "628349f9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{((3, 1), 3), ((3, 3), 1), ((3, 1), 1), ((1, 3), 3), ((1, 1), 1), ((3, 3), 3), ((1, 1), 3), ((1, 3), 1)}\n"
     ]
    }
   ],
   "source": [
    "def product_set(set1, set2):\n",
    "    res = set()\n",
    "    for i in set1:\n",
    "        for j in set2:\n",
    "            res = res | {(i, j)}\n",
    "    return res\n",
    "def exp(input_set, exponent):\n",
    "    res = input_set\n",
    "    for _ in range(exponent - 1):\n",
    "        res = product_set(res, input_set)\n",
    "    return res\n",
    "A = {1, 3}\n",
    "A3 = exp(A, 3)\n",
    "print(A3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bfd52cae",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{(3, 4), (4, 3), (3, 1), (5, 4), (4, 6), (5, 1), (2, 2), (1, 6), (2, 5), (1, 3), (6, 2), (6, 5), (4, 2), (4, 5), (3, 3), (5, 6), (3, 6), (5, 3), (2, 4), (1, 2), (2, 1), (1, 5), (6, 1), (6, 4), (3, 2), (4, 1), (3, 5), (5, 2), (4, 4), (5, 5), (1, 1), (1, 4), (2, 3), (2, 6), (6, 6), (6, 3)}\n"
     ]
    }
   ],
   "source": [
    "def product_set(set1, set2):\n",
    "    res = set()\n",
    "    for i in set1:\n",
    "        for j in set2:\n",
    "            res = res | {(i, j)}\n",
    "    return res\n",
    "cases = {1,2,3,4,5,6}\n",
    "cases_2times = product_set(cases, cases)\n",
    "print(cases_2times)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e6cac41d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number 1, A -> C\n",
      "Number 2, A -> B\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'vai_' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Input \u001b[1;32mIn [23]\u001b[0m, in \u001b[0;36m<cell line: 8>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      6\u001b[0m         \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mNumber \u001b[39m\u001b[38;5;132;01m{}\u001b[39;00m\u001b[38;5;124m, \u001b[39m\u001b[38;5;132;01m{}\u001b[39;00m\u001b[38;5;124m -> \u001b[39m\u001b[38;5;132;01m{}\u001b[39;00m\u001b[38;5;124m'\u001b[39m\u001b[38;5;241m.\u001b[39mformat(n, from_, to_))\n\u001b[0;32m      7\u001b[0m         hanoi(n\u001b[38;5;241m-\u001b[39m\u001b[38;5;241m1\u001b[39m, vai_, to_, from_)\n\u001b[1;32m----> 8\u001b[0m \u001b[43mhanoi\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;241;43m3\u001b[39;49m\u001b[43m,\u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mA\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m,\u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mC\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m,\u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mB\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m)\u001b[49m\n",
      "Input \u001b[1;32mIn [23]\u001b[0m, in \u001b[0;36mhanoi\u001b[1;34m(n, from_, to_, via_)\u001b[0m\n\u001b[0;32m      3\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mNumber \u001b[39m\u001b[38;5;132;01m{}\u001b[39;00m\u001b[38;5;124m, \u001b[39m\u001b[38;5;132;01m{}\u001b[39;00m\u001b[38;5;124m -> \u001b[39m\u001b[38;5;132;01m{}\u001b[39;00m\u001b[38;5;124m'\u001b[39m\u001b[38;5;241m.\u001b[39mformat(n, from_, to_))\n\u001b[0;32m      4\u001b[0m \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[1;32m----> 5\u001b[0m     \u001b[43mhanoi\u001b[49m\u001b[43m(\u001b[49m\u001b[43mn\u001b[49m\u001b[38;5;241;43m-\u001b[39;49m\u001b[38;5;241;43m1\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mfrom_\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mvia_\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mto_\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m      6\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mNumber \u001b[39m\u001b[38;5;132;01m{}\u001b[39;00m\u001b[38;5;124m, \u001b[39m\u001b[38;5;132;01m{}\u001b[39;00m\u001b[38;5;124m -> \u001b[39m\u001b[38;5;132;01m{}\u001b[39;00m\u001b[38;5;124m'\u001b[39m\u001b[38;5;241m.\u001b[39mformat(n, from_, to_))\n\u001b[0;32m      7\u001b[0m     hanoi(n\u001b[38;5;241m-\u001b[39m\u001b[38;5;241m1\u001b[39m, vai_, to_, from_)\n",
      "Input \u001b[1;32mIn [23]\u001b[0m, in \u001b[0;36mhanoi\u001b[1;34m(n, from_, to_, via_)\u001b[0m\n\u001b[0;32m      5\u001b[0m hanoi(n\u001b[38;5;241m-\u001b[39m\u001b[38;5;241m1\u001b[39m, from_, via_, to_)\n\u001b[0;32m      6\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mNumber \u001b[39m\u001b[38;5;132;01m{}\u001b[39;00m\u001b[38;5;124m, \u001b[39m\u001b[38;5;132;01m{}\u001b[39;00m\u001b[38;5;124m -> \u001b[39m\u001b[38;5;132;01m{}\u001b[39;00m\u001b[38;5;124m'\u001b[39m\u001b[38;5;241m.\u001b[39mformat(n, from_, to_))\n\u001b[1;32m----> 7\u001b[0m hanoi(n\u001b[38;5;241m-\u001b[39m\u001b[38;5;241m1\u001b[39m, \u001b[43mvai_\u001b[49m, to_, from_)\n",
      "\u001b[1;31mNameError\u001b[0m: name 'vai_' is not defined"
     ]
    }
   ],
   "source": [
    "def hanoi(n, from_, to_, via_):\n",
    "    if n == 1:\n",
    "        print('Number {}, {} -> {}'.format(n, from_, to_))\n",
    "    else:\n",
    "        hanoi(n-1, from_, via_, to_)\n",
    "        print('Number {}, {} -> {}'.format(n, from_, to_))\n",
    "        hanoi(n-1, vai_, to_, from_)\n",
    "hanoi(3,'A','C','B')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5337560e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "How many fibonacci numbers do you want? 7\n",
      "fibonacci: sequence:  0 1 1 2 3 5 8 "
     ]
    }
   ],
   "source": [
    "def fibonacci(n):\n",
    "    if n<=1:\n",
    "        return n\n",
    "    else:\n",
    "        return(fibonacci(n-1) + fibonacci(n-2))\n",
    "nterms = int(input(\"How many fibonacci numbers do you want? \"))\n",
    "if nterms <= 0:\n",
    "    print('Error : Enter a positive number')\n",
    "else:\n",
    "    print(\"fibonacci: sequence: \", end=' ')\n",
    "    for i in range(nterms):\n",
    "        print(fibonacci(i), end=' ')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "471c90fc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "fibonacci_1(30) * 20 times :  6.907000300000618 seconds\n"
     ]
    }
   ],
   "source": [
    "from timeit import *\n",
    "def fibonacci_1(n):\n",
    "    if n == 0:\n",
    "        return 0\n",
    "    elif n == 1:\n",
    "        return 1\n",
    "    else:\n",
    "        return(fibonacci(n-1) + fibonacci(n-2))\n",
    "t3 = Timer(\"fibonacci_1(30)\",\"from __main__ import fibonacci_1\")\n",
    "print(\"fibonacci_1(30) * 20 times : \", t3.timeit(number = 20), \"seconds\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5d0bc238",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "fibonacci_1(30) * 20 times :  1.9500000234984327e-05 seconds\n"
     ]
    }
   ],
   "source": [
    "from timeit import *\n",
    "dic = {0:0, 1:1}\n",
    "def fibonacci_1(n):\n",
    "    if n in dic:\n",
    "        return dic[n]\n",
    "    dic[n] = (fibonacci_1(n-1) + fibonacci_1(n-2))\n",
    "    return dic[n]\n",
    "t3 = Timer(\"fibonacci_1(30)\",\"from __main__ import fibonacci_1\")\n",
    "print(\"fibonacci_1(30) * 20 times : \", t3.timeit(number = 20), \"seconds\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "16c3e06e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter euler number : 20\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "2.7182818284590455"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def factorial(k):\n",
    "    if k == 1:\n",
    "        return 1\n",
    "    else :\n",
    "        return k * factorial(k - 1)\n",
    "def euler(n):\n",
    "    if n == 0:\n",
    "        return 1\n",
    "    else: \n",
    "        return 1/factorial(n) + euler(n-1)\n",
    "k = int(input(\"Enter euler number : \"))\n",
    "euler(k)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "51459658",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Distinguish year, month and date by .(e.g. 1917. 6.10) : 2200.10.20\n",
      "This is not a publication year of the sherlock Holmes series.\n",
      "This is not the publication date of a Sherlock Holmes series or the input has an error.\n"
     ]
    }
   ],
   "source": [
    "def valid_date(date):\n",
    "    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]\n",
    "    sherlock_series = [1887, 1890, 1892, 1894, 1901, 1905, 1915, 1917, 1927]\n",
    "    splitted = date.split('.')\n",
    "    year = int(splitted[0])\n",
    "    month = int(splitted[1])\n",
    "    day = int(splitted[2])\n",
    "    is_sherlock_book_yr = lambda x: x in sherlock_series\n",
    "    \n",
    "    if not is_sherlock_book_yr(year):\n",
    "        print('This is not a publication year of the sherlock Holmes series.')\n",
    "        return False\n",
    "    if month < 1 or month > 12:\n",
    "        print('The month is incorrect.')\n",
    "        return False\n",
    "    if day < 1 or day > days[month - 1]:\n",
    "        print('The daye is incorrect.')\n",
    "        return False\n",
    "    return True\n",
    "date = input('Distinguish year, month and date by .(e.g. 1917. 6.10) : ')\n",
    "if valid_date(date) == True:\n",
    "    print('This is the publication date of a Sherlock Holmes series!')\n",
    "else:\n",
    "    print('This is not the publication date of a Sherlock Holmes series or the input has an error.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "54116fde",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 4, 9, 16, 25, 36, 49]\n"
     ]
    }
   ],
   "source": [
    "a = [1,2,3,4,5,6,7]\n",
    "square_a = list(map(lambda x: x**2, a))\n",
    "print(square_a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aab85c8a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "adults list:\n",
      "34 39 20 54 "
     ]
    }
   ],
   "source": [
    "def adult_func(n):\n",
    "    if n>=19:\n",
    "        return True\n",
    "    else:\n",
    "        return False\n",
    "ages = [34,39,20,18,13,54]\n",
    "print('adults list:')\n",
    "for a in filter(adult_func, ages):\n",
    "    print(a, end=' ')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b87d5cef",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "adults list:\n",
      "34 39 20 54 "
     ]
    }
   ],
   "source": [
    "ages = [34,39,20,18,13,54]\n",
    "print('adults list:')\n",
    "for a in filter(lambda x: x >= 19, ages):\n",
    "    print(a, end=' ')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0643c6f8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 4, 9, 16, 25, 36, 49]\n"
     ]
    }
   ],
   "source": [
    "a = [1,2,3,4,5,6,7]\n",
    "square_a = list(map(lambda x: x**2, a))\n",
    "print(square_a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b3f5c5aa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n"
     ]
    }
   ],
   "source": [
    "from functools import reduce\n",
    "a = [1,2,3,4]\n",
    "n = reduce(lambda x, y: x + y, a)\n",
    "print(n)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "63515e41",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 4, 6, 8, 10]\n",
      "[1, 3, 5, 7, 9]\n"
     ]
    }
   ],
   "source": [
    "n_list = [1,2,3,4,5,6,7,8,9,10]\n",
    "even_list = []\n",
    "odd_list = []\n",
    "for a in filter(lambda x: x%2 == 0, n_list):\n",
    "    even_list.append(a)\n",
    "odd_list = set(n_list) - set(even_list)\n",
    "print(even_list)\n",
    "print(list(odd_list))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "11ee0e66",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 4, 6, 8, 10]\n"
     ]
    }
   ],
   "source": [
    "n_list = [1,2,3,4,5,6,7,8,9,10]\n",
    "even_list = list(filter(lambda x: x%2 == 0, n_list))\n",
    "print(even_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5ac1e9dc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['A', 'B', 'C', 'D']\n"
     ]
    }
   ],
   "source": [
    "a_list = ['a','b','c','d']\n",
    "def to_upper(n):\n",
    "    return n.upper()\n",
    "list_upper = list(map(to_upper, a_list))\n",
    "print(list_upper)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "46b8b108",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5050\n"
     ]
    }
   ],
   "source": [
    "from functools import reduce\n",
    "a = range(1,101)\n",
    "n = reduce(lambda x,y: x + y, a)\n",
    "print(n)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3f0c4173",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 4, 6, 4, 8, 12, 6, 12, 18]\n"
     ]
    }
   ],
   "source": [
    "product_xy = [x * y for x in [1,2,3] for y in [2,4,6]]\n",
    "print(product_xy)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "76e5424e",
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'list' object has no attribute 'values'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32mc:\\Users\\SIC\\Thun_learn_python\\Chapter three.ipynb Cell 29\u001b[0m in \u001b[0;36m<cell line: 2>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      <a href='vscode-notebook-cell:/c%3A/Users/SIC/Thun_learn_python/Chapter%20three.ipynb#X40sZmlsZQ%3D%3D?line=0'>1</a>\u001b[0m scores \u001b[39m=\u001b[39m [\u001b[39m100\u001b[39m, \u001b[39m90\u001b[39m, \u001b[39m95\u001b[39m, \u001b[39m90\u001b[39m, \u001b[39m80\u001b[39m, \u001b[39m70\u001b[39m, \u001b[39m0\u001b[39m, \u001b[39m80\u001b[39m, \u001b[39m90\u001b[39m, \u001b[39m90\u001b[39m, \u001b[39m0\u001b[39m, \u001b[39m90\u001b[39m, \u001b[39m100\u001b[39m, \u001b[39m75\u001b[39m, \u001b[39m20\u001b[39m, \u001b[39m30\u001b[39m, \u001b[39m50\u001b[39m, \u001b[39m90\u001b[39m]\n\u001b[1;32m----> <a href='vscode-notebook-cell:/c%3A/Users/SIC/Thun_learn_python/Chapter%20three.ipynb#X40sZmlsZQ%3D%3D?line=1'>2</a>\u001b[0m \u001b[39mfor\u001b[39;00m x \u001b[39min\u001b[39;00m scores\u001b[39m.\u001b[39;49mvalues():\n\u001b[0;32m      <a href='vscode-notebook-cell:/c%3A/Users/SIC/Thun_learn_python/Chapter%20three.ipynb#X40sZmlsZQ%3D%3D?line=2'>3</a>\u001b[0m     \u001b[39mprint\u001b[39m(x)\n",
      "\u001b[1;31mAttributeError\u001b[0m: 'list' object has no attribute 'values'"
     ]
    }
   ],
   "source": [
    "scores = [100, 90, 95, 90, 80, 70, 0, 80, 90, 90, 0, 90, 100, 75, 20, 30, 50, 90]\n",
    "for x in scores.values():\n",
    "    print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d3539d7e",
   "metadata": {},
   "outputs": [],
   "source": [
    "scores = [100, 90, 95, 90, 80, 70, 0, 80, 90, 90, 0, 90, 100, 75, 20, 30, 50, 90]\n",
    "print(\"The number of total students is\", len(scores)/3)\n",
    "scoreIter = iter(scores)\n",
    "valid_list = []\n",
    "for i in range(0,range(0, len(scores)/3)):\n",
    "    e = next(scoreIter)\n",
    "    m = next(scoreIter)\n",
    "    s = next(scoreIter)\n",
    "    if all([e,m,s]) == True: \n",
    "        valid_lsit.append([e,m,s])\n",
    "print(len(valid_list))\n",
    "print(\"Valid score list:\", valid_list)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "ff7b877b",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'int' object is not callable",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32mc:\\Users\\SIC\\Thun_learn_python\\Chapter three.ipynb Cell 31\u001b[0m in \u001b[0;36m<cell line: 1>\u001b[1;34m()\u001b[0m\n\u001b[1;32m----> <a href='vscode-notebook-cell:/c%3A/Users/SIC/Thun_learn_python/Chapter%20three.ipynb#X42sZmlsZQ%3D%3D?line=0'>1</a>\u001b[0m \u001b[39mprint\u001b[39m(\u001b[39mabs\u001b[39;49m(\u001b[39mint\u001b[39;49m(\u001b[39m-\u001b[39;49m\u001b[39m1\u001b[39;49m)))\n",
      "\u001b[1;31mTypeError\u001b[0m: 'int' object is not callable"
     ]
    }
   ],
   "source": [
    "X = 10\n",
    "Y = 11\n",
    "def foo():\n",
    "    x = 20\n",
    "    def bar():\n",
    "        a = 30\n",
    "        print(a,x,y)\n",
    "    bar()\n",
    "    x = 40\n",
    "    bar()\n",
    "foo()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "a31c5111",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "callfunc(greet) function call\n",
      "hello world\n"
     ]
    }
   ],
   "source": [
    "def callfunc(func):\n",
    "    func()\n",
    "def greet():\n",
    "    print(\"hello world\")\n",
    "print('callfunc(greet) function call')\n",
    "callfunc(greet)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "b7b1e3b5",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'function' object is not subscriptable",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32mc:\\Users\\SIC\\Thun_learn_python\\Chapter three.ipynb Cell 33\u001b[0m in \u001b[0;36m<cell line: 6>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      <a href='vscode-notebook-cell:/c%3A/Users/SIC/Thun_learn_python/Chapter%20three.ipynb#X44sZmlsZQ%3D%3D?line=3'>4</a>\u001b[0m     \u001b[39mreturn\u001b[39;00m a\u001b[39m-\u001b[39mb\n\u001b[0;32m      <a href='vscode-notebook-cell:/c%3A/Users/SIC/Thun_learn_python/Chapter%20three.ipynb#X44sZmlsZQ%3D%3D?line=4'>5</a>\u001b[0m l_list \u001b[39m=\u001b[39m [plus, minus]\n\u001b[1;32m----> <a href='vscode-notebook-cell:/c%3A/Users/SIC/Thun_learn_python/Chapter%20three.ipynb#X44sZmlsZQ%3D%3D?line=5'>6</a>\u001b[0m a \u001b[39m=\u001b[39m l_list[\u001b[39m0\u001b[39;49m][\u001b[39m100\u001b[39;49m,\u001b[39m200\u001b[39;49m]\n\u001b[0;32m      <a href='vscode-notebook-cell:/c%3A/Users/SIC/Thun_learn_python/Chapter%20three.ipynb#X44sZmlsZQ%3D%3D?line=6'>7</a>\u001b[0m b \u001b[39m=\u001b[39m l_list[\u001b[39m1\u001b[39m][\u001b[39m100\u001b[39m,\u001b[39m200\u001b[39m]\n\u001b[0;32m      <a href='vscode-notebook-cell:/c%3A/Users/SIC/Thun_learn_python/Chapter%20three.ipynb#X44sZmlsZQ%3D%3D?line=7'>8</a>\u001b[0m \u001b[39mprint\u001b[39m(\u001b[39m'\u001b[39m\u001b[39ma =\u001b[39m\u001b[39m'\u001b[39m, a)\n",
      "\u001b[1;31mTypeError\u001b[0m: 'function' object is not subscriptable"
     ]
    }
   ],
   "source": [
    "def plus(a,b):\n",
    "    return a+b\n",
    "def minus(a,b):\n",
    "    return a-b\n",
    "l_list = [plus, minus]\n",
    "a = l_list[0][100,200]\n",
    "b = l_list[1][100,200]\n",
    "print('a =', a)\n",
    "print('b =', b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8e1c37ea",
   "metadata": {},
   "outputs": [],
   "source": [
    "def decorate(style = 'italic'):\n",
    "    def italic(s):\n",
    "        return '<i>'+ s +'</i>'\n",
    "    def bold(s):\n",
    "        return '<b>'+ b +'</b>'\n",
    "    if style == 'italic':\n",
    "        return italic\n",
    "    else:\n",
    "        return bold\n",
    "dec = decorate()\n",
    "print(dec('Hello'))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ddb7b9d7",
   "metadata": {},
   "outputs": [],
   "source": [
    "x = 666\n",
    "def f():\n",
    "    x = 777\n",
    "    def g():\n",
    "        a = 100\n",
    "        def h():\n",
    "            nonlocal a\n",
    "            a = 333\n",
    "        h()\n",
    "        print(\"Level 2\")\n",
    "f()\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "8510f24a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "c1 1\n",
      "c1 2\n",
      "c2 1\n"
     ]
    }
   ],
   "source": [
    "def makecounter():\n",
    "    count = 0\n",
    "    def counter():\n",
    "        nonlocal count\n",
    "        count += 1\n",
    "        return count\n",
    "    return counter\n",
    "c1 = makecounter()\n",
    "c2 = makecounter()\n",
    "print('c1',c1())\n",
    "print('c1',c1())\n",
    "print('c2',c2())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "9a6e8e4f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5 7 9 11\n"
     ]
    }
   ],
   "source": [
    "def clouser():\n",
    "    a = 2\n",
    "    b = 3\n",
    "    return lambda x : a * x + b\n",
    "c = clouser()\n",
    "print(c(1), c(2), c(3), c(4))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "5b0df2c5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello\n"
     ]
    }
   ],
   "source": [
    "def greeting():\n",
    "    def say_hi():\n",
    "        print('hello')\n",
    "    say_hi()\n",
    "greeting()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "de3ab5e9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<function calc.<locals>.mul_add.<locals>.<lambda> at 0x000001CC0ABCDA60>\n"
     ]
    }
   ],
   "source": [
    "def calc():\n",
    "    a = 3\n",
    "    b = 5\n",
    "    def mul_add(x):\n",
    "        return lambda x : a * x + b\n",
    "    return mul_add\n",
    "num = calc()\n",
    "print(num(3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "506d891a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5 12 21 32 45 60 77\n"
     ]
    }
   ],
   "source": [
    "def calc():\n",
    "    a = 2\n",
    "    b = 3\n",
    "    total = 0\n",
    "    def mult_add(x):\n",
    "        nonlocal total\n",
    "        total += a * x + b\n",
    "        return total\n",
    "    return mult_add\n",
    "c = calc()\n",
    "print(c(1), c(2), c(3), c(4), c(5), c(6), c(7))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "b01b09b1",
   "metadata": {},
   "outputs": [
    {
     "ename": "Terminator",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTerminator\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32mc:\\Users\\SIC\\Thun_learn_python\\Chapter three.ipynb Cell 41\u001b[0m in \u001b[0;36m<cell line: 2>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      <a href='vscode-notebook-cell:/c%3A/Users/SIC/Thun_learn_python/Chapter%20three.ipynb#X55sZmlsZQ%3D%3D?line=0'>1</a>\u001b[0m \u001b[39mimport\u001b[39;00m \u001b[39mturtle\u001b[39;00m \u001b[39mas\u001b[39;00m \u001b[39mt\u001b[39;00m\n\u001b[1;32m----> <a href='vscode-notebook-cell:/c%3A/Users/SIC/Thun_learn_python/Chapter%20three.ipynb#X55sZmlsZQ%3D%3D?line=1'>2</a>\u001b[0m t\u001b[39m.\u001b[39;49msetup(width \u001b[39m=\u001b[39;49m \u001b[39m400\u001b[39;49m, height \u001b[39m=\u001b[39;49m \u001b[39m400\u001b[39;49m)\n\u001b[0;32m      <a href='vscode-notebook-cell:/c%3A/Users/SIC/Thun_learn_python/Chapter%20three.ipynb#X55sZmlsZQ%3D%3D?line=2'>3</a>\u001b[0m \u001b[39mfor\u001b[39;00m i \u001b[39min\u001b[39;00m \u001b[39mrange\u001b[39m(\u001b[39m200\u001b[39m):\n\u001b[0;32m      <a href='vscode-notebook-cell:/c%3A/Users/SIC/Thun_learn_python/Chapter%20three.ipynb#X55sZmlsZQ%3D%3D?line=3'>4</a>\u001b[0m     t\u001b[39m.\u001b[39mforward(i)\n",
      "File \u001b[1;32m<string>:5\u001b[0m, in \u001b[0;36msetup\u001b[1;34m(width, height, startx, starty)\u001b[0m\n",
      "\u001b[1;31mTerminator\u001b[0m: "
     ]
    }
   ],
   "source": [
    "import turtle as t\n",
    "t.setup(width = 400, height = 400)\n",
    "for i in range(200):\n",
    "    t.forward(i)\n",
    "    t.left(98)\n",
    "t.done()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "c068dd07",
   "metadata": {},
   "outputs": [
    {
     "ename": "Terminator",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTerminator\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32mc:\\Users\\SIC\\Thun_learn_python\\Chapter three.ipynb Cell 42\u001b[0m in \u001b[0;36m<cell line: 7>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      <a href='vscode-notebook-cell:/c%3A/Users/SIC/Thun_learn_python/Chapter%20three.ipynb#X56sZmlsZQ%3D%3D?line=3'>4</a>\u001b[0m GLASS_COLOR \u001b[39m=\u001b[39m \u001b[39m'\u001b[39m\u001b[39m#9acedc\u001b[39m\u001b[39m'\u001b[39m\n\u001b[0;32m      <a href='vscode-notebook-cell:/c%3A/Users/SIC/Thun_learn_python/Chapter%20three.ipynb#X56sZmlsZQ%3D%3D?line=4'>5</a>\u001b[0m GLASS_SHADOW \u001b[39m=\u001b[39m \u001b[39m'\u001b[39m\u001b[39m'\u001b[39m\n\u001b[1;32m----> <a href='vscode-notebook-cell:/c%3A/Users/SIC/Thun_learn_python/Chapter%20three.ipynb#X56sZmlsZQ%3D%3D?line=6'>7</a>\u001b[0m s \u001b[39m=\u001b[39m turtle\u001b[39m.\u001b[39;49mgetscreen()\n\u001b[0;32m      <a href='vscode-notebook-cell:/c%3A/Users/SIC/Thun_learn_python/Chapter%20three.ipynb#X56sZmlsZQ%3D%3D?line=7'>8</a>\u001b[0m t \u001b[39m=\u001b[39m turtle\u001b[39m.\u001b[39mTurtle()\n\u001b[0;32m     <a href='vscode-notebook-cell:/c%3A/Users/SIC/Thun_learn_python/Chapter%20three.ipynb#X56sZmlsZQ%3D%3D?line=9'>10</a>\u001b[0m \u001b[39m# it can move forward backward left right\u001b[39;00m\n",
      "File \u001b[1;32m<string>:5\u001b[0m, in \u001b[0;36mgetscreen\u001b[1;34m()\u001b[0m\n",
      "\u001b[1;31mTerminator\u001b[0m: "
     ]
    }
   ],
   "source": [
    "import turtle\n",
    "\n",
    "BODY_COLOR =  'red'\n",
    "GLASS_COLOR = '#9acedc'\n",
    "GLASS_SHADOW = ''\n",
    "\n",
    "s = turtle.getscreen()\n",
    "t = turtle.Turtle()\n",
    "\n",
    "# it can move forward backward left right\n",
    "def body():\n",
    "    \"\"\" draws the body \"\"\"\n",
    "    t.pensize(20)\n",
    "    #t.speed(15)\n",
    "\n",
    "    t.fillcolor(BODY_COLOR)\n",
    "    t.begin_fill()\n",
    "\n",
    "    # right side\n",
    "    t.right(90)\n",
    "    t.forward(50)\n",
    "    t.right(180)\n",
    "    t.circle(40, -180)\n",
    "    t.right(180)\n",
    "    t.forward(200)\n",
    "\n",
    "    # head curve\n",
    "    t.right(180)\n",
    "    t.circle(100, -180)\n",
    "\n",
    "    # left side\n",
    "    t.backward(20)\n",
    "    t.left(15)\n",
    "    t.circle(500, -20)\n",
    "    t.backward(20)\n",
    "\n",
    "    #t.backward(200)\n",
    "    t.circle(40, -180)\n",
    "    #t.right(90)\n",
    "    t.left(7)\n",
    "    t.backward(50)\n",
    "\n",
    "    # hip\n",
    "    t.up()\n",
    "    t.left(90)\n",
    "    t.forward(10)\n",
    "    t.right(90)\n",
    "    t.down()\n",
    "    #t.right(180)\n",
    "    #t.circle(25, -180)\n",
    "    t.right(240)\n",
    "    t.circle(50, -70)\n",
    "\n",
    "    t.end_fill()\n",
    "\n",
    "\n",
    "def glass():\n",
    "    t.up()\n",
    "    #t.right(180)\n",
    "    t.right(230)\n",
    "    t.forward(100)\n",
    "    t.left(90)\n",
    "    t.forward(20)\n",
    "    t.right(90)\n",
    "\n",
    "    t.down()\n",
    "    t.fillcolor(GLASS_COLOR)\n",
    "    t.begin_fill()\n",
    "\n",
    "    t.right(150)\n",
    "    t.circle(90, -55)\n",
    "\n",
    "    t.right(180)\n",
    "    t.forward(1)\n",
    "    t.right(180)\n",
    "    t.circle(10, -65)\n",
    "    t.right(180)\n",
    "    t.forward(110)\n",
    "    t.right(180)\n",
    "    \n",
    "    #t.right(180)\n",
    "    t.circle(50, -190)\n",
    "    t.right(170)\n",
    "    t.forward(80)\n",
    "\n",
    "    t.right(180)\n",
    "    t.circle(45, -30)\n",
    "\n",
    "    t.end_fill()\n",
    "\n",
    "def backpack():\n",
    "    t.up()\n",
    "    t.right(60)\n",
    "    t.forward(100)\n",
    "    t.right(90)\n",
    "    t.forward(75)\n",
    "\n",
    "    t.fillcolor(BODY_COLOR)\n",
    "    t.begin_fill()\n",
    "\n",
    "    t.down()\n",
    "    t.forward(30)\n",
    "    t.right(255)\n",
    "\n",
    "    t.circle(300, -30)\n",
    "    t.right(260)\n",
    "    t.forward(30)\n",
    "\n",
    "    t.end_fill()\n",
    "\n",
    "\n",
    "body()\n",
    "glass()\n",
    "backpack()\n",
    "\n",
    "t.screen.exitonclick()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "c1157ccc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<re.Match object; span=(0, 4), match='Life'>\n",
      "None\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'Life'"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import re\n",
    "txt1 = 'Life is too short, you need python'\n",
    "txt2 = 'The best moments of my life'\n",
    "print(re.search('Life', txt1))\n",
    "print(re.search('Life',txt2))\n",
    "match = re.search('Life',txt1)\n",
    "match.group()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "9122325d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "None\n"
     ]
    }
   ],
   "source": [
    "import re\n",
    "txt1 = 'Who are you to judge the life I live'\n",
    "txt2 = 'The best moments of my life'\n",
    "print(re.search('life$',txt1))\n",
    "re.findall('o',txt1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "8fe63b4d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Result list divided by 5 or 7 =  [5, 7, 10, 14, 15, 20, 21, 25, 28, 30, 35, 35, 40, 42, 45, 49, 50, 55, 56, 60, 63, 65, 70, 70, 75, 77, 80, 84, 85, 90, 91, 95, 98, 100]\n"
     ]
    }
   ],
   "source": [
    "lst = [i for i in range(1,101)]\n",
    "def func1(a):\n",
    "    def func2():\n",
    "        result1 = []\n",
    "        for i in lst:\n",
    "            if i % 5 == 0:\n",
    "                result1.append(i)\n",
    "        return result1\n",
    "    def func3():\n",
    "        result2 = []\n",
    "        for i in lst:\n",
    "            if i % 7 == 0:\n",
    "                result2.append(i)\n",
    "        return result2\n",
    "    result = func2() + func3() \n",
    "    return result\n",
    "print(\"Result list divided by 5 or 7 = \", sorted(func1(lst)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "23ac480c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<re.Match object; span=(0, 3), match='ABA'>\n",
      "None\n",
      "None\n",
      "None\n",
      "None\n",
      "None\n",
      "None\n",
      "<re.Match object; span=(1, 4), match='ABB'>\n",
      "<re.Match object; span=(1, 7), match='ABBBBB'>\n",
      "<re.Match object; span=(0, 1), match='A'>\n",
      "<re.Match object; span=(0, 1), match='A'>\n",
      "None\n",
      "<re.Match object; span=(3, 4), match='A'>\n",
      "<re.Match object; span=(1, 4), match='ABB'>\n",
      "<re.Match object; span=(1, 7), match='ABBBBB'>\n"
     ]
    }
   ],
   "source": [
    "import re\n",
    "print(re.search('A.A','ABA'))\n",
    "print(re.search('A.A','ABBA'))\n",
    "print(re.search('A.A','ABBBA'))\n",
    "print(re.search('AB+','A'))\n",
    "print(re.search('AB+','AA'))\n",
    "print(re.search('AB+','J-Hope'))\n",
    "print(re.search('AB+','X-MAN'))\n",
    "print(re.search('AB+','CABBA'))\n",
    "print(re.search('AB+','CABBBBBA'))\n",
    "print(re.search('AB*','A'))\n",
    "print(re.search('AB*','AA'))\n",
    "print(re.search('AB*','J-Hope'))\n",
    "print(re.search('AB*','X-MAN'))\n",
    "print(re.search('AB*','CABBA'))\n",
    "print(re.search('AB*','CABBBBBA'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "0d8bcba1",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (2851914068.py, line 18)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Input \u001b[1;32mIn [26]\u001b[1;36m\u001b[0m\n\u001b[1;33m    return 'The Balance of {}'s account {} is {:,} won.'.format(self.name, self.account_num, self.balance)\u001b[0m\n\u001b[1;37m                              ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "\n",
    "class BankAccount:\n",
    "    def __init__(self, name, account_num, balance = 0):\n",
    "        self.name = nameself.accont_num = account_numself.balance = balance\n",
    "    def get_name():\n",
    "        return self.name()\n",
    "    def get_account_num():\n",
    "        return self.account_num\n",
    "    def deposit(self,amount):\n",
    "        self.balance += amount\n",
    "        print('{} won has been deposited. The balance is {} won.'.format(amount, self.balance))\n",
    "        return self.balance\n",
    "    def withdraw(self, amout):\n",
    "        if self.balance - amount > 0:\n",
    "            self.balance -= amount\n",
    "        else:\n",
    "            print('The account balance is {} won. This is smaller rthan the request amount of withdraw {} won'.format(self.balance, amount))\n",
    "    def __str__(self):\n",
    "        return 'The Balance of {}'s account {} is {:,} won.'.format(self.name, self.account_num, self.balance)\n",
    "acount1 = BankAccount(\"David\", \"1234,0001\")\n",
    "print(account1)\n",
    "acount1.deposit(2000)\n",
    "print(account1)\n",
    "account1.withdraw(500)\n",
    "print(account1)\n",
    "account1.withdraw(5000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "5e1b1719",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "meow meow~~~\n"
     ]
    }
   ],
   "source": [
    "class cat:\n",
    "    def meow(self):\n",
    "        print('meow meow~~~')\n",
    "nabi = cat()\n",
    "nabi.meow()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f86b1055",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "meow meow~~~\n",
      "meow meow~~~\n",
      "meow meow~~~\n"
     ]
    }
   ],
   "source": [
    "class cat :\n",
    "    def meow(self):\n",
    "        print('meow meow~~~')\n",
    "nabi = cat()\n",
    "nabi.meow()\n",
    "nero = cat()\n",
    "nero.meow()\n",
    "mimi = cat()\n",
    "mimi.meow()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "2edd5862",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<__main__.cat object at 0x00000182097C58E0>\n",
      "<__main__.cat object at 0x00000182097C5640>\n",
      "My name is nabi, color is black, meow meow~~\n",
      "My name is nero, color is white, meow meow~~\n",
      "meow meow~~~\n"
     ]
    }
   ],
   "source": [
    "class cat :\n",
    "    def __init__(self, name, color):\n",
    "        self.name = name\n",
    "        self.color = color\n",
    "    def meow(self):\n",
    "        print('My name is {}, color is {}, meow meow~~'.format(self.name, self.color))\n",
    "nabi = cat('nabi','black')\n",
    "nero = cat('nero', 'white')\n",
    "print(nabi)\n",
    "print(nero)\n",
    "nabi.meow()\n",
    "nero.meow()\n",
    "mimi.meow()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "62f6e398",
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'circle' object has no attribute '_circle__name'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32mc:\\Users\\SIC\\Thun_learn_python\\Chapter three.ipynb Cell 51\u001b[0m in \u001b[0;36m<cell line: 8>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      <a href='vscode-notebook-cell:/c%3A/Users/SIC/Thun_learn_python/Chapter%20three.ipynb#Y101sZmlsZQ%3D%3D?line=5'>6</a>\u001b[0m     \u001b[39mdef\u001b[39;00m \u001b[39marea\u001b[39m(\u001b[39mself\u001b[39m):\n\u001b[0;32m      <a href='vscode-notebook-cell:/c%3A/Users/SIC/Thun_learn_python/Chapter%20three.ipynb#Y101sZmlsZQ%3D%3D?line=6'>7</a>\u001b[0m         \u001b[39mreturn\u001b[39;00m \u001b[39mself\u001b[39m\u001b[39m.\u001b[39m__PI \u001b[39m*\u001b[39m \u001b[39mself\u001b[39m\u001b[39m.\u001b[39m__raius \u001b[39m*\u001b[39m\u001b[39m*\u001b[39m \u001b[39m2\u001b[39m\n\u001b[1;32m----> <a href='vscode-notebook-cell:/c%3A/Users/SIC/Thun_learn_python/Chapter%20three.ipynb#Y101sZmlsZQ%3D%3D?line=7'>8</a>\u001b[0m c1 \u001b[39m=\u001b[39m circle(\u001b[39m\"\u001b[39;49m\u001b[39mc1\u001b[39;49m\u001b[39m\"\u001b[39;49m, \u001b[39m4\u001b[39;49m,\u001b[39m3.14\u001b[39;49m)\n\u001b[0;32m      <a href='vscode-notebook-cell:/c%3A/Users/SIC/Thun_learn_python/Chapter%20three.ipynb#Y101sZmlsZQ%3D%3D?line=8'>9</a>\u001b[0m \u001b[39mprint\u001b[39m(\u001b[39m\"\u001b[39m\u001b[39mArea of c1:\u001b[39m\u001b[39m\"\u001b[39m, c1\u001b[39m.\u001b[39marea())\n\u001b[0;32m     <a href='vscode-notebook-cell:/c%3A/Users/SIC/Thun_learn_python/Chapter%20three.ipynb#Y101sZmlsZQ%3D%3D?line=9'>10</a>\u001b[0m c2 \u001b[39m=\u001b[39m circle(\u001b[39m\"\u001b[39m\u001b[39mc2\u001b[39m\u001b[39m\"\u001b[39m, \u001b[39m6\u001b[39m,\u001b[39m3.141\u001b[39m)\n",
      "\u001b[1;32mc:\\Users\\SIC\\Thun_learn_python\\Chapter three.ipynb Cell 51\u001b[0m in \u001b[0;36mcircle.__init__\u001b[1;34m(self, name, radius, PI)\u001b[0m\n\u001b[0;32m      <a href='vscode-notebook-cell:/c%3A/Users/SIC/Thun_learn_python/Chapter%20three.ipynb#Y101sZmlsZQ%3D%3D?line=1'>2</a>\u001b[0m \u001b[39mdef\u001b[39;00m \u001b[39m__init__\u001b[39m(\u001b[39mself\u001b[39m, name, radius, PI):\n\u001b[1;32m----> <a href='vscode-notebook-cell:/c%3A/Users/SIC/Thun_learn_python/Chapter%20three.ipynb#Y101sZmlsZQ%3D%3D?line=2'>3</a>\u001b[0m     \u001b[39mself\u001b[39;49m\u001b[39m.\u001b[39;49m__name \u001b[39m==\u001b[39m name\n\u001b[0;32m      <a href='vscode-notebook-cell:/c%3A/Users/SIC/Thun_learn_python/Chapter%20three.ipynb#Y101sZmlsZQ%3D%3D?line=3'>4</a>\u001b[0m     \u001b[39mself\u001b[39m\u001b[39m.\u001b[39m__radius \u001b[39m==\u001b[39m radius\n\u001b[0;32m      <a href='vscode-notebook-cell:/c%3A/Users/SIC/Thun_learn_python/Chapter%20three.ipynb#Y101sZmlsZQ%3D%3D?line=4'>5</a>\u001b[0m     \u001b[39mself\u001b[39m\u001b[39m.\u001b[39m__PI \u001b[39m=\u001b[39m PI\n",
      "\u001b[1;31mAttributeError\u001b[0m: 'circle' object has no attribute '_circle__name'"
     ]
    }
   ],
   "source": [
    "class circle:\n",
    "    def __init__(self, name, radius, PI):\n",
    "        self.__name == name\n",
    "        self.__radius == radius\n",
    "        self.__PI = PI\n",
    "    def area(self):\n",
    "        return self.__PI * self.__raius ** 2\n",
    "c1 = circle(\"c1\", 4,3.14)\n",
    "print(\"Area of c1:\", c1.area())\n",
    "c2 = circle(\"c2\", 6,3.141)\n",
    "print(\"Area of c2:\", c2.area())\n",
    "c3 = circle(\"c3\", 5,3.1415)\n",
    "print(\"Area of c3:\", c3.area())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "55df95ea",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "success\n"
     ]
    }
   ],
   "source": [
    "class Stack:\n",
    "    def __init__(self):\n",
    "        self.stack = []\n",
    "    def is_empty(self):\n",
    "        return True if len(self.stack) == 0 else False\n",
    "    def push(self, item):\n",
    "        self.stack.append(item)\n",
    "    def pop(self):\n",
    "        return None if self.is_empty() else self.stack.pop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9c346d52",
   "metadata": {},
   "outputs": [],
   "source": [
    "def check_parentheses(expr):\n",
    "    opening = \"[{(\"\\\n",
    "    closing = \")}]\"\n",
    "    stack = Stack()\n",
    "    for char in expr:\n",
    "        if char in opening:\n",
    "            stack.puch(char)\n",
    "        elif char in closing:\n",
    "            if stack.is_empty():\n",
    "                return False "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "5d2d350a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Input the stringt of HTML docement: <html> <body> <h1> </h1> <p> </p> <ul> <li> </li> <li> </li> <li> </li> </ul> </body> </html>\n",
      "<html> <body> <h1> </h1> <p> </p> <ul> <li> </li> <li> </li> <li> </li> </ul> </body> </html> "
     ]
    }
   ],
   "source": [
    "text = input(\"Input the stringt of HTML docement: \")\n",
    "start = text.find('<')\n",
    "while start != -1:\n",
    "    end = text.find('>', start + 1)\n",
    "    tag = text[start:end + 1]\n",
    "    print(tag, end = ' ')\n",
    "    start = text.find('<', end + 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d88de7d2",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  },
  "vscode": {
   "interpreter": {
    "hash": "1424bbd6e5dad52fbf0c33910f427463eeb871d0831968cdb45995310ea244b2"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
