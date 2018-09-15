//
//  ViewController.swift
//  TestAlertView
//
//  Created by Ryuichirou on 2018/09/15.
//  Copyright © 2018年 gokennya. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }
    
    @IBAction func didPushedAlertButton(_ sender: Any) {
        let alert: UIAlertController = UIAlertController(title: "Alert title", message: "Alert message", preferredStyle:  UIAlertControllerStyle.alert)
        
        let defaultAction: UIAlertAction = UIAlertAction(title: "OK", style: UIAlertActionStyle.default, handler:nil)

        alert.addAction(defaultAction)
        
        present(alert, animated: true, completion: nil)
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

