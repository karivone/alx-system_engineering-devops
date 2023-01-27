Processes and Signals
Each file in this repository holds code that illustrates an essential concept of system engineering and devOps pertaining to processes and signals: ps, pgrep, kill, pkill, SIGINT (Ctrl-C), SIGTERM(kill), SIGQUIT(Ctrl-|)

Description of what each file shows:
Files that start with:
display bash script's pid
list processes
display pid's related to bash using ps
display pid's related to bash using pgrep
create infinite loop with sleep 2 that Ctrl-C can kill
script to kill file 4 in different terminal
script to pkill file 4 in different terminal
upgrade file 4 to catch Ctrl-C SIGINT and display message instead .67 script to kill file 7 in different terminal and gets caught
script to pkill file 7 successfully
infinite loop that can be killed with Ctrl-C
infinite loop with multiple signal catches and ultimately exits
creates 5 zombie processes
Environment
Language: Bash scripts
OS: Ubuntu 14.04 LTS
Executable: chmod +x [filename]; run with ./[filename]
Style guidelines: Shellcheck
Authors
Karivone