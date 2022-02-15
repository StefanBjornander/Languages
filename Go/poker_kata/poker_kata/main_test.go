package poker

import (
	"testing"

	"poker/result"

	"github.com/stretchr/testify/assert"
)

func TestHighCardTie(t *testing.T) {
	hand1 := NewHand("Ks 2h 5c Jd Td")
	hand2 := NewHand("Kc 2s 5h Jh Tc")

	assert.Equal(t, result.Tie, hand1.CompareWith(hand2))
}

func TestPairWin(t *testing.T) {
	hand1 := NewHand("As 2h 2c Qd Td")
	hand2 := NewHand("Ac 2s 5h Kh Tc")

	assert.Equal(t, result.Win, hand1.CompareWith(hand2))
}

func TestThreeOfAKindLoss(t *testing.T) {
	hand1 := NewHand("As Ts Th Kd Td")
	hand2 := NewHand("Ac As Ah Ad Tc")

	assert.Equal(t, result.Lose, hand1.CompareWith(hand2))
}
