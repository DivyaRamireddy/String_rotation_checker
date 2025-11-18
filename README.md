# 🔄 String Rotation Checker 
> Check if one string is a **rotation** of another string.

### ✔ Example  
str1 = "abcde"  
str2 = "cdeab"  
Output → Rotation ✔️  

---

## 🔹 Key Insight (Important Trick)
If str2 is a rotation of str1,  
then str2 will ALWAYS appear inside **str1 + str1**.

Example:  
"abcde" + "abcde" = "abcdeabcde"  
"cdeab" appears in it.

This is the logic asked in top interviews.

---

## 🧠 Concepts Used
- String concatenation
- Substring search
- Logical pattern matching
- Length validation

---

## 🚀 How to Run
```bash
python string_rotation_checker.py# String_rotation_checker
