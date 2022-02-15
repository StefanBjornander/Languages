package hand

import "strings"
import "strconv"

import "card"
import "error"
import "result"
import "container/list"

type ComparableHand interface {
  CompareWith(compareTo ComparableHand) (result int)
}

type Hand struct {
  m_cards *list.List
  m_rank, m_maxValue, m_minValue int
  m_map map[int]*list.List
  m_restValues *list.List
}

func NewHand(text string) ComparableHand {
  var hand Hand
  (&hand).TextToCards(text)
  (&hand).ExtractSameOfAKind()
  (&hand).SetRankOfHand()
  return hand
}

func (handPtr *Hand) TextToCards(text string) {
  handPtr.m_cards = list.New()
  cardTextArray := strings.Split(text, " ")

  if len(cardTextArray) != 5 {
    error.InvalidNumberOfCards(len(cardTextArray))
  }

  for _, cardText := range cardTextArray {
    if len(cardText) != 2 {
      error.InvalidLengthOfCardText(cardText)
    }

    valueChar := string(cardText[0])
    valueCharUpper := strings.ToUpper(valueChar)

    const valueText string = "23456789TJQKA"
    var value int

    if strings.Contains(valueText, valueCharUpper) {
      value = strings.Index(valueText, valueCharUpper) + 2
    } else {
      error.InvalidCardValue(valueChar)
    }

    suitChar := string(cardText[1])
    suitCharUpper := strings.ToUpper(suitChar)

    suitMap := map[string]int{"C": card.Clubs, "D": card.Diamonds, "H": card.Hearts, "S": card.Spades}
    suit, exists := suitMap[suitCharUpper]
    
    if !exists {
      error.InvalidCardSuit(suitChar)
    }

    newCard := card.New(value, suit)
    inserted := false

    for iterator := handPtr.m_cards.Front(); iterator != nil; iterator = iterator.Next() {
      card := iterator.Value.(card.Card)

      if card == newCard {
        error.CardOccoursTwice(card)
      }

      if newCard.GreaterThan(card) {
        handPtr.m_cards.InsertBefore(newCard, iterator)
        inserted = true
        break
      }
    }

    if !inserted {
      handPtr.m_cards.PushBack(newCard)
    }
  }
}

func (handPtr *Hand) ExtractSameOfAKind() {
  handPtr.m_map = make(map[int]*list.List)

  for outerIterator := handPtr.m_cards.Front(); outerIterator != nil; outerIterator = outerIterator.Next() {
    outerCard := outerIterator.Value.(card.Card)
    count := 0

    for innerIterator := handPtr.m_cards.Front(); innerIterator != nil; innerIterator = innerIterator.Next() {
      innerCard := innerIterator.Value.(card.Card)

      if outerCard.Value == innerCard.Value {
        count++
      }
    }

    var listPtr *list.List

    if ContainsKeyInMap(handPtr.m_map, count) {
      listPtr = handPtr.m_map[count]
          
    } else {
      listPtr = list.New()
    }

    if !ContainsValueInList(listPtr, outerCard.Value) {
      listPtr.PushBack(outerCard.Value)
    }

    handPtr.m_map[count] = listPtr
  }
}

func ContainsValueInList(listPtr *list.List, value interface{}) bool {
  for iterator := listPtr.Front(); iterator != nil; iterator = iterator.Next() {
    if iterator.Value == value {
      return true
    }
  }

  return false
}

func (handPtr *Hand) SetRankOfHand() {
  if handPtr.IsRoyalFlush() {
    handPtr.m_rank = card.RoyalFlush

  } else if handPtr.IsStraightFlush() {
    handPtr.m_rank = card.StraightFlush
    handPtr.m_maxValue = handPtr.m_cards.Front().Value.(card.Card).Value

  } else if handPtr.IsFourOfAKind() {
    handPtr.m_rank = card.FourOfAKind
    handPtr.m_maxValue = handPtr.m_map[4].Front().Value.(int)

  } else if handPtr.IsFullHouse() {
    handPtr.m_rank = card.FullHouse
    handPtr.m_maxValue = handPtr.m_map[3].Front().Value.(int)

  } else if handPtr.IsFlush() {
    handPtr.m_rank = card.Flush
    handPtr.LoadCardValues(handPtr.m_cards)

  } else if handPtr.IsStraight() {
    handPtr.m_rank = card.Straight
    handPtr.m_maxValue = handPtr.m_cards.Front().Value.(card.Card).Value

  } else if handPtr.IsThreeOfAKind() {
    handPtr.m_rank = card.ThreeOfAKind
    handPtr.m_maxValue = handPtr.m_map[3].Front().Value.(int)

  } else if handPtr.IsTwoPairs() {
    handPtr.m_rank = card.TwoPairs
    handPtr.m_maxValue = handPtr.m_map[2].Front().Value.(int)
    handPtr.m_minValue = handPtr.m_map[2].Front().Next().Value.(int)
    handPtr.m_restValues = handPtr.m_map[1]

  } else if handPtr.IsOnePair() {
    handPtr.m_rank = card.OnePair
    handPtr.m_maxValue = handPtr.m_map[2].Front().Value.(int)
    handPtr.m_restValues = handPtr.m_map[1]

  } else {
    handPtr.m_rank = card.Nothing
    handPtr.LoadCardValues(handPtr.m_cards)
  }
}

