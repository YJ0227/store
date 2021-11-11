f = open(file="baidu_x_system.log", mode="r+", encoding="utf-8")
data = f.readlines()

all_ip = []
ip_count = {}
for i in data:
    ip = i.split(" ", 1)
    all_ip.append(ip[0])

for i in all_ip:
    if i in ip_count:
        ip_count[i] += 1
    else:
        ip_count[i] = 1

print(ip_count)

