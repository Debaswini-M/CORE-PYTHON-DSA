# Binary Search with Multiple Inputs (Python)

This repository demonstrates an implementation of **Binary Search in Python**
along with a wrapper function that allows searching for **multiple user inputs**
in a sorted list.

The goal of this project is to practice algorithmic thinking, recursion,
and clean separation of concerns.

---

## 📌 Features

- Recursive binary search implementation
- Supports multiple search queries in a single run
- Returns index if the element exists
- Gracefully handles values not present in the list
- Clean and beginner-friendly code structure

---

## 🧠 How It Works

1. **`binary_search()`**
   - Performs recursive binary search on a sorted list
   - Returns the index of the target if found
   - Returns `None` if the target does not exist

2. **`binary_search_multipleargs()`**
   - Accepts multiple target values
   - Calls binary search for each value
   - Stores results in a dictionary `{value: index}`

3. **`verify()`**
   - Displays human-readable output
   - Clearly indicates whether each input exists in the list

---

## ▶️ Example Usage

**Input**: 12,33,44
**Output**:
Number 12 is found in the list at index 2
Sorry,Dude! The number 33 doesn't exist in the list..
Sorry,Dude! The number 44 doesn't exist in the list..

Process finished with exit code 0
---

---

## 🛠 Tech Stack

- Python 3.x
- No external libraries required

---

## ⚠️ Important Notes

- The list must be **sorted** for binary search to work correctly
- Indices returned are based on the current recursive slice
- This implementation focuses on clarity over optimization

---

## 🌱 What I Learned

- Binary search is naturally a **single-target algorithm**
- Supporting multiple inputs requires a wrapper function
- Why early `return` statements break multi-input logic
- The importance of separating responsibilities between functions

---

⭐ If you find this repository useful, feel free to star it.



