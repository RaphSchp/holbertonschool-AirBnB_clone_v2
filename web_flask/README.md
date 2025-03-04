<div align="center">
    <h1>🖼️ AirBnB clone - Web framework 🏡</h1>
</div>

![Holberton School Logo](https://uploads-ssl.webflow.com/64107f65f30b69371e3d6bfa/6480d99a4643eeded57474df_Holberton%20actual%20digital%20france.png)

![UBUNTU](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

## Description

This project is to understand what is Python and how use it, it was made in the software development program of [Holberton School](https://www.holbertonschool.fr/).

# Learning Objectives

At the end of this project, you are expected to be able to <a href="https://fs.blog/feynman-learning-technique/">explain to anyone</a>, **without the help of Google:**

## General

* What is a Web Framework
* How to build a web framework with Flask
* How to define routes in Flask
* What is a route
* How to handle variables in a route
* What is a template
* How to create a HTML response in Flask by using a template
* How to create a dynamic template (loops, conditions…)
* How to display in HTML data from a MySQL database

# Requirements

## Python Scripts

* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.7.*)
* All your files must be executable
* The length of your files will be tested using `wc`
* All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## HTML/CSS Files

* Allowed editors: `vi`, `vim`, `emacs`
* All your files should end with a new line
* A `README.md` file at the root of the folder of the project is mandatory
* Your code should be W3C compliant and validate with <a href="https://github.com/hs-hq/W3C-Validator">W3C-Validator</a> (except for jinja template)
* All your CSS files should be in the `styles` folder
* All your images should be in the `images` folder
* You are not allowed to use `!important` or id (`#...` in the CSS file)
* All tags must be in uppercase
* Current screenshots have been done on `Chrome 56.0.2924.87`.
* No cross browsers

# More Info

## MySQL Default charset issues

* If you get Flask errors after executing the `curl ...` commands, it might be because of the `DEFAULT CHARSET`. If it’s `DEFAULT CHARSET=latam1`, you might want to change it to `DEFAULT CHARSET=utf8mb4`, either on the server’s config file (/etc/mysql/my.cnf commonly) orm on the CREATE DATABASE statement.

## Install Flask

```
$ pip3 install Flask
```

<p align="center">
  <img src="/images/hbnb_step3.png" alt="Requirements">
</p>

[![AirBnB Clone Demo](https://img.youtube.com/vi/lzs4nQOiZQY/0.jpg)](https://youtu.be/lzs4nQOiZQY)

# NOTE:

* Try setting FLASK configuration `debug` to `False` if you get the following error when running the checker:

```
 - [Got]
rpc error: code = 2 desc = oci runtime error: exec failed: container_linux.go:290: starting container process caused "process_linux.go:111: decoding init error from pipe caused \"read parent: connection reset by peer\""


(222 chars long)
```

# Manual QA Review

**It is your responsibility to request a review for this project from a peer before the project’s deadline. If no peers have been reviewed, you should request a review from a TA or staff member.**

## :radio_button: Author

* Raphaël Schopfer <a href="https://github.com/RaphSchp" rel="nofollow"><img align="center" alt="github" src="https://www.vectorlogo.zone/logos/github/github-tile.svg" height="24" /></a>

## :radio_button: License

This program is distributed under the terms of the Holberton license.