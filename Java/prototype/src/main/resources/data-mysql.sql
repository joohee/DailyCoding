INSERT INTO `account` (email, joined, password, username)
  SELECT * FROM (SELECT 'neigie@gmail.com', now(), 'password', 'joey') AS tmp
  WHERE NOT EXISTS (SELECT username FROM `account` WHERE username = 'joey');