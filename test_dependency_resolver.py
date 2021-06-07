from dependency_resolver import DependencyResolver
import unittest

class DependencyResolverTest(unittest.TestCase):
    '''unit test cases for dependency resolver'''
    def test_add_dependency(self):
        depend_obj = DependencyResolver()
        with self.assertRaises(Exception) as context:
            depend_obj.add_dependency('',['B','C'])
        self.assertTrue('invalid input' in str(context.exception))
        with self.assertRaises(Exception) as context:
            depend_obj.add_dependency('A',[])
        self.assertTrue('invalid input' in str(context.exception))
        with self.assertRaises(Exception) as context:
            depend_obj.add_dependency(None,['B','C'])
        self.assertTrue('invalid input' in str(context.exception))
        with self.assertRaises(Exception) as context: 
            depend_obj.add_dependency('A',None)
        self.assertTrue('invalid input' in str(context.exception))
    
    def test_get_dependency_input(self):
        depend_obj = DependencyResolver()
        depend_obj.add_dependency('A',['B','C'])
        with self.assertRaises(Exception) as context:
            depend_obj.get_dependency('')
        self.assertTrue('invalid input' in str(context.exception))
        with self.assertRaises(Exception) as context:
            depend_obj.get_dependency(None)
        self.assertTrue('invalid input' in str(context.exception))
    
    def test_get_dependency_positive(self):
        depend_obj = DependencyResolver()
        depend_obj.add_dependency('A',['B','C'])
        depend_obj.add_dependency('B',['C','E'])
        depend_obj.add_dependency('C',['G'])
        depend_obj.add_dependency('D',['A','F'])
        depend_obj.add_dependency('E',['F'])
        depend_obj.add_dependency('F',['H'])

        self.assertListEqual(['B', 'C', 'G', 'E', 'F', 'H'],depend_obj.get_dependency('A'))
        self.assertListEqual(['C', 'G', 'E', 'F', 'H'],depend_obj.get_dependency('B'))
        self.assertListEqual(['G'],depend_obj.get_dependency('C'))
        self.assertListEqual(['A', 'B', 'C', 'G', 'E', 'F', 'H'],depend_obj.get_dependency('D'))
        self.assertListEqual(['F', 'H'],depend_obj.get_dependency('E'))
        self.assertListEqual(['H'], depend_obj.get_dependency('F'))
        self.assertListEqual([], depend_obj.get_dependency('G'))
        self.assertListEqual([], depend_obj.get_dependency('H'))

    def test_set_dependency_negative(self):
            depend_obj = DependencyResolver()
            depend_obj.add_dependency('A',['B'])
            depend_obj.add_dependency('B',['C'])
            depend_obj.add_dependency('C',['A'])
            
            with self.assertRaises(Exception) as context:
                depend_obj.get_dependency('A')
            self.assertTrue('cycle detected in Dependency list' in str(context.exception))


if __name__ == '__main__':
    unittest.main()



