
f = open('exclude.txt', 'r')
lines = f.readlines()
f.close()

f_out = open('exclude_gt4.txt', 'w')
for line in lines:
    if len(line.strip().decode('utf-8'))>4:
        f_out.write(line)
f_out.close()
