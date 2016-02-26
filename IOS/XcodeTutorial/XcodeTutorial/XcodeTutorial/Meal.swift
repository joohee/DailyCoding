//
//  Meal.swift
//  XcodeTutorial
//
//  Created by Joohee Kang on 2016. 2. 24..
//  Copyright © 2016년 Joohee Kang. All rights reserved.
//

import UIKit

class Meal {
    // MARK: Properties
    var name:String
    var photo:UIImage?
    var rating:Int
    
    // MARK: Initialization
    init?(name: String, photo: UIImage?, rating: Int) {
        self.name = name
        self.photo = photo
        self.rating = rating
        
        if (name.isEmpty || rating < 0) {
            return nil
        }
    }
    
    
    
    
    
}
