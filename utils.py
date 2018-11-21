import subprocess as subp

def grep(**kwargs):
    """Wrapper for the grep command line utility
    If return code isn't 0, raise an exception with the code.
        **kwargs:
            "e": string to pass as "-e" options (can be list)
            "r": boolean for recursive operation
            "file": file or directory with files with which to match (can be list)
    """
    grepArgs = ["grep"]

    # All arguments that can be either string or list
    # We convert them to list first
    for symbol in ["e", "file"]:
        if symbol in kwargs and type(kwargs[symbol]) == str:
            kwargs[symbol] = [ kwargs[symbol] ]

    if "r" in kwargs:
        grepArgs += ["-r"]

    if "e" in kwargs:
        [ grepArgs.extend(["-e", i]) for i in kwargs["e"] ]

    if "file" in kwargs:
        grepArgs += kwargs["file"]

    ret = subp.check_output(grepArgs).decode("utf8")

    return ret


