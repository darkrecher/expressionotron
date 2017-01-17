# Installation de flask

Version python :
Python 3.4.4 (v3.4.4:737efcadf5a6, Dec 20 2015, 20:20:57) [MSC v.1600 64 bit (AM
D64)] on win32

## Test de pip (foiré)

`pip` tout court, en ligne de commande, reste bloqué. (Pas de message, il faut faire Ctr-C pour quitter)

`pip install flask` : pareil.

## Upgrade de pip (foiré/inutile)

https://pip.pypa.io/en/stable/installing/

http://stackoverflow.com/questions/6587507/how-to-install-pip-with-python-3

Lancement d'un upgrade de pip. (Dans une console MS-DOS en pas administrateur)
Ça se termine en erreur.

C:\Recher\projets\expressionotron\repo_git\expressionotron\www>python -m pip install -U pip

    Collecting pip
      Downloading pip-8.0.2-py2.py3-none-any.whl (1.2MB)
        100% |################################| 1.2MB 49kB/s
    Installing collected packages: pip
      Found existing installation: pip 7.1.2
        Uninstalling pip-7.1.2:
          Successfully uninstalled pip-7.1.2
    Exception:
    Traceback (most recent call last):
      File "C:\Python34\lib\shutil.py", line 375, in _rmtree_unsafe
        os.unlink(fullname)
    PermissionError: [WinError 5] Accès refusé: 'C:\\Users\\Recher\\AppData\\Local\\
    Temp\\pip-gliz4uvh-uninstall\\python34\\scripts\\pip.exe'

    During handling of the above exception, another exception occurred:

    Traceback (most recent call last):
      File "C:\Python34\lib\site-packages\pip\basecommand.py", line 211, in main
        # and when it is done, isinstance is not needed anymore
      File "C:\Python34\lib\site-packages\pip\commands\install.py", line 311, in run

      File "C:\Python34\lib\site-packages\pip\req\req_set.py", line 657, in install
        for subreq in dist.requires(available_requested):
      File "C:\Python34\lib\site-packages\pip\req\req_install.py", line 729, in comm
    it_uninstall
        if dist.has_metadata('entry_points.txt'):
      File "C:\Python34\lib\site-packages\pip\req\req_uninstall.py", line 152, in co
    mmit
        )
      File "C:\Python34\lib\site-packages\pip\_vendor\retrying.py", line 49, in wrap
    ped_f
        return Retrying(*dargs, **dkw).call(f, *args, **kw)
      File "C:\Python34\lib\site-packages\pip\_vendor\retrying.py", line 212, in cal
    l
        raise attempt.get()
      File "C:\Python34\lib\site-packages\pip\_vendor\retrying.py", line 247, in get

        six.reraise(self.value[0], self.value[1], self.value[2])
      File "C:\Python34\lib\site-packages\pip\_vendor\six.py", line 659, in reraise
        _assertCountEqual = "assertItemsEqual"
      File "C:\Python34\lib\site-packages\pip\_vendor\retrying.py", line 200, in cal
    l
        attempt = Attempt(fn(*args, **kwargs), attempt_number, False)
      File "C:\Python34\lib\site-packages\pip\utils\__init__.py", line 90, in rmtree

        if os.path.basename(sys.argv[0]) in ('__main__.py', '-c'):
      File "C:\Python34\lib\shutil.py", line 482, in rmtree
        return _rmtree_unsafe(path, onerror)
      File "C:\Python34\lib\shutil.py", line 372, in _rmtree_unsafe
        _rmtree_unsafe(fullname, onerror)
      File "C:\Python34\lib\shutil.py", line 372, in _rmtree_unsafe
        _rmtree_unsafe(fullname, onerror)
      File "C:\Python34\lib\shutil.py", line 377, in _rmtree_unsafe
        onerror(os.unlink, fullname, sys.exc_info())
      File "C:\Python34\lib\site-packages\pip\utils\__init__.py", line 102, in rmtre
    e_errorhandler
    PermissionError: [WinError 5] Accès refusé: 'C:\\Users\\Recher\\AppData\\Local\\
    Temp\\pip-gliz4uvh-uninstall\\python34\\scripts\\pip.exe'


