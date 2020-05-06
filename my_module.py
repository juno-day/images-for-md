
# change directory to script directory
import os
def cd_to_script_dir():
    """Change to directory the script is running from
    
    Returns:
        [str] -- [path to script directory]
    """
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    return dname

