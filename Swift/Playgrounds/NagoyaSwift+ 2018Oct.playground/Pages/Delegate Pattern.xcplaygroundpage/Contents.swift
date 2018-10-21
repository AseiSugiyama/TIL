class Lawyer{
    func decide(){
        let library = Library()
        //デリゲート先でデリゲート元のメソッドが実行できるようにするために、デリゲート先のプロパティにデリゲート元のインスタンスを代入する。
        library.delegate = self
        //デリゲート先のメソッドを実行する。
        library.search()
    }
    //libraryから（完了）通知を受け取るためのメソッド
    func didEndSearch(with library:Library){
        print("弁護士「調査が完了しました。」")
        // デリゲート先のインスタンスを消去する（大事！）
        library.delegate = nil
    }
}

class Library{
    var delegate:Lawyer?
    func search(){
        print("ライブラリ「判例を探しました。」")
        self.delegate?.didEndSearch(with:self)
    }
}

var lawyer = Lawyer()
lawyer.decide()