Lancement de la même commande en mode administrateur.
Ça se termine sans erreur. (Mais il est possible que ça n'ait rien fait d'utile)

Récupération de get-pip.py. En mode administrateur, exécution de `python get-pip.py`
Ça se termine sans erreur. (Mais à nouveau, il est possible que ça n'ait rien fait d'utile)

En mode administrateur, exécution de la commande `pip install flask`. Ce n'est pas mieux, ça reste bloqué.
Même chose avec `pip install Flask` (il y a un F majuscule).

(Je ne sais plus si tout cela a été testé avec le PowerShell ou avec la console MS-DOS classique)

## Installation de flask (réussie)

http://stackoverflow.com/questions/35099372/pip-install-somepackage-freezes-powershell

Powershell ou MS-DOS classique, en mode administrateur :

C:\Python34>python.exe -m pip install Flask

    Collecting Flask
      Downloading Flask-0.10.1.tar.gz (544kB)
        100% |################################| 544kB 56kB/s
    Collecting Werkzeug>=0.7 (from Flask)
      Downloading Werkzeug-0.11.3-py2.py3-none-any.whl (305kB)
        100% |################################| 307kB 90kB/s
    Collecting Jinja2>=2.4 (from Flask)
      Downloading Jinja2-2.8-py2.py3-none-any.whl (263kB)
        100% |################################| 266kB 46kB/s
    Collecting itsdangerous>=0.21 (from Flask)
      Downloading itsdangerous-0.24.tar.gz (46kB)
        100% |################################| 49kB 57kB/s
    Collecting MarkupSafe (from Jinja2>=2.4->Flask)
      Downloading MarkupSafe-0.23.tar.gz
    Building wheels for collected packages: Flask, itsdangerous, MarkupSafe
      Running setup.py bdist_wheel for Flask ... done
      Stored in directory: C:\Users\Recher\AppData\Local\pip\Cache\wheels\d2\db\61\c
    b9b80526b8f3ba89248ec0a29d6da1bb6013681c930fca987
      Running setup.py bdist_wheel for itsdangerous ... done
      Stored in directory: C:\Users\Recher\AppData\Local\pip\Cache\wheels\97\c0\b8\b
    37c320ff57e15f993ba0ac98013eee778920b4a7b3ebae3cf
      Running setup.py bdist_wheel for MarkupSafe ... done
      Stored in directory: C:\Users\Recher\AppData\Local\pip\Cache\wheels\94\a7\79\f
    79a998b64c1281cb99fa9bbd33cfc9b8b5775f438218d17a7
    Successfully built Flask itsdangerous MarkupSafe
    Installing collected packages: Werkzeug, MarkupSafe, Jinja2, itsdangerous, Flask

    Successfully installed Flask-0.10.1 Jinja2-2.8 MarkupSafe-0.23 Werkzeug-0.11.3 i
    tsdangerous-0.24

Lancement de python et test de `import flask` : ça marche.

## Installation de pytest (réussie aussi)

Pas besoin de lancer en mode administrateur, pas besoin de se mettre dans le répertoire Python34.
Mais le "-m" est vraiment nécessaire.


C:\Recher\projets\expressionotron\repo_git\expressionotron>python -m pip install pytest

    Collecting pytest
      Downloading pytest-2.8.7-py2.py3-none-any.whl (151kB)
        100% |################################| 155kB 655kB/s
    Collecting py>=1.4.29 (from pytest)
      Downloading py-1.4.31-py2.py3-none-any.whl (81kB)
        100% |################################| 86kB 655kB/s
    Collecting colorama (from pytest)
      Downloading colorama-0.3.6-py2.py3-none-any.whl
    Installing collected packages: py, colorama, pytest
    Successfully installed colorama-0.3.6 py-1.4.31 pytest-2.8.7

