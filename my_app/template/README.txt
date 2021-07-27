Hello!

Thank you for downloading my Flask template website. Before you get going, there
are a few things you should be aware of.The template is designed to allow users 
to immediately have about 95% of a website and provide the majority of back-end 
content, but there are three easy steps required.

First, feel free to search the entire document for the word 'Item'. I have used
this word to stand in for default classes. If, for example, you are making an 
API for automobiles, you may want to replace the word 'Item' to be 'Car' or
whatever your API displays as appropriate. Be aware as well that these are 
case-sensitive; sometimes the 'item' is a variable while 'Item' is a class. 
VS Code has nifty tools to search and replace with Regex so you don't have to 
worry about it.
(TLDR: Make sure you copy formatting.)

Second, you will have to add a database and initialize it. Go to:

https://www.elephantsql.com/ 

Once there, create a profile for yourself, and create a database instance. Once 
you are there, you'll want to copy paste the URL from ElephantSQL to the .env 
file in the Flask template base. PLEASE NOTE: Because we are using 
SQLAlchemy, we need to add the characters 'ql' after 'postgres' in the database 
URI. This is because SQLAlchemy reads a little differently than ElephantSQL or 
PGAdmin4. For example: "postgres://template_master" should be modified to 
"postgresql://template_master". 

Lastly, you will want to instantiate the database. With the terminal open to 
your downloaded website, you will want to type the following commands: 
"flask db init", "flask db migrate", and "flask db upgrade". Do this AFTER the 
other two steps mentioned above (replacing the word Item and linking the 
database). 

Further directions can be 
found here: https://flask-migrate.readthedocs.io/en/latest/ 

After this, it is all up to you - you can style your database at 
main_folder/static/css/main.css and change HTML files in site/site_templates, 
authentication/auth_templates, and /templates.

Thank you so much for visiting my application, and if you have comments or 
questions please feel free to contact me at apolbrandon@gmail.com. 