
 Si la version de Python est < 3.3, on dispose pas de venv. 
 Dans cette cas il faut installer la dernière version de Python.
 Pour créer et activer l'environnement virtuel on va utiliser
 le tterminal ( Linux, Mac os ), cmd (Windows).
 
 Avec les commandes:"python -m venv --help" et "python --version"
 on va vérifier ci on dispose des bons outils pour créer un
 environnement virtuel.
 
 Pour créer un env, on va utiliser la commande " python3 -m venv env " :
 
 vitalie@vitalie-HP-Compaq-6200-Pro-SFF-PC:~/example$ python3 -m venv env
 vitalie@vitalie-HP-Compaq-6200-Pro-SFF-PC:~/example$ ls
 env  test.py
 vitalie@vitalie-HP-Compaq-6200-Pro-SFF-PC:~/example$
 
 Pour activer l'environnement, exécutez "source env/bin/activate" :
 
 vitalie@vitalie-HP-Compaq-6200-Pro-SFF-PC:~/example$ source env/bin/activate
 (env) vitalie@vitalie-HP-Compaq-6200-Pro-SFF-PC:~/example$ 
 (env) vitalie@vitalie-HP-Compaq-6200-Pro-SFF-PC:~/example$

  Le BASH ajoutera au début de chaque ligne de terminal (‘env’) 
 
 Pour exécuter le code d'application 'test.py", avec la commade "pip install"
 on va installer d'abord les paquets nécessaire :
 
 (env) vitalie@vitalie-HP-Compaq-6200-Pro-SFF-PC:~/example$ pip install requests
 
 Installing collected packages: charset-normalizer, certifi, urllib3, idna, requests
 Successfully installed certifi-2021.5.30 charset-normalizer-2.0.6 idna-3.2 
 (env) vitalie@vitalie-HP-Compaq-6200-Pro-SFF-PC:~/example$

 La commande "pip freeze" pour vérification :
 
 (env) vitalie@vitalie-HP-Compaq-6200-Pro-SFF-PC:~/example$ pip freeze
 certifi==2021.5.30
 charset-normalizer==2.0.6
 idna==3.2
 requests==2.26.0
 urllib3==1.26.7
 (env) vitalie@vitalie-HP-Compaq-6200-Pro-SFF-PC:~/example$
  

 Mentent avec la commande "python3 test.py" on exécite le cod :
 
 (env) vitalie@vitalie-HP-Compaq-6200-Pro-SFF-PC:~/example$ python3 test.py
  200
 (env) vitalie@vitalie-HP-Compaq-6200-Pro-SFF-PC:~/example$ 

 
 


 
