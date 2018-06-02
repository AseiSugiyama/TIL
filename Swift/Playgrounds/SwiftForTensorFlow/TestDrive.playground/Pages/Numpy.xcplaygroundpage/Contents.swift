//: [Previous](@previous)
import Python

// import numpy
let np = Python.import("numpy")
//a = np.arange(15).reshape(3, 5)
let a = np.arange.call(with: 15).reshape.call(with: 3, 5)
//b = np.array([6, 7, 8])
let b = np.array.call(with: [6, 7, 8, 9, 10])
// broadcast
a + b

//: [Next](@next)
