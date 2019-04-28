// swift-tools-version:4.0
import PackageDescription

let package = Package(
    name: "ToDoServer",
    dependencies: [
      .package(url: "https://github.com/IBM-Swift/Kitura.git", .upToNextMinor(from: "2.7.0")),
      .package(url: "https://github.com/IBM-Swift/HeliumLogger.git", from: "1.7.1"),
      .package(url: "https://github.com/IBM-Swift/CloudEnvironment.git", from: "9.0.0"),
      .package(url: "https://github.com/RuntimeTools/SwiftMetrics.git", from: "2.0.0"),
      .package(url: "https://github.com/IBM-Swift/Health.git", from: "1.0.0"),
      .package(url: "https://github.com/IBM-Swift/Kitura-OpenAPI.git", from: "1.0.0"),
      .package(url: "https://github.com/IBM-Swift/Kitura-CORS.git", from: "2.1.0"),
      .package(url: "https://github.com/IBM-Swift/Swift-Kuery-ORM", from: "0.4.1"),
      .package(url: "https://github.com/IBM-Swift/Swift-Kuery-PostgreSQL", from: "2.1.0"),
    ],
    targets: [
      .target(name: "Application", dependencies: ["SwiftKueryPostgreSQL", "SwiftKueryORM", "KituraCORS", "KituraOpenAPI", "Kitura", "CloudEnvironment","SwiftMetrics","Health",]),
      .target(name: "ToDoServer", dependencies: [ .target(name: "Application"), "Kitura" , "HeliumLogger"]),
      .testTarget(name: "ApplicationTests" , dependencies: [.target(name: "Application"), "Kitura","HeliumLogger" ])
    ]
)
