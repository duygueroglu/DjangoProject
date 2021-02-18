# DjangoProject :white_check_mark: :pencil:

![](https://img.shields.io/badge/version-1.0-orange) ![](https://img.shields.io/badge/issues-5%20closed-green) 
[![Linkedin](https://i.stack.imgur.com/gVE0j.png) Duygu Eroglu](https://www.linkedin.com/in/duygu-eroglu-75428796/)

It's a dynamic to-do web app project that is created with python's django framework.

![](https://github.com/duygueroglu/DjangoProject/blob/main/todo_app/img/homepage.png)


![](https://github.com/duygueroglu/DjangoProject/blob/main/todo_app/img/adminpage.png)

Features
=============

1. There was used csrf_token for secure login.

![](https://github.com/duygueroglu/DjangoProject/blob/main/todo_app/img/login.png)

```python
<form class="d-flex" method="POST">
      {% csrf_token %}
        <input class="form-control me-2" type="text" placeholder="Add to list" name="title">
        <button class="btn btn-outline-success" type="submit">Add To-Do List</button>
      </form>
```

2. You can select todos to change in admin page and also home page.
3. You can delete todos in admin page and home page.
4. You can change todos' finishing status in home page and also admin page. 

Clone
=============
```
git clone https://github.com/duygueroglu/DjangoProject.git
```

Create Environment and Install
=============
Install Python3 virtualenv dependencies for run the server.
```
 pip install virtualenv

 virtualenv DjangoEnv
```

Usage
=============

```
cd DjangoProject\DjangoEnv\Scripts

& .\Activate

cd DjangoProject\todo_project

python manage.py runserver
```
Server will be started at port 8000.  
![](https://github.com/duygueroglu/DjangoProject/blob/main/todo_app/img/opening.png)

Used Technologies
=============
![](https://github.com/duygueroglu/DjangoProject/blob/main/todo_app/img/technologies.png)

Author
=============
👤 Duygu Eroğlu
* Github: [@duygueroglu](https://github.com/duygueroglu "@duygueroglu")
* Linkedin: [Duygu Eroğlu](https://www.linkedin.com/in/duygu-eroglu-75428796/ "Duygu Eroğlu")
