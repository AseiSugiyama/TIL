let x = 1
let y = 2
let z = x + y


import UIKit
import ImportPlaygroundFramework
import PlaygroundSupport

let mainView = UIStoryboard(
        name: "Main",
        bundle: Bundle(for: ViewController.self)
        )
        .instantiateInitialViewController() as! ViewController

PlaygroundPage.current.liveView = mainView

mainView.mainLabel.text = "Hello, Playground"
