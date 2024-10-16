# Math formulas

```This library implements functions for calculating perimeter and area for a circle, rectangle and triangle```

## Area calculation functions
- Circle: 
```python
import math
def area(r): return math.pi * r * r
```

```python
a = 5
circle_area = area(a)
```


- Rectangle: 
```python
def area(a, b):
    return a * b
```

```python
a = 5
b = 10
rectangle_area = area(a, b)
```

- Square:
```python
def area(a):
    return a * a
```

```python
a = 5
b = 10
square_area = area(a, b)
```

- Triangle:
```python
def area(a, h):
    return a * h / 2
```
```python
a = 5
h = 10
triangle_area = area(a, h)
```

## Perimeter calculation functions
- Circle:
```python
import math
def perimeter(r):
    return 2 * math.pi * r
```
```python
a = 5
circle_perimeter = perimeter(a)
```

- Rectangle:
```python
def perimeter(a, b):
    return 2 * (a + b)
```
```python
a = 5
b = 10
rectangle_perimeter = perimeter(a, b)
```

- Square:
```python
def perimeter(a):
    return 4 * a
```
```python
a = 5
b = 10
square_perimeter = perimeter(a, b)
```

- Triangle:
```python
def perimeter(a, b, c):
    return a + b + c
```
```python
a = 5
b = 10
triangle_perimeter = perimeter(a, b)
```

# change log
- commit be43a51c0aac1c80df879375e520038b553ad785
- Author: Gleb <408820@edu.itmo.ru>
- Date:   Thu Sep 19 09:13:45 2024 +0300

#### Добавлен новый файл triangle.py

- commit c945964b7b6b05575b7464ce86b3e278651ba45f
- Author: Gleb <408820@edu.itmo.ru>
- Date:   Thu Sep 19 09:12:13 2024 +0300

#### Добавлен новый файл rectangle.py

- commit d078c8d9ee6155f3cb0e577d28d337b791de28e2 (origin/main, origin/HEAD, main)
- Author: smartiqa <info@smartiqa.ru>
- Date:   Thu Mar 4 14:55:29 2021 +0300
