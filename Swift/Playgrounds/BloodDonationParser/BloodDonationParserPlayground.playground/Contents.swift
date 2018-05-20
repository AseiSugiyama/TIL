//: Playground - noun: a place where people can play
import UIKit
import SwiftSoup
import PlaygroundSupport

// for HTTP(S)
PlaygroundPage.current.needsIndefiniteExecution = true

class Client{
    func getJson(){
        let url = URL(string: "http://date.jsontest.com/")!
        let task = URLSession.shared.dataTask(with: url) {data, response, error in
            if let jsonData = data {
                self.printJson(jsonData)
            }
        }
        task.resume()
    }
    
    func getHtml(from fqdn:String){
        let url = URL(string: fqdn)!
        let task = URLSession.shared.dataTask(with: url) {data, response, error in
            print("hello")
            if let htmlData = data {
                let html = String(data:htmlData, encoding:String.Encoding.utf8)!
                self.parseHtml(html)
            }
        }
        task.resume()
    }

    func printJson(_ data: Data) {
        do{
            let json = try JSONSerialization.jsonObject(with: data, options: .allowFragments)
            print(json)
        } catch {
            print("parse error!")
        }
    }
    
    func parseHtml(_ html:String){
        // SwiftSoup
        do {
            let doc: Document = try SwiftSoup.parse(html)
            try print(doc.text())
            PlaygroundPage.current.finishExecution()
        } catch Exception.Error(let _, let message) {
            print(message)
        } catch {
            print("error")
        }
    }
}

let client = Client()
client.getJson()
client.getHtml(from:"https://example.com/")
