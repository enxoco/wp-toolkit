import os
import mysql.connector
import calendar
import time

if os.system('which git') != "":
    git_installed = True

cur_dir = os.getcwd()
ts = calendar.timegm(time.gmtime())
db_pass = 'password'
db_user = input("Enter DB user: ")
mydb = mysql.connector.connect(
  host="localhost",
  user=f"{db_user}",
  passwd="password"
)

project_name = input("Enter project name: ")
# Convert spaces and underscores to dashes
project_name = project_name.replace(' ', '-')
project_name = project_name.lower().replace('_', '-')
db_name = project_name.replace('-', '_')

createFolder = input(f"Create folder {project_name} in {cur_dir} ? (Y/N)")
if createFolder.upper() == "Y":
    try:
        os.mkdir(project_name)
        if git_installed:
            os.chdir(project_name)

            print("Creating directory and pulling down Wordpress")
            os.system('git clone https://github.com/WordPress/WordPress.git .')

            print("Creating wp-config.php...")

            try:
                wp_sample = open("wp-config-sample.php", "rt")
                wp_config = open("wp-config.php", "wt")

                checkWords = ("database_name_here", "username_here", "password_here")
                repWords = (db_name, db_user, db_pass)

                for line in wp_sample:
                    for check, rep in zip(checkWords, repWords):
                        line = line.replace(check, rep)
                    wp_config.write(line)
                wp_sample.close()
                wp_config.close()

                mycursor = mydb.cursor()

                try:
                    mycursor.execute("SHOW DATABASES")
                    for x in mycursor:
                        if x[0] == db_name:
                            print('Database already exists.')
                            exit(8)
                    mycursor.execute(f"CREATE DATABASE {db_name}")
                    use_valet = input("Serve site using Valet? ")
                    if use_valet:
                        os.system('valet park')
                        os.system('valet link')
                except:
                    print("Something went wrong")
                    print(sys.exc_info()[0])
                install_custom_theme = input("Install Custom theme? (Y/N)")
                if install_custom_theme.upper() == "Y":
                    os.chdir("wp-content/themes")
                    print("Cloning custom theme")
                    os.system('git clone git@github.com:enxoco/Simple-Bootstrap-Hero.git')
                    os.chdir("Simple-Bootstrap-Hero")
                    os.system('git checkout iown_theme')
            except:
                print("Something went wrong with config file")
    except:
        print("Something went wrong.  Does this project already exist in this location?")
