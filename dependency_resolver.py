
class DependencyResolver:

    def __init__(self) -> None:
        '''Initializing the dictionary that will hold the dependency relationship'''
        self.dep_map = {}
    
    def add_dependency(self, base: str, depend_list: list):
        '''Stores new classes and there corresponding dependencies'''
        if not base:
            raise Exception('invalid input')
        if not depend_list:
            raise Exception('invalid input')
        if base in self.dep_map:
            self.dep_map[base].extend(depend_list)
        else:
            self.dep_map[base] = depend_list

    def get_dependency(self, base: str):
        '''Returns the list of dependencies for the given class'''
        if not base:
            raise Exception('invalid input')
        exc_order = []
        visited = []
        visited.append(base)
        isCycle = self.__get_sub_dependency_list(base,visited,exc_order)
        if isCycle:
            raise Exception('cycle detected in Dependency list')
        return exc_order

    def __get_sub_dependency_list(self, base: str, visited: list, exc_order: list):
        '''Returns if the dependency is cyclic and updates the exc_order variable with the dependencies
        of base'''
        if not self.dep_map.get(base):
                visited.remove(base)
                return False
        for dep in self.dep_map[base]:
            if dep not in visited:
                visited.append(dep)
                if dep not in exc_order:
                    exc_order.append(dep)
                if self.__get_sub_dependency_list(dep,visited, exc_order) == True:
                    return True
            else:
                return True
        visited.remove(base)