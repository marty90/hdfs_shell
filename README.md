HDFS Shell
==========
A simple HDFS shell. Use it to browse into HDFS directories.

# Install
Simply clone the repo, and install it:
```
git https://github.com/marty90/hdfs_shell
pushd hdfs_shell
sudo python3 setup.py install
popd
```

# Usage
Start it and play:
```
$ hdfs_shell
(HDFS) mark@host:/user/mark$ 
(HDFS) mark@host:/user/mark$ ls
Found 1096 items
drwxr-x---   - mark a_group          0 2019-07-05 17:00 /user/mark/.Trash
...
```

Exit with CTRL+C, `logout`, `exit` or `quit`.

HDFS commands are identified.
E.g.: `ls` will actually execute `hdfs dfs -ls`.

You can pipe to Linux commands.
E.g., `cat my_file | wc -l` will `cat` the HDFS file named `my_file`

You can change directory with `cd`. As such, all paths that you enter in the shell are relative to the current working directory (if they not begin with `/`).

To execute a bash command, use the prefix `!`. E.g., `!ls` will list file in your local directory

# Limitations
Commands that interact with the local file system like `put` or `copyToLocal` are not yet supported.
