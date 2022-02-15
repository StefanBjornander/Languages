package poker

// ComparableHand contains attributes of a poker hand
type ComparableHand interface {
	CompareWith(compareTo ComparableHand) (result int)
}

// NewHand returns something that represents a hand with the given `cards`
func NewHand(hand string) ComparableHand {

}
