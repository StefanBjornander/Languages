package main

import (
  "testing"
  "github.com/stretchr/testify/assert"
  "result"
)

func TestHighCardTie(t *testing.T) {
  hand1 := NewHand("Ks 2h 5c Jd Td") // Nothing
  hand2 := NewHand("Kc 2s 5h Jh Tc") // Nothing
  assert.Equal(t, result.Tie, hand1.CompareWith(hand2))
}

func TestPairWin(t *testing.T) {
  hand1 := NewHand("As 2h 2c Qd Td") // One pair
  hand2 := NewHand("Ac 2s 5h Kh Tc") // Nothing
  assert.Equal(t, result.Win, hand1.CompareWith(hand2))
}

func TestThreeOfAKindLoss(t *testing.T) {
  hand1 := NewHand("As Ts Th Kd Td") // Three of a kind
  hand2 := NewHand("Ac As Ah Ad Tc") // Four of a kind
  assert.Equal(t, result.Lose, hand1.CompareWith(hand2))
}

func TestStraighFlushes(t *testing.T) {
  hand1 := NewHand("Ts Js Qs 9s 8s") // Straigh flush, queen highest
  hand2 := NewHand("Th Jh 9h 7h 8h") // Straigh flush, jack highest
  assert.Equal(t, result.Win, hand1.CompareWith(hand2))
}

// Note that the first hand wins, since it holds higher thres of a kind, even though the second hand has higher cards.
func TestFullHouse(t *testing.T) {
  hand1 := NewHand("Js Jd 8s 8c Jh") // Full house, 3 jacks, 2 eights
  hand2 := NewHand("Th Kd Td Ks Tc") // Full house, 3 tens, 2 kings
  assert.Equal(t, result.Win, hand1.CompareWith(hand2))
}

func TestStraigh(t *testing.T) {
  hand1 := NewHand("Js 7s 8s 4s Ks") // Straight of spades, king highest
  hand2 := NewHand("7h Jh 4h 8h Kh") // Straight of hearts, king highest
  assert.Equal(t, result.Tie, hand1.CompareWith(hand2))
}

func TestStraighAgain(t *testing.T) {
  hand1 := NewHand("Jc 7c 8c 3c Kc")  // Straight of clubs, king highest
  hand2 := NewHand("7d Jd 4d 8d Kd")  // Straight of diamonds, king highest
  assert.Equal(t, result.Lose, hand1.CompareWith(hand2))
}

func TestFullHouseTwoPairs(t *testing.T) {
  hand1 := NewHand("Jc Ts Js Td Th")  // Full house
  hand2 := NewHand("Ac As Kc Qd Qh")  // Two pairs
  assert.Equal(t, result.Win, hand1.CompareWith(hand2))
}

func TestRoyalFlush(t *testing.T) {
  hand1 := NewHand("Ac Qc Kc Tc Jc")  // Royal flush
  hand2 := NewHand("Qh Th Jh Kh Ah")  // Royal flush
  assert.Equal(t, result.Tie, hand1.CompareWith(hand2))
}