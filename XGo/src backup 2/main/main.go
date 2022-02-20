package main

import (
  "fmt"
  "error"
  "poker"
)

func main() {
  defer func() {
    err, ok := recover().(error.Error)

    if ok {
      fmt.Println(err.Message())
    }
  }()

  fmt.Println(poker.NewHand("Th Jh Qh Kh Ah"), "\n") // Royal Flush
  fmt.Println(poker.NewHand("Ts Js Qs 9s 8s"), "\n") // Straight Flush
  fmt.Println(poker.NewHand("Ts Tc Td 9s Th"), "\n") // Four of a kind
  fmt.Println(poker.NewHand("5s 8h 5c 8s 5d"), "\n") // Full House
  fmt.Println(poker.NewHand("Kd 8d 4d Td 2d"), "\n") // Flush
  fmt.Println(poker.NewHand("5s 8h 4c 6s 7d"), "\n") // Straight
  fmt.Println(poker.NewHand("5s 7h 4c 7s 7d"), "\n") // Three of a kind
  fmt.Println(poker.NewHand("5s 6h 4c 6s 5d"), "\n") // Two Pairs
  fmt.Println(poker.NewHand("5s 7h 4c 7s 8d"), "\n") // One Pair
  fmt.Print(poker.NewHand("2s 7h 4c Ts Qd"))         // Nothing
}