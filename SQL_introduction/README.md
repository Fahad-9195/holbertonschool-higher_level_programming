# MySQL - Introduction

## Description
This project covers the fundamentals of **databases**, **relational databases**, and **SQL** using **MySQL 8.0**.  
You will practice writing SQL scripts that create and modify database structures (**DDL**) and manipulate/query data (**DML / SELECT**), including subqueries and common MySQL functions.

## Learning Objectives
By the end of this project, you should be able to explain (without Google):

- What a database is
- What a relational database is
- What SQL stands for
- What MySQL is
- How to create a database in MySQL
- What DDL and DML stand for
- How to `CREATE` or `ALTER` a table
- How to `SELECT` data from a table
- How to `INSERT`, `UPDATE`, or `DELETE` data
- What subqueries are
- How to use MySQL functions

## Requirements
- OS: **Ubuntu 22.04 LTS**
- MySQL: **MySQL 8.0** (project environment uses MySQL 8.0.x)
- Allowed editors: `vi`, `vim`, `emacs`
- All files must end with a new line
- Each SQL file must:
  - Start with a comment describing the task
  - Have a comment just **before** each SQL query
  - Use **UPPERCASE** for SQL keywords (`SELECT`, `WHERE`, `INSERT`, ...)
- A `README.md` file is mandatory at the root of the project folder

## Setup MySQL (Ubuntu 22.04)
```bash
sudo apt update
sudo apt install -y mysql-server
sudo service mysql start
mysql --version
