#       Dependency Resolver
##      Summary
#####   The goal of this project is to build a dependency resolver that returns the set of classes that need to be complied before the base class. It takes in classes and their         dependencies and provides a way to fetch all the dependencies for a given class including even those that are transitively dependent.
##      Usage
####    Adding dependencies:
        add_dependency(base: str, depend_list: list)
        
        @parameter 
        base is the class to which the dependencies are associated
        depend_list contains the list of classes that the base class is dependent on
       
####    get dependencies:
        get_dependency(base: str)
        
        @parameter
        base is the class for which dependencies need to be retrieved
        
        @return
        complete list of classes the base class is dependent on
