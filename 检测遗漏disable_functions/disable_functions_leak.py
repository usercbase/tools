import sys
need_check=""
if(len(sys.argv)==1):
	print("please input command:\n					python xxx.py system,exec....\n				such as:\n					python 1.py pcntl_alarm,pcntl_fork,pcntl_waitpid,pcntl_wait")
	sys.exit(0)
need_check=sys.argv[1]
if(sys.argv[1]=="-h" or sys.argv[1]=="--h" or sys.argv[1]==""):
	print("please input command:\n					python xxx.py system,exec....\n				such as:\n					python 1.py pcntl_alarm,pcntl_fork,pcntl_waitpid,pcntl_wait")
	sys.exit(0)


all_command="pcntl_alarm,pcntl_fork,pcntl_waitpid,pcntl_wait,pcntl_wifexited,pcntl_wifstopped,pcntl_wifsignaled,pcntl_wifcontinued,pcntl_wexitstatus,pcntl_wtermsig,pcntl_wstopsig,pcntl_signal,pcntl_signal_get_handler,pcntl_signal_dispatch,pcntl_get_last_error,pcntl_strerror,pcntl_sigprocmask,pcntl_sigwaitinfo,pcntl_sigtimedwait,pcntl_exec,pcntl_getpriority,pcntl_setpriority,pcntl_async_signals,system,exec,shell_exec,popen,proc_open,passthru,symlink,link,syslog,imap_open,ld,dl".split(',')
str_tmp=need_check.replace("()","").split(',')
for i in range(len(str_tmp)):
	if(str_tmp[i]!=""):
		for j in range(len(all_command)):
			if(all_command[j]==str_tmp[i]):
				del(all_command[j])
				break
if(len(all_command)==0):
	print("All command execution functions are disabled")
else:
	print("The following " + str(len(all_command)) + " commands are not baned:")
	for j in range(len(all_command)):
		print("        "+all_command[j])
