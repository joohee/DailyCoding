### RedisTemplateExample project

#### features
- Spring-Redis에서 제공하는 StringRedisTemplate 사용 예시. 
  - StringRedisTemplate에서 제공하는 operations 는 아래와 같다. 
```
  ValueOperations - Strings
  BoundValueOperations - String bound to the given key.
  ListOperations - List
  BoundListOperations - List bound to the given key.
  SetOperaions - Set
  BoundSetOperations - Set bound to the given key.
  ZSetOperations - a.k.a Sorted Set
  BoundZSetOperations - Sorted Set bound to the given key.
  HashOperations - Hash
  BoundHashOperations - Hash bound to the given key.
```

#### references
- http://redis.io/
- http://docs.spring.io/spring-data/redis/docs/current/reference/html/

#### structure
- JDK 1.8

#### spring configuration
- spring-boot 적용
- template engine 으로 thymeleaf 적용
```
	compile("org.springframework.boot:spring-boot-starter-web:1.1.9.RELEASE")
	compile("org.springframework.boot:spring-boot-starter-data-jpa")
	compile("org.springframework.boot:spring-boot-starter-test")
	compile('org.springframework.boot:spring-boot-starter-thymeleaf')
```
- 설정파일 : yaml 파일로 작성.
    - classpath:application.yml
        - spring.profiles.active 값에 따라 설정파일을 분리하여 인식함.

#### libraries
- db
	- mysql driver 적용

- log
    - logback

- modelmapper
	- http://modelmapper.org/
	- Object간 매핑을 쉽게 하기 위함.

- lombok
		- setter/getter generator

- test
	- junit
	- FEST
		- https://code.google.com/p/fest/
