//
//  File.swift
//  Application
//
//  Created by Ryuichirou on 2019/04/21.
//

import Foundation
import SwiftKueryORM

public struct ToDo : Codable, Equatable {
    public var id: Int?
    public var user: String?
    public var title: String?
    public var order: Int?
    public var completed: Bool?
    public var url: String?
    
    public static func ==(lhs: ToDo, rhs: ToDo) -> Bool {
        return (lhs.title == rhs.title) && (lhs.user == rhs.user) && (lhs.order == rhs.order) && (lhs.completed == rhs.completed) && (lhs.url == rhs.url) && (lhs.id == rhs.id)
    }
}

extension ToDo : Model {
}
