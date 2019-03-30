//
//  ViewController.swift
//  TestStoryboardPlayground
//
//  Created by Ryuichirouon 2018/12/15.
//  Copyright © 2018 gokennya. All rights reserved.
//

import UIKit

public class ViewController: UIViewController {

    @IBOutlet public weak var mainLabel: UILabel!
    
    public override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        mainLabel.text = "Hello, world"
    }

}

