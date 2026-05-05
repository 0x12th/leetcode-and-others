"""
You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. Your task is to transform this absolute path into its simplified canonical path.
The rules of a Unix-style file system are as follows:
A single period '.' represents the current directory.
A double period '..' represents the previous/parent directory.
Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, '...' and '....' are valid directory or file names.
The simplified canonical path should follow these rules:
The path must start with a single slash '/'.

Input: path = "/home/"
Output: "/home"
"""


def simplifyPath(path: str) -> str:
    res, dirs = [], [dir for dir in path.split("/") if dir]
    for dir_ in dirs:
        if dir_ not in (".", ".."):
            res.append(dir_)
        if res and dir_ == "..":
            res.pop()

    return "/" + "/".join(res)
