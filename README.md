#       Dependency Resolver
##      Summary
#####   The goal of this project is to identify and return the full set of dependencies for any given objects.
##      Usage
####    Adding dependencies:
        add_dependency(base: str, depend_list: list)
        @parameter base is the object to which the dependencies are associated with
                   depend_list contains the list of objects that the base object is dependent on
        
