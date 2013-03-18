#!/usr/bin/python2.7

# A class to interface LTspice with Python

def find_file(path, exename):
    import os
    for root, dirs, files in os.walk(path):
        if exename in files:
            return os.path.join(root, exename)
    return None # Not found
        
def find_in_PATH(exename):
    """ Finds filename in $PATH. Returns None if not found the file. """
    import os
    PATH = os.environ["PATH"].split(':')
    
    for path in PATH:
        found_file =  find_file(path,exename)
        if found_file is not None:
            return found_file
    
    return None
    
def find_LTspice_exe(path):
    """ Does what the name says: finds the LTspice EXE file. """
    import os
    exename = "scad3.exe"
    return find_file(path, exename)


class LTspice(object):
    
    operating_system = None
    exename = None
    netlist_name = None
    parameters = None
        
    def __init__(self,path=None):
        import platform, os
        """ Creates the LTspice object: tries to find where LTspice 
            is installed, otherwise fails. """
        
        if path is None: # No path was given: we're left on our own.
            # http://stackoverflow.com/questions/1854/
            self.operating_system = platform.system()
        
            if 'Windows' in self.operating_system:
                # cf.: http://stackoverflow.com/questions/1283664
                # XXX: I do not have Windows so I can't test this.
                program_files_path = os.environ["ProgramFiles"]
            elif 'Linux' in self.operating_system:
                # Assume we're using Wine
                program_files_path = os.environ["HOME"]
            else:
                raise IOError, "Please give the path for LTspice manually \
                                 when creating the object. Alternatively, \
                                 add a case for your OS."
        
            self.exename = find_LTspice_exe(program_files_path)
            if self.exename is None:
                raise IOError, "Can't find LTspice in your /home or in Program Files."
            else:
                print "Found LTspice exe at: ", self.exename
        else:
            self.exename = path

    def run(self):
        pass
        
        
            
        
