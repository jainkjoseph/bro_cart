to activate environment
cd ..
source bro_env/bin/activate
after activation
cd bro_cart

to runserver : python3 manage.py runserver

gitubunto commands - pythone & django installation
	python3 -- version       // to check preinstalled python3  
	sudo apt install python3-pip  // to install pip
	
	sudo apt install python3-venv    // to venv install venv
	python3 -m venv <sample_env>    // to create vertual environment variable

	source <sample_env>/bin/activate

	(env\Scripts\activate) for windows

	<sample_env> pips3 install django
	django-admin --version
	
	dnango-admin startproject <project_name>
	cd <project_name>
	git init & .gitignore setting-root folder
	git add .gitignore
	pythone3 manage.py runserver
	python3 manage.py startapp <app_name>
	
git commands

	git add .add 
	git log / git log --all
	git status  // to display modified file details
	git restore folder_name/file_name  // restore git add  files
	###git check-ignore -v folder_name/file_name  // restore before edit mode

	git restore --staged folder/filename
	git restore folder_name/file_name  // restore git add  files

	git commit -m "message"

	

	git remote add <origin-remote_namhttps://github.com/jainkjoseph/newbrocart.git
	(copy & paste from git folder)
	git remote             // to display remote name- origin
	git remote -v          // to display remote url
	git push <origin> <master>    // master is branch name
	                             //to upload to git site
	Deleting folder from git repository
	Method 1: 
		from command prompt:> git rm -r --cached /d/Django/ikqs/brokart/customers/migrations
		git add .
		git commit -m "msg"
		git push <remote_name> <branch_name>
		uid: jainkjoseph
		pwd: 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
		

	Method 2:
		brows the directory (migrations) in your repository that you want to delete. Inthe top-right
		corner, selecthe dropdown menu, then click Delete Directory. type commit message
		back to git cmd prompt
`		git pull (to download from server)
		
	git clone  <url>    // clone a repository to our computer
	
ubunto commands
	
	ls   - display directory
	ls -a   - to display hidden files
	cd <folder_name>
	pwd   - display current path
	mkdir  <folder_name>
    rm -r .git   // to remove directory
    git branch  - - delete old_branch
    
	touch  text.txt     /file creationg
	mv text.txt
	rm text.txt
	
	sudo   for install
	apt-get  // for help install, update, remove

VS code setting
	create new folder before starting new project
	open folder from Vs code
	install extension Save Typing
    code .   type from terminal to open vs code

psql commands


\l  - display list of database
\c <database>  - connect specified database
 select * from <table>;
\q – exit postgres Shell
\password [USERNAME] – to change database password
\drop databse <database> - delete database  (before connection-\c)
 \password      --- to change default password  - ubundo compulsory 

		
	                             
	                             
	
	