import Foundation
import PlaygroundSupport
PlaygroundPage.current.needsIndefiniteExecution = true

// Github API を使う
// curl -i https://api.github.com/users/ryuichirou
// 結果をjsonで得る
let urlString = "https://api.github.com/users/ryuichirou"
let url = URL(string: urlString)!

// 1. Create a session configuration.
let configuration = URLSessionConfiguration.default

// 2. Create a session, specifying a configuration object and, optionally, a delegate.
var session = URLSession(configuration: configuration)

// 3. Create task objects within a session that each represent a resource request.
var task = session.dataTask(with: url) { (data, response, error) in
    // header
    if let response = response {
        print(response)
    }
    
    if let data = data {
        do {
            let object = try JSONSerialization.jsonObject(with: data, options: [])
            print(object)
        } catch let e{
            print(e)
        }
    }
    PlaygroundPage.current.finishExecution()
}
task.resume()
