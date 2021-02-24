import os

groupName = input('Enter group name: ')

os.system(f'sudo groupadd {groupName}')

newUser = input('Enter new users username: ')

os.system(f'sudo useradd -m {newUser}')
os.system(f'sudo passwd {newUser}')
os.system(f'sudo chage -d 0 {newUser}') 

os.system(f'sudo usermod -aG {groupName} {newUser}')