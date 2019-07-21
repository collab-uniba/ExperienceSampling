import os, platform

def lock(LOCK_PATH):
    """Returns true if other instances are running. This function uses a lock file."""
    
    is_running = False

    if os.name == 'nt' or platform.system() == 'Windows' or 'cygwin' in platform.system().lower():
        try:
            if os.path.exists(LOCK_PATH):
                os.unlink(LOCK_PATH)
            fh = os.open(LOCK_PATH, os.O_CREAT | os.O_EXCL | os.O_RDWR)
        except EnvironmentError as err:
            if err.errno == 13:
                is_running = True
            else:
                raise
    else:
        import fcntl
        try:
            fh = open(LOCK_PATH, 'w')
            fcntl.lockf(fh, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except EnvironmentError as err:
            if fh is not None:
                is_running = True
            else:
                raise 

    return is_running