import paramiko
ip = input("ENTER IP: ")
user = input("ENTER USERNAME: ")
passwd = input("ENTER PASSWORD: ")

client = paramiko.SSHClient()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(ip,username=user,password=passwd)

remote_connection = client.invoke_shell()

stdin, stdout, stderr = client.exec_command('wall Hello_world > /dev/null 2>&1')
out = stdout.readlines()
error = stderr.readlines()
print(out)
print(error)




