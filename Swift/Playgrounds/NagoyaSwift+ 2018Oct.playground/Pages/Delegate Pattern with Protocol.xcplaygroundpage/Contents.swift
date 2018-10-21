protocol VendorDelegate {
    func didEndBuilt(with vendor:Vendor)
}

class Vendor{
    var delegate:VendorDelegate?
    func build(){
        print("Vendor「ビルドしたよ。完璧！」")
        delegate?.didEndBuilt(with: self)
    }
}

class Engineer:VendorDelegate{
    func order(with vendor:Vendor){
        vendor.delegate = self
        vendor.build()
        print("Engineer「ベンダーにビルドしてもらったよ」")
    }
    func didEndBuilt(with vendor:Vendor){
        print("Engineer「検収したよ。完璧！」")
        vendor.delegate = nil
    }
}

class Manager:VendorDelegate{
    func order(with vendor:Vendor){
        vendor.delegate = self
        vendor.build()
        print("Manager「ベンダーにビルドしてもらったよ。」")
    }
    func didEndBuilt(with vendor: Vendor) {
        print("Manager「検収したよ。」")
        vendor.delegate = nil
    }
}

let vendor = Vendor()
let engineer = Engineer()
engineer.order(with: vendor)

let myManager = Manager()
myManager.order(with: vendor)
