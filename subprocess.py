import subprocess
command = "df -h"
proc = subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)
(out, err) = proc.communicate()
outwithoutreturn = out.rstrip('\n')
print out 




#./myfile.ext


print outwithoutreturn
./mifile.ext
