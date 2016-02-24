import UIKit

class RatingControl: UIView {
    
    // MARK: Properties
    // property observer 속성을 갖도록 한다.
    var rating = 0 {
        didSet {
            setNeedsLayout()
        }
    }
    
    var ratingButtons = [UIButton]()
    var spacing = 5
    var stars = 5
    
    // MARK: Initialization 
    
    required init?(coder aDecoder: NSCoder) {
        super.init(coder: aDecoder)
        
        let filledStartImage = UIImage(named: "filledStar")
        let emptyStarImage = UIImage(named: "emptyStar")
        
        for _ in 0..<stars {
            let button = UIButton()
            button.setImage(emptyStarImage, forState: .Normal)
            button.setImage(filledStartImage, forState: .Selected)
            button.setImage(filledStartImage, forState: [.Highlighted, .Selected])
            button.adjustsImageWhenDisabled = false     // 버튼 상태 변경시의 별도의 하이라이트 효과가 나타나는 것을 막아줌.
            button.addTarget(self, action: "ratingButtonTapped:", forControlEvents: .TouchDown)
            ratingButtons += [button]
            addSubview(button)
        }
        
    }
    
    override func layoutSubviews() {
        let buttonSize = Int(frame.size.height)
        
        var buttonFrame = CGRect(x: 0, y: 0, width: buttonSize, height: buttonSize)
        
        for (index, button) in ratingButtons.enumerate() {
            buttonFrame.origin.x = CGFloat(index * (buttonSize + spacing))
            button.frame = buttonFrame
        }
        
        updateButtonSelectionStates()
        
    }

    override func intrinsicContentSize() -> CGSize {
        return CGSize(width: 240, height: 44)
    }
    
    // MARK: Button Action
    func ratingButtonTapped(button: UIButton) {
        
        // rating은 1~5의 값을 갖는다.
        rating = ratingButtons.indexOf(button)! + 1
        updateButtonSelectionStates()
        
    }
    
    func updateButtonSelectionStates() {
        // rating 보다 작은 애들이 선택된 애들이다.
        for (index, button) in ratingButtons.enumerate() {
            button.selected = index < rating
        }
    }
    
}
