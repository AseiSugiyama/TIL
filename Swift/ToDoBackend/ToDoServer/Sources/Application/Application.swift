import Dispatch
import Foundation
import Kitura
import KituraOpenAPI
import KituraContracts
import KituraCORS
import LoggerAPI
import Configuration
import CloudEnvironment
import Health

public let projectPath = ConfigurationManager.BasePath.project.path
public let health = Health()

public class App {
    let router = Router()
    let cloudEnv = CloudEnv()
    private var todoStore: [ToDo] = []
    private var nextId: Int = 0
    private let workerQueue = DispatchQueue(label: "worker")

    public init() throws {
        // Run the metrics initializer
        initializeMetrics(router: router)
    }

    func postInit() throws {
        // Endpoints
        initializeHealthRoutes(app: self)
        KituraOpenAPI.addEndpoints(to: router)
        let options = Options(allowedOrigin: .all)
        let cors = CORS(options: options)
        router.all("/*", middleware: cors)
        router.get("/", handler: getAllHandler)
        router.get("/", handler: getOneHandler)
        router.post("/", handler: storeHandler)
        router.delete("/", handler: deleteAllHandler)
        router.delete("/", handler: deleteOneHandler)
        router.patch("/", handler: updateHandler)
    }
    
    func getAllHandler(completion: ([ToDo]?, RequestError?) -> Void ) {
        completion(todoStore, nil)
    }
    
    func getOneHandler(id: Int, completion: (ToDo?, RequestError?) -> Void ) {
        guard let todo = todoStore.first(where: { $0.id == id }) else {
            return completion(nil, .notFound)
        }
        completion(todo, nil)
    }
    
    func storeHandler(todo: ToDo, completion: (ToDo?, RequestError?) -> Void ) {
        var todo = todo
        if todo.completed == nil {
            todo.completed = false
        }
        todo.id = nextId
        todo.url = "http://localhost:8080/\(nextId)"
        nextId += 1
        execute {
            todoStore.append(todo)
        }
        completion(todo, nil)
    }
    
    func deleteAllHandler(completion: (RequestError?) -> Void ) {
        execute {
            todoStore = []
        }
        completion(nil)
    }
    
    func deleteOneHandler(id: Int, completion: (RequestError?) -> Void ) {
        guard let index = todoStore.index(where: { $0.id == id }) else {
            return completion(.notFound)
        }
        execute {
            todoStore.remove(at: index)
        }
        completion(nil)
    }
    
    func updateHandler(id: Int, new: ToDo, completion: (ToDo?, RequestError?) -> Void ) {
        guard let index = todoStore.index(where: { $0.id == id }) else {
            return completion(nil, .notFound)
        }
        var current = todoStore[index]
        current.user = new.user ?? current.user
        current.order = new.order ?? current.order
        current.title = new.title ?? current.title
        current.completed = new.completed ?? current.completed
        execute {
            todoStore[index] = current
        }
        completion(current, nil)
    }

    public func run() throws {
        try postInit()
        Kitura.addHTTPServer(onPort: cloudEnv.port, with: router)
        Kitura.run()
    }
    
    func execute(_ block: (() -> Void)) {
        workerQueue.sync {
            block()
        }
    }
}
