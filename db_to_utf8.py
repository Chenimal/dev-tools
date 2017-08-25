#coding=utf-8

#change all maria db to utf8

from colorama import Fore
import MySQLdb
import time
import re
import yaml

env = "prod"
city = 'tw'
# load config file
o = yaml.load(open("/Users/chen/lalamove/data/db.yml"))

db_config = o[env]['mobile'][city]

allowed_collations = ['utf8_unicode_ci', 'utf8_general_ci']
ignored_field_types = ['int', 'decimal', 'datetime', 'date', 'tinyint', 'smallint', 'float', 'timestamp', 'polygon', 'geometry']

#connect db
conn=MySQLdb.connect(host=db_config['host'], user=db_config['user'], passwd=db_config['passwd'], db=db_config['db'])
cur = conn.cursor(MySQLdb.cursors.DictCursor)

# get all tables' names
def getAllTables():
    result = []
    cnt = cur.execute("SHOW TABLE STATUS FROM `" + db_config['db'] + "`")
    print("# of tables: " + str(cnt))
    tables =  cur.fetchmany(cnt)
    for i in tables:
        result.append((i['Name'], i['Rows'], i['Collation']))
    return result

def getLatinTables(all_tables):
    result = []
    for i in all_tables:
        if i[2] not in allowed_collations:
            result.append((i[0], i[1]))
    print("# of non-utf8 tables: ", len(result))
    return result

#change table one by one
def toUtf8(tables):
    #default db charset(for new tables):
    cur.execute("ALTER DATABASE `" + db_config['db'] + "` DEFAULT CHARACTER SET utf8")
    i=0
    for table_name in tables:
        i+=1
        print(Fore.WHITE + str(i) + " | " + table_name[0].ljust(50) + " | " + str(table_name[1]).ljust(10), end='| ')
        t1=time.time();
        # default table charset(for new fields)
        cur.execute("ALTER TABLE `" + table_name[0] + "` CHARSET=utf8;")
        has_warning = cur.execute("SHOW WARNINGS")
        if has_warning > 0:
            warnings = cur.fetchmany(has_warning)
            for w in warnings:
                print(Fore.YELLOW + "warning:"+ w)
        # existing fields(existed columns)
        cur.execute("ALTER TABLE `" + table_name[0] + "` CONVERT TO CHARACTER SET utf8")
        has_warning = cur.execute("SHOW WARNINGS")
        if has_warning > 0:
            warnings = cur.fetchmany(has_warning)
            for w in warnings:
                print(Fore.YELLOW + "warning:"+ w)
        t2=time.time()
        print("cost: " + str(t2-t1))

def checkFieldASCII(tables):
    j=0
    for i in tables:
        r = cur.execute("DESCRIBE `"+ i[0] + "`")
        rows = cur.fetchmany(r)
        print (Fore.GREEN+"Table:",i[0])
        for row in rows:
            skip = False
            for ignore_type in ignored_field_types:
                found = row['Type'].find(ignore_type)
                if found>=0:
                    skip =True
                    break
            if not skip:
                j+=1
                print(Fore.YELLOW, j, row['Type'],row['Field'])
                vc = cur.execute("SELECT DISTINCT `" + row['Field'] + "` FROM " + i[0])
                values = cur.fetchmany(vc)
                for v in values:
                    if v[row['Field']] is None:
                        continue
                    is_ascii = all(ord(c) < 128 for c in v[row['Field']])
                    if not is_ascii:
                        print(Fore.RED, v[row['Field']], row['Field'], i[0])
                        exit()

def checkAnyLatinFieldsInUtf8Tables(all_tables):
    tables=[]
    for table in all_tables:
        cur.execute("SHOW CREATE TABLE `"+table[0]+"`")
        res = cur.fetchone()
        if res['Create Table'].find("latin") >=0:
            tables.append(table[0])
            lines = res['Create Table'].split("\n")
            for line in lines:
                if line.find("latin")>=0:
                    field = re.search("`.*`", line).group()
                    rc = cur.execute("SELECT DISTINCT "+field+" FROM `"+table[0]+"`")
                    values = cur.fetchmany(rc)
                    for v in values:
                        vv = v[field.strip('`')]
                        if vv is None:
                            continue
                        is_ascii = all(ord(c) < 128 for c in vv)
                        if not is_ascii:
                            print(Fore.RED, vv, field, table[0])
                            exit()
    print("Has", len(tables), "more tables to modify")
    for table in tables:
        print(table, end='| ')
        t1=time.time();
        # existing fields(existed columns)
        cur.execute("ALTER TABLE `" + table + "` CONVERT TO CHARACTER SET utf8")
        has_warning = cur.execute("SHOW WARNINGS")
        if has_warning > 0:
            warnings = cur.fetchmany(has_warning)
            for w in warnings:
                print(Fore.YELLOW + "warning:"+ w)
        t2=time.time()
        print("cost: " + str(t2-t1))


#execution
print(Fore.BLUE+"BEFORE change:")
all_tables = getAllTables()
tables_to_be_changed= getLatinTables(all_tables)

checkFieldASCII(tables_to_be_changed)

time_start=time.time();
toUtf8(tables_to_be_changed)
time_end=time.time();

print(Fore.GREEN+"AFTER change:")
all_tables = getAllTables()
getLatinTables(all_tables)

print(Fore.WHITE + "Time cost: " + str(time_end-time_start))

print(Fore.YELLOW + "Final check:")
checkAnyLatinFieldsInUtf8Tables(all_tables)
#close connection
cur.close()
conn.close()
print(Fore.GREEN + "You are done. Get some sleep")
