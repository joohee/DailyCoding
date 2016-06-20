## RxJava Examples

- Usage of RxJava (by Netflix)

### Example
```
    public static void main(String[] args) {
        hello("A", "B", "C");
    }

    public static void hello(String ...names) {
        Observable.from(names).subscribe(s -> {
            logger.info("Hello: " + s);
        });
    }

```

### Result
```
17:25:58.650 [main] INFO  com.joey.RxJavaExample - Hello: A
17:25:58.654 [main] INFO  com.joey.RxJavaExample - Hello: B
17:25:58.654 [main] INFO  com.joey.RxJavaExample - Hello: C

```
