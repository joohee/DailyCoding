//
//  XcodeTutorialTests.swift
//  XcodeTutorialTests
//
//  Created by Joohee Kang on 2016. 2. 19..
//  Copyright © 2016년 Joohee Kang. All rights reserved.
//

import XCTest
@testable import XcodeTutorial

class XcodeTutorialTests: XCTestCase {
    
    // MARK: FoodTracker Tests
    func testMealInitialization() {
        // success case
        let potentialItem = Meal(name: "Newest Meal", photo: nil, rating: 5)
        XCTAssertNotNil(potentialItem)
        
        // failure case
        let noName = Meal(name: "", photo: nil, rating: 0)
        XCTAssertNil(noName, "Empty name is invalid")
        
        let badRating = Meal(name: "Really bad rating", photo: nil, rating: -1)
        XCTAssertNil(badRating, "Negative ratings is invalid, be positive")
        
    }
}
