### VTF-API sample project

#### structure
- JDK 1.8

### features
- ContextListener 사용 예제 
  - Bean에서 ApplicationListener<ContextRefreshedEvent>를
  상속받으면 Spring Context가 모두 loading된 후에 실행된다. 
  - ClassLoader를 보장한 후 정상적으로 기능을 수행하기 위해 사용된다. 
- spring boot 1.3 이후 @EventListener annotation을 통해 동일한 기능을
  구현할 수 있으므로, 반드시 ApplicationListener를 상속받을 필요가 없다. 

  - spring boot 1.2.x 이전  
```
public class CustomContextListener implements
ApplicationListener<ContextRefreshedEvent> {
      @Override
            public void onApplicationEvent(ContextRefreshedEvent event)
            {
              ...
            }
} 
```
  - spring boot 1.3.x 이후 
    - ContextRefreshEvent object를 argument로 받아야 한다. 받지 않으면
    오류 발생. 
```
@Component
@Slf4j
public class CustomByAnnotationContextListener {

      @EventListener
            public void handleContextRefresh(ContextRefreshedEvent
                event) {
              ...
            }
}



```

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
