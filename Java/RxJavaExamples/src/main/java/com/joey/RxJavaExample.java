package com.joey;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import rx.Observable;

/**
 * Created by joey on 2016. 6. 20..
 */
public class RxJavaExample {

	private static Logger logger = LoggerFactory.getLogger(RxJavaExample.class);

	public static void main(String[] args) {
		hello("A", "B", "C");
	}

	public static void hello(String ...names) {
		Observable.from(names).subscribe(s -> {
			logger.info("Hello: " + s);
		});
	}
}
