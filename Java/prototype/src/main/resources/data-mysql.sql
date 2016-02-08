INSERT INTO `account` (email, joined, password, username)
  SELECT * FROM (SELECT 'aaa@bbb.com', now(), 'password', 'aaa') AS tmp
  WHERE NOT EXISTS (SELECT username FROM `account` WHERE username = 'aaa');