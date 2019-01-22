import importlib

class Extension:
    def __init__(self, name, path, module_name, class_name, type_name):
        self.name = name
        self.path = path
        self.class_name = class_name
        self.module_name = module_name
        self.type = type_name
        self._class = None


    def get(self):
        if(not self._class):
            spec = importlib.util.spec_from_file_location(self.module_name, self.path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
        
            self._class = module.__getattribute__(self.class_name)
        
        return self._class


    def get_rank(self):
        return self.get().__rank__()