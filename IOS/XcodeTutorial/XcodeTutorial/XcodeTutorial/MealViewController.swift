//
//  MealViewController.swift
//  XcodeTutorial
//
//  Created by Joohee Kang on 2016. 2. 19..
//  Copyright © 2016년 Joohee Kang. All rights reserved.
//

import UIKit

class MealViewController: UIViewController, UITextFieldDelegate, UIImagePickerControllerDelegate, UINavigationControllerDelegate {

    // MARK: Properties
    @IBOutlet weak var nameTextField: UITextField!
    @IBOutlet weak var photoImageView: UIImageView!
    @IBOutlet weak var ratingControl: RatingControl!
    @IBOutlet weak var saveButton: UIBarButtonItem!
    
    var meal = Meal?()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        nameTextField.delegate = self
        if let meal = meal {
            navigationItem.title = meal.name
            nameTextField.text = meal.name
            photoImageView.image = meal.photo
            ratingControl.rating = meal.rating
        }
        checkValidMealName()
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    // MARK: UITextFieldDelegate
    func textFieldShouldBeginEditing(textField: UITextField) -> Bool {
        saveButton.enabled = false
        return true
    }
    
    func textFieldShouldReturn(textField: UITextField) -> Bool {
        // hide the keyboard
        textField.resignFirstResponder()
        return true
    }
    
    func textFieldDidEndEditing(textField: UITextField) {
        checkValidMealName()
        navigationItem.title = textField.text
    }
    
    func checkValidMealName() {
        let text = nameTextField.text ?? ""
        saveButton.enabled = !text.isEmpty
    }
    
    // MARK: UIImagePickerControllerDelegate
    func imagePickerControllerDidCancel(picker: UIImagePickerController) {
        // dismiss the picker if the user cancelled.
        dismissViewControllerAnimated(true, completion: nil)
    }
    
    func imagePickerController(picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [String : AnyObject]) {
        // This info dictionary contains multiple representations of the image, and this uses the original.
        let selectedImage = info[UIImagePickerControllerOriginalImage] as! UIImage
        
        // set photoImage to display the seleted image. 
        photoImageView.image = selectedImage
        
        // dismiss the picker
        dismissViewControllerAnimated(true, completion: nil)
        
    }
    
    // MARK: Navigations
    
    @IBAction func cancel(sender: UIBarButtonItem) {
        // true면 + 버튼을 통해 들어온거고, false 면 tableCell을 클릭해서 들어왔다는 의미.
        let isPresentingInAddingMealMode = presentingViewController is UINavigationController
        if isPresentingInAddingMealMode {
            dismissViewControllerAnimated(true, completion: nil)
        } else {
            navigationController!.popToRootViewControllerAnimated(true)
        }
    }
    
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        if saveButton === sender {
            let name = nameTextField.text ?? ""
            let photo = photoImageView.image
            let rating = ratingControl.rating
            
            meal = Meal(name: name, photo: photo, rating: rating)
        }
    }
    
    // MARK: Actions
    
    @IBAction func selectImageFromPhotoLibrary(sender: UITapGestureRecognizer) {
        // Hide the keyboard.
        nameTextField.resignFirstResponder()
        
        // UIImagePickerController is a view controller that lets a user pick media from their photo library.
        let imagePickerController = UIImagePickerController()
        
        // Only allow photos to be picked, not taken
        imagePickerController.sourceType = .PhotoLibrary
        
        // Make sure ViewController is notified when the user picks the image. 
        imagePickerController.delegate = self
        
        // ViewController내부에서 호출되는 메서드.
        presentViewController(imagePickerController, animated: true, completion: nil)
        
    }

    
}

