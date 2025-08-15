# Dev Dash

**Note:** This repository was created for my college competition.

## Problem Statements

### 1. Odd Sum Challenge
**Scenario:** Malware Payload Filtering  
You are analyzing network packets from a suspected malware communication channel. The threat intelligence system flags all packet sizes that are odd numbers as suspicious. Your task is to sum the sizes of all suspicious packets to estimate the total data being exfiltrated.  

**Statement:**  
Write a program that takes `N` packet sizes and returns the sum of all odd packet sizes.  

**Sample Input/Output:**  
- Input:  
  Number of elements in an array/list: 5  
  Elements of the list/array: 2 7 4 9 3  
  Output: 19  

- Input:  
  Number of elements in an array/list: 6  
  Elements of the list/array: 10 21 32 43 54 65  
  Output: 129  

- Input:  
  Number of elements in an array/list: 8  
  Elements of the list/array: 99 100 101 102 103 104 105 106  
  Output: 408  

---

### 2. Binary Count  
**Scenario:** Bitmask Permissions Audit  
In a Linux server audit, file permissions are stored as binary bitmasks. A `1` indicates a granted permission. You need to count how many permissions are enabled for a given file.  

**Statement:**  
Given a number representing the permission bitmask, count the number of `1`s in its binary form.  

**Sample Input/Output:**  
- Input: An integer value: 5  
  Output: Number of ones in its binary value: 2  

- Input: An integer value: 29  
  Output: Number of ones in its binary value: 4  

- Input: An integer value: 1023  
  Output: Number of ones in its binary value: 10  

---

### 3. Anagram Checker  
**Scenario:** Malicious Code Signature Matching  
In a malware detection lab, some malware authors shuffle variable names to evade signature-based detection. If two code snippets contain the same set of identifiers, they are likely variants of the same malware.  

**Statement:**  
Check if two given strings are anagrams of each other (case-insensitive). Print `"YES"` or `"NO"`.  

**Sample Input/Output:**  
- Input:  
  Primary String: listen  
  Anagram of primary string: silent  
  Output: YES  

- Input:  
  Primary String: exploit  
  Anagram of primary string: tolexpi  
  Output: YES  

- Input:  
  Primary String: ransomware  
  Anagram of primary string: warm reason  
  Output: NO  

---

## Details 

- **College Name:** [Velalar College of Engineering and Technology](https://www.velalarengg.ac.in/)
- **Department:** [Computer Science and Engineering](https://www.velalarengg.ac.in/departments/department-of-cse-accredited-by-nba/)
- **Club Name:** Hackers Bay
