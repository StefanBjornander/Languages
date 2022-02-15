package card

const (
  Jack int = iota + 11
  Queen
  King
  Ace
)

const (
  Clubs int = iota
  Diamonds
  Hearts
  Spades
)

type Card struct {
  Value int
  Suit int
}

func New(value int, suit int) Card {
  return Card{value, suit}
}

func (leftCard Card) LessThan(rightCard Card) bool {
  return leftCard.Value < rightCard.Value
}

func (leftCard Card) GreaterThan(rightCard Card) bool {
  return leftCard.Value > rightCard.Value
}

func (card Card) String() string {
  valueArray := [...]string{"Two", "Three", "Four", "Five", "Six", "Seven",
                            "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"}
  suitArray := [...]string{"Clubs", "Diamonds", "Hearts", "Spades"}
  return valueArray[card.Value - 2] + " of " + suitArray[card.Suit]
}
