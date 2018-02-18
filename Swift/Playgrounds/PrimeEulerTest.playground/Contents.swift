//: Playground - noun: a place where people can play

import UIKit

/**
 * WIP: exponential function
 * FIXME: EXC_BAD_INSTRUCTION (code=EXC_I386_INVOP, subcode=0x0)
 */
func power(x:Int, y:Int) -> Int{
    if y == 0 {
        return 1
    }else if y == 1{
        return x
    }else if y % 2 == 0 {
        let tmp = power(x: x, y: y / 2)
        return tmp * tmp
    }else {
        let tmp = power(x: x, y: (y-1) / 2)
        return x * tmp * tmp
    }
}

/**
 * WIP: exponential function in Z_n
 * FIXME: EXC_BAD_INSTRUCTION (code=EXC_I386_INVOP, subcode=0x0)
 */
func power(x:Int, y:Int, mod: Int) -> Int{
    if y == 0 {
        return 1 % mod
    }else if y == 1{
        return x % mod
    }else if y % 2 == 0 {
        let tmp = power(x: x, y: y / 2) % mod
        return (tmp * tmp) % mod
    }else {
        let tmp = power(x: x, y: (y-1) / 2) % mod
        return (x * tmp * tmp) % mod
    }
}

power(x: 2, y: 3)

/**
 * GCD function
 */
func greatestCommonDivisor(m:Int, n:Int) -> Int{
    if m <= n {
        return greatestCommonDivisor(m: n, n: m)
    }else if n == 0{
        return m
    }else{
        let r = m % n
        return greatestCommonDivisor(m: n, n: r)
    }
}

greatestCommonDivisor(m: 10, n: 3)

/**
 * Euler test : see https://en.wikipedia.org/wiki/Euler%27s_criterion
 */
func eulerTest(number:Int) -> Bool{
    if number == 1 {
        return false;
    }else if number == 2{
        return true
    }else if number % 2 == 0 {
        return false
    }else{
        for i in 2..<number{
            if(greatestCommonDivisor(m: i, n: number) != 1){
                return false
            }
            if (power(x: i, y: number - 1) % number != 1){
                return false
            }
        }
        return true
    }
}

eulerTest(number: 1023)

