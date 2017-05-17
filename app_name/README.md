
> # **Readme Structure**
- [PYTHON](#python)
- [BOWER](#bower)
- [EXTRA](#extra)


Just click `module_name` to go there. ✨


# Python
```bash
$ pip install -t lib -r requirements.txt # prima instalare a librariilor
$ pip install --upgrade -t lib -r requirements.txt - upgrade
```

# Bower
```bower
$ bower install
# Instaleaza toate componentele

$ bower update
# Update la cerintele bower.json

$ bower prune
# Curata pachetele in plus fata de bower.json

$ bower install "package name" --save
# Instalare pachet nou
```

# Yarn
```yarn
$ yarn init
# Creaza package.json

$ yarn install <pkg_name>
# Instaleaza pachetul respectiv

$ yarn install <pkg_name>
# Instaleaza pachetul respectiv si il adauga in package.json

$ yarn install
# Instalare dependente din package.json

$ yarn install --modules-folder "main/static/node_modules"
# Instalare dependente din package.json in direcotrul specificat
```