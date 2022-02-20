package error

import (
  "fmt"
  "card"
)

type Error struct {
  m_message string
}

func (errorPtr *Error) Message() string {
  return errorPtr.m_message
}

func InvalidNumberOfCards(number int) {
  panic(Error{fmt.Sprintf("Invalid number of cards in hand: %d.", number)})
}

func InvalidLengthOfCardText(cardText string) {
  panic(Error{fmt.Sprintf("Invalid length of card text: %s.", cardText)})
}

func InvalidCardValue(valueChar string) {
  panic(Error{fmt.Sprintf("Invalid card value: %s.", valueChar)})
}

func InvalidCardSuit(suitChar string) {
  panic(Error{fmt.Sprintf("Invalid card suit: %s.", suitChar)})
}

func CardOccoursTwice(card card.Card) {
  panic(Error{fmt.Sprintf("Card occours twice in the hand: %s.",
                          card.String())})
}

func HandsOverlaps(card card.Card) {
  panic(Error{fmt.Sprintf("Card occours in both hands: %s.",
                          card.String())})
}