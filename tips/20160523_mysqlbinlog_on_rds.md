### mysqlbinlog

#### reference
- https://docs.aws.amazon.com/ko_kr/AmazonRDS/latest/UserGuide/USER_LogAccess.Concepts.MySQL.html 

#### example 
- mysqlbinlog -h yourhost.ds.amazonaws.com -u user -p --read-from-remote-server -t [mysql logfile]

### mysql logfile
- SHOW BINARY LOGS;
- SHOW MASTER STATUS;
