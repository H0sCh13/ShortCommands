# ShortCommands
Basic Python Script, which lets the user run a selection of useful Powershell and Cmdline commands directly from the Terminal.

The implemented commands are as follows:

Powershell Commands:

- IP on network (Powershell -c get-netneighbor)
- list process (Powershell -c get-process)
- kill process (Powershell -c stop-process -name:[PROCESS]

Cmdline Commands:

- list process (tasklist)
- kill process (tasklist /F /PID [PROCESS])

While killing processes it is also possible to kill a certain process without having to type in the file extension in Powershell, since it is already implemented in the code.

