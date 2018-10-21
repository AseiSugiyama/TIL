import Foundation

protocol KyotoProtocol{
    func stopWarming()
}

class Japan:KyotoProtocol{
    func stopWarming() {
        print("排気ガス規制します")
    }
}

