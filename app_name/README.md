
> # **Readme Structure**
- [PYTHON](#python)
- [BOWER](#bower)
- [EXTRA](#extra)


Just click `module_name` to go there. ✨


# Python
```bash
# First time install the required libraries
$ pip install -t lib -r requirements.txt 

# Upgrade /force reinstall the libraries 
$ pip install --upgrade -t lib -r requirements.txt
$ pip install --upgrade --force-reinstall -t lib -r requirements.txt
```

# Bower
```bower
# Install all components
$ bower install

# Update components based on bower.json file
$ bower update

# Cleans extra packages based on bower.json file
$ bower prune

# Install new package and save it to bower.json file
$ bower install "package name" --save
```

# Yarn
```yarn
# Create package.json
$ yarn init

# Install the required package
$ yarn install <pkg_name>

# Install the required package and add it to package.json
$ yarn install <pkg_name>

# Install dependencies from package.json
$ yarn install

# Install dependencies from package.json in the specified directory
$ yarn install --modules-folder "main/static/node_modules"
```