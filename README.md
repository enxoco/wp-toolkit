# WP Toolkit

## What?
A simple tool to automate creating a new Wordpress project in my local dev environment.

* Creates a new project folder using passed in project name.
* Pulls down the latest version of Wordpress into new project directory.
* (Optional) Switches to /wp-content/themes/ and pulls down a custom theme from Wordpress.
* Creates a new Database for the project
* Replaces username/password/database name in wp-config-sample.php with provided values and copies it to wp-config.php.
* (Optional) Sets the new project up to be served using valet.

## Running Source
The only dependency needed to run this tool is the mysql-connector library.

```bash
pip install mysql-connector
```

Then you can simply run it
```bash
python wp-toolkit.py
```

Or, if you want an executable binary you can
```
$: pip install pyinstaller
$: pyinstaller wp-toolkit.py -F
27 INFO: PyInstaller: 3.6
27 INFO: Python: 3.6.8
5482 INFO: Building EXE because EXE-00.toc is non existent
5482 INFO: Building EXE from EXE-00.toc
...
...
5483 INFO: Appending archive to ELF section in EXE /tmp/wp-toolkit/dist/wp-toolkit
5499 INFO: Building EXE from EXE-00.toc completed successfully.

$: ls 
build  dist  __pycache__  README.md  wp-toolkit.py  wp-toolkit.spec
$: ls dist/
    wp-toolkit 

murph@pop-os:/tmp/wp-toolkit$ ./dist/wp-toolkit 
/usr/bin/git
Enter DB user: 