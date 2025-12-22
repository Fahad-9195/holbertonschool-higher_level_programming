# Python - Serialization

## Project Badge
**Python - Serialization**  
Level: Novice  
Author: Javier Valenzani  
Weight: 1

## Description
This project explores **marshaling** and **serialization**, two essential concepts used to transform data into formats suitable for storage or transmission. The project focuses on understanding how Python handles serialization and how data can be preserved, transferred, and reconstructed across systems.

You will gain hands-on experience converting Python objects into serial formats such as JSON, and restoring them back into usable Python data structures.

## Introduction

### What is Marshaling?
Marshaling is the process of converting in-memory objects into a standardized format that can be transmitted or stored. It is commonly used in distributed systems, such as remote procedure calls (RPC), where data must be transferred between different environments or architectures.

### What is Serialization?
Serialization is a specific form of marshaling that focuses on converting data structures or object states into a format that can be saved to disk or sent over a network, and later reconstructed exactly as they were.

Serialization is widely used in:
- Data persistence
- Web applications
- Network communication
- Distributed systems

## Learning Objectives
By the end of this project, you should be able to:

- Explain the differences and similarities between marshaling and serialization
- Implement serialization in Python
- Convert Python objects to serialized formats
- Deserialize data back into Python objects
- Understand the use of serialized data in web apps, databases, and networks
- Compare serialization formats such as JSON, XML, and binary formats
- Analyze performance implications of different serialization methods

## Resources
Read or watch:
- Real Python – Serialization
- Real Python: Working With JSON Data in Python
- Python `pickle` documentation
- Corey Schafer – Pickle
- CSV to JSON in Python
- Python XML ElementTree Guide
- Socket Programming Guide

## Requirements

### Python Scripts
- OS: Ubuntu 20.04 LTS
- Python version: 3.8.x
- Allowed editors: `vi`, `vim`, `emacs`
- First line of each file must be:
  ```bash
  #!/usr/bin/python3
