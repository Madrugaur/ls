import winreg

""" 
brief: Returns a dict containing the tuples of registry info 
"""
def readConsoleReg():
    # access the registry containing user preferences
    access_registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
    # access the key containing all of the information concerning the command prompt
    access_key = winreg.OpenKey(access_registry, r"Console")
    values = dict()
    # accessing the key to open the registry directories under
    i = 0
    while True:
        try:
            _name, _data, _type = winreg.EnumValue(access_key, i)
            values[_name] = _data
            i += 1
        except OSError:
            break
    return values

if __name__ == '__main__':
    print(readConsoleReg())