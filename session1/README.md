# Python Exam – Session 1

**Duration:** 2 Hours  
**Total Marks:** 100  
**Session Focus:** Fundamentals, Loops, Strings, Lists, and Basic Theory

---

## Question 1 – FizzBuzz (10 Marks)

**Instructions:**  
Write a program that prints the numbers from 1 to 100.  
But for multiples of **3**, print `"Fizz"` instead of the number, and for multiples of **5**, print `"Buzz"`.  
For numbers which are multiples of **both 3 and 5**, print `"FizzBuzz"`.

**Example Output:**
```
1  
2  
Fizz  
4  
Buzz  
...  
14  
FizzBuzz  
```

**Marks Allocation:**
| Criteria | Marks |
|-----------|-------|
| Correct output and logic | 6 |
| Clean, readable code (indentation, naming) | 2 |
| Correct use of conditionals and loops | 2 |

---
## Question 2 – Pattern Printing (25 Marks)

**Instructions:**  
Write programs to print the following patterns using loops.  
Each pattern must be generated dynamically based on a variable `n` (e.g. `n = 5`).

### (a) Right-Angled Triangle
```
*
**
***
****
*****
```

### (b) Inverted Triangle
```
*****
****
***
**
*
```

### (c) Diamond Shape
```
  *
 ***
*****
 ***
  *
```

**Marks Allocation:**
| Criteria | Marks |
|-----------|-------|
| Right-angled triangle | 8 |
| Inverted triangle | 8 |
| Diamond shape | 7 |
| Proper formatting, code readability | 2 |

🧩 **Hint:**  
For the diamond, combine an upward and a downward triangle using spaces and stars.  
Make sure your pattern remains centered when `n` changes

---




## Question 3 – Word Frequency Counter (25 Marks)

**Instructions:**  
Write a function called `"word_frequency(sentence)"` that takes a string and returns a dictionary showing how many times each word appears.  
Ignore case and punctuation.

**Example:**
```python
Input: "The cat and the hat."
Output: {"the": 2, "cat": 1, "and": 1, "hat": 1}
```

**Marks Allocation:**
| Criteria | Marks |
|-----------|-------|
| Accurate counting logic | 10 |
| Proper string handling (case & punctuation) | 5 |
| Correct use of dictionary | 5 |
| Clean, efficient code | 5 |

---

## Question 4 – List Analyzer (30 Marks)

**Instructions:**  
Write a function called `"analyze_list(numbers)"` that takes a list of integers and returns a dictionary with:
- `"sum"`: total of all numbers  
- `"average"`: mean value  
- `"unique"`: number of unique elements  
- `"max"`: largest number  
- `"min"`: smallest number  

**Example:**
```python
Input: [1, 2, 3, 4, 4, 5]
Output: {"sum": 19, "average": 3.166..., "unique": 5, "max": 5, "min": 1}
```

**Marks Allocation:**
| Criteria | Marks |
|-----------|-------|
| Correct computations (sum, avg, etc.) | 15 |
| Proper handling of empty list | 5 |
| Efficient code and structure | 5 |
| Readability and naming conventions | 5 |

---

## Question 5 – Mini Theory (10 Marks)

**Instructions:**  
Answer the following conceptual questions briefly **in comments** within your Python file.

1. What is the difference between `"is"` and `"=="` in Python?  
2. What is the difference between a **list** and a **tuple**?  
3. What does it mean that strings are **immutable** in Python?  
4. What is the difference between a **function** and a **method**?  
5. What is the purpose of `"if __name__ == '__main__':"` ?

**Marks Allocation:**
| Criteria | Marks |
|-----------|-------|
| Each correct explanation | 2 × 5 = 10 |

---


Each test file should import the relevant question module and verify the output of functions.

---

**End of Session 1 – Total: 100 Marks**