func (handPtr *Hand) LoadCardValues(values *list.List) {
  handPtr.m_restValues = list.New()

  for iterator := values.Front(); iterator != nil; iterator = iterator.Next() {
    handPtr.m_restValues.PushBack(iterator.Value.(card.Card).Value)
  }
}

func (handPtr *Hand) IsRoyalFlush() bool {
  return handPtr.IsStraightFlush() && (handPtr.m_cards.Front().Value.(card.Card).Value == card.Ace)
}

func (handPtr *Hand) IsStraightFlush() bool {
  return handPtr.IsStraight() && handPtr.IsFlush()
}

func (handPtr *Hand) IsFourOfAKind() bool {  
  return ContainsKeyInMap(handPtr.m_map, 4)
}

func (handPtr *Hand) IsFullHouse() bool {
  return handPtr.IsThreeOfAKind() && handPtr.IsOnePair();
}

func (handPtr *Hand) IsFlush() bool {
  firstSuit := handPtr.m_cards.Front().Value.(card.Card).Suit
  
  for iterator := handPtr.m_cards.Front().Next(); iterator != nil; iterator = iterator.Next() {
    if iterator.Value.(card.Card).Suit != firstSuit {
      return false
    }
  }
  
  return true
}

func (handPtr *Hand) IsStraight() bool {
  firstCard := handPtr.m_cards.Front().Value.(card.Card)
  lastCard := handPtr.m_cards.Back().Value.(card.Card)

  return (len(handPtr.m_map) == 1) && ContainsKeyInMap(handPtr.m_map, 1) &&
         (firstCard.Value == (lastCard.Value + 4))
}

func (handPtr *Hand) IsThreeOfAKind() bool {
  return ContainsKeyInMap(handPtr.m_map, 3)
}

func (handPtr *Hand) IsTwoPairs() bool {
  return ContainsKeyInMap(handPtr.m_map, 2) && (handPtr.m_map[2].Len() == 2)
}

func (handPtr *Hand) IsOnePair() bool {
  return ContainsKeyInMap(handPtr.m_map, 2)
}

func ContainsKeyInMap(m map[int]*list.List, key int) bool {
  _, exists := m[key]
  return exists
}

func (leftHand Hand) CompareWith(compareTo  ComparableHand) (res int) {
  compare := 0
  rightHand, ok := compareTo.(Hand)

  if ok {
    for iterator := leftHand.m_cards.Front(); iterator != nil; iterator = iterator.Next() {
      card := iterator.Value.(card.Card)
      if ContainsValueInList(rightHand.m_cards, card) {
        error.HandsOverlaps(card)
      }
    }

    if leftHand.m_rank != rightHand.m_rank {
      compare = leftHand.m_rank - rightHand.m_rank

    } else if leftHand.m_maxValue != rightHand.m_maxValue {
      compare = leftHand.m_maxValue - rightHand.m_maxValue

    } else if leftHand.m_minValue != rightHand.m_minValue {
      compare = leftHand.m_minValue - rightHand.m_minValue

    } else {
      leftIterator := leftHand.m_restValues.Front()
      rightIterator := rightHand.m_restValues.Front();

      for leftIterator != nil {
        leftValue := leftIterator.Value.(int)
        rightValue := rightIterator.Value.(int)

        if leftValue != rightValue {
          compare = leftIterator.Value.(int) - rightIterator.Value.(int)
          break
        }

        leftIterator = leftIterator.Next()
        rightIterator = rightIterator.Next()
      }
    }
  }

  if compare > 0 {
    return result.Win

  } else if compare < 0 {
    return result.Lose

  } else {
    return result.Tie
  }
}

func (hand Hand) String() string {
  cardsBuffer := "{"
  for iterator := hand.m_cards.Front(); iterator != nil; iterator = iterator.Next() {
    if iterator != hand.m_cards.Front() {
      cardsBuffer += ", "
    }

    card := iterator.Value.(card.Card)
    cardsBuffer += card.String()
  }
  cardsBuffer += "}"

  rankArray := [...] string {"Nothing", "One Pair", "Two Pairs",
                             "Three Of A Kind", "Straight", "Flush", "Full House",
                             "Four Of A Kind", "Straight Flush", "Royal Flush"};
  rankBuffer := rankArray[hand.m_rank]

  if hand.m_maxValue != 0 {
    rankBuffer += ", max value " + strconv.Itoa(hand.m_maxValue)
  }

  if hand.m_minValue != 0 {
    rankBuffer += ", min value " + strconv.Itoa(hand.m_minValue)
  }

  mapBuffer := "{"
  for size, list := range hand.m_map {
    if len(mapBuffer) > 1 {
      mapBuffer += ", "
    }

    mapBuffer += strconv.Itoa(size) + ": ["

    for iterator := list.Front(); iterator != nil; iterator = iterator.Next() {
      if iterator != list.Front() {
        mapBuffer += ", "
      }

      mapBuffer += strconv.Itoa(iterator.Value.(int))
    }

    mapBuffer += "]"
  }
  mapBuffer += "}"

  return cardsBuffer + "\n" + rankBuffer + ", " + mapBuffer + "\n"
}