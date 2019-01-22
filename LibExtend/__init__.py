from LibExtend.Descriptor import Descriptor

import glob
import operator

class ExtensionCatalogue:

    def __init__(self, namespace, directiories=[], search_system=True):
        # Save the namespace
        self.namespace = namespace

        descriptor_files = []

        for directiory in directiories:
            # Find all extension descriptor files under the namespace
            descriptor_files += glob.glob(directiory + "/**.ledr")

        if(search_system):
            # Find all in system dir
            descriptor_files += glob.glob("/usr/share/extensions/%s/**.ledr" % self.namespace)

        self.extensions = set()

        for desc_file in descriptor_files:
            # Read the description
            description = open(desc_file, 'r').read()

            # Add extensions to list
            self.extensions.update(Descriptor.get_extensions(description))

    
    def best(self, of_type):
        """Get the best ranked extension of a type"""
        ranked = []

        for extension in self.extensions:
            if(extension.type == of_type):
                rank = extension.get_rank()
                if(rank >= 0):
                    ranked.append((rank, extension.name, extension))

        sorted_rank = sorted(ranked, key=operator.itemgetter(0, 1))

        return sorted_rank[0][2]


    def get_all(self, of_type):
        """Get all extensions of a type"""
        filtered = set()

        for extension in self.extensions:
            if(extension.type == of_type):
                filtered.add(extension)

        return filtered



    