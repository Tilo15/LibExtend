from LibExtend.Extension import Extension
import operator

class Descriptor:
    @staticmethod
    def get_extensions(data: str):
        extensions = set()
        lines = data.splitlines()

        for i, line in enumerate(lines):
            if(line.startswith(">")):
                # Name and type follows
                name, type_name = line[1:].split(":")

                name = name.strip()
                type_name = type_name.strip()

                # Next line holds path
                path = lines[i+1]

                # Last line holds module and class name
                module, class_name = lines[i+2].rsplit(".", 1)

                # Create the extension
                extensions.add(Extension(name, path, module, class_name, type_name))

        return extensions
        
