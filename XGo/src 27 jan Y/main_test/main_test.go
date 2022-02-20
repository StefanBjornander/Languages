package main_test

import (
  "testing"
  "github.com/stretchr/testify/assert"
  "main"
  "result"
)

func TestStraightThreeOfAKind(t *testing.T) {
  hand1 := NewHand("Kh 2h 5h Jh Ah") // Straigh with ace low
  hand2 := NewHand("Kc 2s Ks 4c Kd") // Three of a kind
  assert.Equal(t, result.Win, hand1.CompareWith(hand2))
}

func TestStraightThreeOfAKindReversed(t *testing.T) {
  hand1 := NewHand("Kc 2s Ks 4c Kd") // Three of a kind
  hand2 := NewHand("Kh 2h 5h Jh Ah") // Straigh with ace low
  assert.Equal(t, result.Lose, hand1.CompareWith(hand2))
}

func TestThreeOfAKind(t *testing.T) {
  hand1 := NewHand("Kc 2s Kh 4c Kd") // Three of a kind, Kings
  hand2 := NewHand("2c Js Ks Jc Jd") // Three of a kind, Jacks
  assert.Equal(t, result.Win, hand1.CompareWith(hand2))
}

func TestThreeOfAKindReverse(t *testing.T) {
  hand1 := NewHand("2c Js Ks Jc Jd") // Three of a kind, Jacks
  hand2 := NewHand("Kc 2s Kh 4c Kd") // Three of a kind, Kings
  assert.Equal(t, result.Lose, hand1.CompareWith(hand2))
}

func TestTwoPairs(t *testing.T) {
  hand1 := NewHand("Kc 2s Kh 4c 4d") // Two pairs, Kings ansd Twos
  hand2 := NewHand("8c Js Ah Jc 8d") // Two pairs, Jacks and Eights
  assert.Equal(t, result.Win, hand1.CompareWith(hand2))
}

func TestTwoPairsReversed(t *testing.T) {
  hand1 := NewHand("8c Js Ah Jc 8d") // Two pairs, Jacks and Eights
  hand2 := NewHand("Kc 2s Kh 4c 4d") // Two pairs, Kings ansd Twos
  assert.Equal(t, result.Lose, hand1.CompareWith(hand2))
}

func TestFullHouse(t *testing.T) {
  hand1 := NewHand("5c Ks 5h Kc Kd") // Full House, 3 Kings, 2 Fives
  hand2 := NewHand("Qc As Qh Qd Ad") // Full House, 3 Queens, 2 Aces
  assert.Equal(t, result.Win, hand1.CompareWith(hand2))
}

func TestFullHouseReversed(t *testing.T) {
  hand1 := NewHand("Qc As Qh Qd Ad") // Full House, 3 Queens, 2 Aces
  hand2 := NewHand("5c Ks 5h Kc Kd") // Full House, 3 Kings, 2 Fives
  assert.Equal(t, result.Lose, hand1.CompareWith(hand2))
}

func TestFullFourOfAKind(t *testing.T) {
  hand1 := NewHand("Qc Qs Qh Qd 2d") // Four Of A Kind, Queens
  hand2 := NewHand("Ac Ts Th Tc Td") // Four Of A Kind, Tens
  assert.Equal(t, result.Win, hand1.CompareWith(hand2))
}

func TestFullFourOfAKindReversed(t *testing.T) {
  hand1 := NewHand("Ac Ts Th Tc Td") // Four Of A Kind, Tens
  hand2 := NewHand("Qc Qs Qh Qd 2d") // Four Of A Kind, Queens
  assert.Equal(t, result.Lose, hand1.CompareWith(hand2))
}

func TestStraightFlushFullFourOfAKind(t *testing.T) {
  hand1 := NewHand("2d 5d 4d 3d 6d") // Four Of A Kind, Tens
  hand2 := NewHand("Qc Qs Qh Qd 2c") // Four Of A Kind, Queens
  assert.Equal(t, result.Win, hand1.CompareWith(hand2))
}

func TestStraightFlushFullFourOfAKindReversed(t *testing.T) {
  hand1 := NewHand("Qc Qs Qh Qd 2c") // Four Of A Kind, Queens
  hand2 := NewHand("2d 5d 4d 3d 6d") // Four Of A Kind, Tens
  assert.Equal(t, result.Lose, hand1.CompareWith(hand2))
}
