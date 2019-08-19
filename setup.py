from distutils.core import setup

#This is a list of files to install, and where
#(relative to the 'root' dir, where setup.py is)
#You could be more specific.
files = ["moudles/*"]

setup(name = "piglib",
    version = "0.1.0",
    description = "pigglib",
    author = "QiaanYicheng",
    author_email = "qsp2020@outlook.com",
    url = "https://github.com/Easonqsp/piglib",
    #Name the folder where your packages live:
    #(If you have other packages (dirs) or modules (py files) then
    #put them into the package directory - they will be found 
    #recursively.)
    packages = ['piglib'],
    #'package' package must contain files (see list above)
    #I called the package 'package' thus cleverly confusing the whole issue...
    #This dict maps the package name =to=> directories
    #It says, package *needs* these files.
    package_data = {'piglib' : files },
    #'runner' is in the root.
    scripts = ["test.py"],
    #long_description = """Really long text here.""" 
    #
    #This next part it for the Cheese Shop, look a little down the page.
    #classifiers = []     
) 
