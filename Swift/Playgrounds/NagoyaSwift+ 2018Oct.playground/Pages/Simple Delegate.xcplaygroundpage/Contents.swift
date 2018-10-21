import Foundation

class Layer{
    func defend(){
        print("異議あり！")
    }
}

class Defendant{
    var delegate : Layer?
    func defend(){
        if let delegate = self.delegate {
            delegate.defend()
        }else{
            print("たすけてください")
        }
    }
}

var defendant = Defendant()
defendant.delegate = Layer()
defendant.defend()
