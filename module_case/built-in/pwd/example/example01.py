import pwd

# pwd.getpwuid(uid)：返回对应uid的示例信息
print(pwd.getpwuid(0))

# pwd.getpwnam(name)：返回对应name的用户信息
print(pwd.getpwnam('root'))


