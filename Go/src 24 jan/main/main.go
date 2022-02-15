package main

import "fmt"
import "hand"
//import "error"
import "result"

func main() {
  /*defer func() {
    err, ok := recover().(error.Error)

    if ok {
      fmt.Println(err.Message())
    }
  }()*/

  { hand1 := hand.NewHand("TH JH 9H 7H 8H") // Straigh flush, Jack highest
    hand2 := hand.NewHand("TS JS QS 9S 8S") // straigh flush, Queen highest
    PrintResult(hand1.CompareWith(hand2))
    PrintResult(hand2.CompareWith(hand1))
  }
  
  /*{ hand1 := hand.NewHand("TH JH QH KH 8H") // 
    hand2 := hand.NewHand("TS JS QS KS 7S")
    fmt.Println(hand1)
    fmt.Println(hand2)
    PrintResult(hand1.CompareWith(hand2))
    PrintResult(hand2.CompareWith(hand1))
  }

  { hand1 := hand.NewHand("5S 5H TC TD 8H")
    hand2 := hand.NewHand("5C 5D TH TS 8D")
    fmt.Println(hand1)
    fmt.Println(hand2)
    PrintResult(hand1.CompareWith(hand2))
    PrintResult(hand2.CompareWith(hand1))
  }

  { hand1 := hand.NewHand("5S 5H TC TD 8H")
    hand2 := hand.NewHand("5C 5D TH TS 7D")
    fmt.Println(hand1)
    fmt.Println(hand2)
    PrintResult(hand1.CompareWith(hand2))
    PrintResult(hand2.CompareWith(hand1))
  }

  fmt.Println(hand.NewHand("Th Jh Qh Kh Ah")) // Royal Flush
  fmt.Println(hand.NewHand("Ts Js Qs 9s 8s")) // Straight Flush
  fmt.Println(hand.NewHand("Ts Tc Td 9s Th")) // Four of a kind
  fmt.Println(hand.NewHand("5s 8h 5c 8s 5d")) // Full House
  fmt.Println(hand.NewHand("Kd 8d 4d Td 2d")) // Flush
  fmt.Println(hand.NewHand("5s 8h 4c 6s 7d")) // Straight
  fmt.Println(hand.NewHand("5s 7h 4c 7s 7d")) // Three of a kind
  fmt.Println(hand.NewHand("5s 6h 4c 6s 5d")) // Two Pairs
  fmt.Println(hand.NewHand("5s 7h 4c 7s 8d")) // One Pair
  fmt.Println(hand.NewHand("2s 7h 4c Ts Qd")) // Nothing
}

func PrintResult(res int) {
  if (res == result.Win) {
    fmt.Println("Win");

  } else if (res == result.Lose) {
    fmt.Println("Lose");

  } else if (res == result.Tie) {
    fmt.Println("Tie");
  }
}

/*func main() {
  l := list.New()
  l.PushBack(1)
  l.PushBack(2)
  l.PushBack(3)

  a := l.Front().Value
  b := l.Front().Next().Value
  fmt.Println(a, b)

  a_int, a_ok := a.(int)
  fmt.Println(a, a_int, a_ok)
  b_int, b_ok := b.(int)
  fmt.Println(b, b_int, b_ok, a_int + b_int)

  s := intset.New()

  fmt.Println("Add 1:", s.Add(1))
  fmt.Println("Add 2:", s.Add(2))
  fmt.Println("Add 4:", s.Add(4))
  fmt.Println("Add 3:", s.Add(3))
  fmt.Println("Add 2:", s.Add(2))
  fmt.Println("Add 4:", s.Add(4))
  fmt.Println("Add 3:", s.Add(3))

  fmt.Println("Contains 1:", s.Contains(1))
  fmt.Println("Contains 2:", s.Contains(2))
  fmt.Println("Contains 7:", s.Contains(7))
  fmt.Println("Contains 3:", s.Contains(3))
  fmt.Println("Contains 6:", s.Contains(6))
  fmt.Println("Contains 5:", s.Contains(5))
  fmt.Println("Contains 3:", s.Contains(3))

  fmt.Println("Remove 1:", s.Remove(1))
  fmt.Println("Remove 6:", s.Remove(6))
  fmt.Println("Remove 7:", s.Remove(7))
  fmt.Println("Remove 3:", s.Remove(3))
  fmt.Println("Remove 2:", s.Remove(2))
  fmt.Println("Remove 4:", s.Remove(4))
  fmt.Println("Remove 3:", s.Remove(3))

  fmt.Println("size:", s.Size())
  //maxValue := s.Max().Value()
  //minValue := s.Min().Value()
  //fmt.Println("max:", maxValue)
  //fmt.Println("min:", minValue)

  for iterator := s.Front() iterator != nil iterator = iterator.Next() {
    fmt.Println("value: ", iterator.Value())
  }

  var hand1 hand.ComparableHand = hand.NewHandHand("AC KH TS 4D 2C")
  fmt.Println(hand1)

  var hand2 hand.ComparableHand = hand.NewHandHand("2C 4D TS KH AC")
  fmt.Println(hand2)

  c1 := card.New(card.Jack, card.Spades)
  c2 := card.New(card.Queen, card.Spades)

  fmt.Println(c1 == c1)
  fmt.Println(c1 == c2)

  m := make(map[int]string)

  m[1] = "One"
  m[2] = "Two"
  m[3] = "Three"

  fmt.Println(m[1], ContainsKey(m, 1))
  fmt.Println(m[4], ContainsKey(m, 4))
  fmt.Println(m[2], ContainsKey(m, 2))
  fmt.Println(m[3], ContainsKey(m, 3))
}

func ContainsKey(m map[int]string, key int) bool {
  _, exists := m[key]
  return exists
}*/