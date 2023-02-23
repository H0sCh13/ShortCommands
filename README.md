# ShortCommands
Basic Python Script, which lets the User run a selection of useful Powershell and Cmdline Commands directly from the Terminal.

The implemented Commands are as follows:

Powershell Commands:

- IP on network (Powershell -c get-netneighbor)
- list process (Powershell -c get-process)
- kill process (Powershell -c stop-process -name:[PROCESS]

Cmdline Commands:

- list process (tasklist)
- kill process (tasklist /F /PID [PROCESS])
- clear terminal (cls)

Docstrings:

- help [Keyword] (help function on all keywords with additional Information about the chosen Command)

While killing processes it is also possible to kill a certain process without having to type in the file extension in Powershell, since it is already implemented in the code, although the path needs to be configured beforehand to function properly.
