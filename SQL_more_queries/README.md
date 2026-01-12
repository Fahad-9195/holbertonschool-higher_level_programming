# MySQL - Advanced Queries

## Description
This project focuses on advanced SQL concepts using **MySQL 8.0**, including user management, privileges, constraints, joins, subqueries, and relational database design principles such as normalization and ER modeling.

You will practice creating MySQL users, granting and revoking privileges, defining table constraints, and writing complex queries that retrieve data from multiple related tables.

## Learning Objectives
By the end of this project, you should be able to explain (without Google):

- How to create a new MySQL user
- How to manage privileges for a user on a database or a table
- What a PRIMARY KEY is
- What a FOREIGN KEY is
- How to use NOT NULL and UNIQUE constraints
- How to retrieve data from multiple tables in one request
- What subqueries are
- What JOIN and UNION are

## Requirements
- OS: **Ubuntu 20.04 LTS**
- MySQL: **MySQL 8.0.25**
- Allowed editors: `vi`, `vim`, `emacs`
- All files must end with a new line
- Each SQL file must:
  - Start with a comment describing the task
  - Have a comment just **before** each SQL query
  - Use **UPPERCASE** for SQL keywords (`SELECT`, `WHERE`, `JOIN`, etc.)
- A `README.md` file is mandatory at the root of the project folder
- File length will be checked using `wc`

## Setup MySQL (Ubuntu 20.04)
> Skip this if you are using the provided sandbox.

```bash
sudo apt update
sudo apt install mysql-server
mysql --version
sudo mysql
