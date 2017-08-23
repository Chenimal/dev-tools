1. Change default charset for DB (For new tables)
  - All cities db now are latin1
  - ```SELECT schema_name,default_character_set_name FROM information_schema.SCHEMATA;```
  - ```ALTER DATABASE db_name DEFAULT CHARACTER SET utf8;```

2. Change default charset for tables (For new fields in existing tables)
  - Around 40 latin1 tables, TW has 80
  - ```ALTER TABLE tb_name CHARSET=UTF8;```

3. Change charset for existing fields (For existing fields in existing tables)
  - ```ALTER TABLE tb_name CONVERT TO CHARACTER SET utf8;```
  - For those latin1 tables:
    * Check if any special characters?(ASCII should be safe to just use ALTER TABLE):
      - tw: tw_vanlookuplocality_polygon.polygon_ref
      - hk: vanorder_remark.remark_desc
      - th: no on snapshot
    * Affect type geometry, polygon?
  - For those utf8 tables:
    * Checked each db has 8-10 utf8 tables has latin1 fields
    * Checked all are ASCII chars

Test:
  - On sandbox(Kappi)
  - On staging(ask Simon)
  - Speed
    * 10 seconds in test& dev)
    * 27 seconds in snapshot(th)

Script:
https://git.easygroup.co/chenimal.sun/scripts/blob/master/db_to_utf8.py
