dbname = 'db.sqlite3'
dbpath = 'D:\\python\\graduation\\gratuation_design'
csvpath = pspath

# custom thread number
tnum = 20
hvsrvs_all = hvsrvs.objects.all()
serverips = []
# ls = []
for hvsrv in hvsrvs_all:
    Phy_ServerIP = hvsrv.serverip
    serverips.append(Phy_ServerIP)

for ips in lstg(tnum, serverips):
    threads = []

    for Phy_ServerIP in ips:
        # print Phy_ServerIP
        t = threading.Thread(target=GetVMs, args=(PS_GetVMs, Phy_ServerIP))
        t.setDaemon(True)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

sql_insert = '''insert into sinfors_hvvms values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
conn = sqlite3.connect(dbpath)
cu = conn.cursor()
datas = []
i = 1
for csvf in os.listdir(csvpath):
    if os.path.splitext(csvf)[0].startswith('queryresult-') and os.path.splitext(csvf)[1] == '.csv':
        csvfile = os.path.join(csvpath, csvf)
        # print csvfile
        cf = open(csvfile)
        cf.readline()

        for l in csv.reader(cf):
            l.insert(0, i)
            i = i + 1
            datas.append(tuple(l))
        cf.close()
        # print csvfile
        os.remove(csvfile)
# print datas
if len(datas) > 0:
    cu.execute('delete from sinfors_hvvms')
    conn.commit()
    for data in datas:
        cu.execute(sql_insert, data)

    conn.commit()
    cu.execute('select * from sinfors_hvvms')
    cu.close()