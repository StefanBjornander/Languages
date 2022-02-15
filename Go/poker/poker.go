package poker

import (
  "strings"
  "strconv"
  "container/list"
  "card"
  "result"
  "error"
  "fmt"
)

const (
  Nothing int = iota
  OnePair
  TwoPairs
  ThreeOfAKind
  Straight
  Flush
  FullHouse
  FourOfAKind
  StraightFlush
  RoyalFlush
)

type ComparableHand interface {
  CompareWith(compareTo ComparableHand) (theResult int)
}

type hand struct {
  m_cards *list.List
  m_rank, m_maxValue, m_minValue int
  m_map map[int]*list.List
  m_restValues *list.List
}

func NewHand(text string) ComparableHand {
  var newHand hand
  (&newHand).analyzeText(text)
  (&newHand).analyzeCards()
  (&newHand).setRankOfHand()
  return newHand
}

func (handPtr *hand) analyzeText(text string) {
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

    suitMap := map[string]int{"C": card.Clubs, "D": card.Diamonds,
                              "H": card.Hearts, "S": card.Spades}
    suit, exists := suitMap[suitCharUpper]
    
    if !exists {
      error.InvalidCardSuit(suitChar)
    }

    newCard := card.New(value, suit)
    inserted := false

    for iterator := handPtr.m_cards.Front(); iterator != nil;
        iterator = iterator.Next() {
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

func (handPtr *hand) analyzeCards() {
  handPtr.m_map = make(map[int]*list.List)

  for outerIterator := handPtr.m_cards.Front(); outerIterator != nil;
      outerIterator = outerIterator.Next() {
    outerCard := outerIterator.Value.(card.Card)
    count := 0

    for innerIterator := handPtr.m_cards.Front(); innerIterator != nil;
        innerIterator = innerIterator.Next() {
      innerCard := innerIterator.Value.(card.Card)

      if outerCard.Value == innerCard.Value {
        count++
      }
    }

    listPtr, exists := handPtr.m_map[count]
    if !exists {
      listPtr = list.New()
    }

    if !containsValueInList(listPtr, outerCard.Value) {
      listPtr.PushBack(outerCard.Value)
    }

    handPtr.m_map[count] = listPtr
  }
}

func containsValueInList(listPtr *list.List, value interface{}) bool {
  for iterator := listPtr.Front(); iterator != nil;
      iterator = iterator.Next() {
    if iterator.Value == value {
      return true
    }
  }

  return false
}

func (handPtr *hand) setRankOfHand() {
  if handPtr.isRoyalFlush() {
    handPtr.m_rank = RoyalFlush

  } else if handPtr.isStraightFlush() {
    handPtr.m_rank = StraightFlush
    handPtr.m_maxValue = handPtr.m_cards.Front().Value.(card.Card).Value

  } else if handPtr.isFourOfAKind() {
    handPtr.m_rank = FourOfAKind
    handPtr.m_maxValue = handPtr.m_map[4].Front().Value.(int)

  } else if handPtr.isFullHouse() {
    handPtr.m_rank = FullHouse
    handPtr.m_maxValue = handPtr.m_map[3].Front().Value.(int)

  } else if handPtr.isFlush() {
    handPtr.m_rank = Flush
    handPtr.loadCardValues(handPtr.m_cards)

  } else if handPtr.isStraight() {
    handPtr.m_rank = Straight
    handPtr.m_maxValue = handPtr.m_cards.Front().Value.(card.Card).Value

  } else if handPtr.isThreeOfAKind() {
    handPtr.m_rank = ThreeOfAKind
    handPtr.m_maxValue = handPtr.m_map[3].Front().Value.(int)

  } else if handPtr.isTwoPairs() {
    handPtr.m_rank = TwoPairs
    handPtr.m_maxValue = handPtr.m_map[2].Front().Value.(int)
    handPtr.m_minValue = handPtr.m_map[2].Front().Next().Value.(int)
    handPtr.m_restValues = handPtr.m_map[1]

  } else if handPtr.isOnePair() {
    handPtr.m_rank = OnePair
    handPtr.m_maxValue = handPtr.m_map[2].Front().Value.(int)
    handPtr.m_restValues = handPtr.m_map[1]

  } else {
    handPtr.m_rank = Nothing
    handPtr.loadCardValues(handPtr.m_cards)
  }
}

func containsKeyInMap(m map[int]*list.List, key int) bool {
  _, exists := m[key]
  return exists
}

func (handPtr *hand) loadCardValues(values *list.List) {
  handPtr.m_restValues = list.New()

  for iterator := values.Front(); iterator != nil;
      iterator = iterator.Next() {
    handPtr.m_restValues.PushBack(iterator.Value.(card.Card).Value)
  }
}

func (handPtr *hand) isRoyalFlush() bool {
  return handPtr.isStraightFlush() &&
         (handPtr.m_cards.Front().Value.(card.Card).Value == card.Ace)
}

func (handPtr *hand) isStraightFlush() bool {
  return handPtr.isStraight() && handPtr.isFlush()
}

func (handPtr *hand) isFourOfAKind() bool {  
  return containsKeyInMap(handPtr.m_map, 4)
}

func (handPtr *hand) isFullHouse() bool {
  return handPtr.isThreeOfAKind() && handPtr.isOnePair();
}

func (handPtr *hand) isFlush() bool {
  firstSuit := handPtr.m_cards.Front().Value.(card.Card).Suit
  
  for iterator := handPtr.m_cards.Front().Next(); iterator != nil;
      iterator = iterator.Next() {
    if iterator.Value.(card.Card).Suit != firstSuit {
      return false
    }
  }
  
  return true
}

func (handPtr *hand) isStraight() bool {
  firstCard := handPtr.m_cards.Front().Value.(card.Card)
  lastCard := handPtr.m_cards.Back().Value.(card.Card)

  return ((firstCard.Value - lastCard.Value) == 4) &&
         (len(handPtr.m_map) == 1) && containsKeyInMap(handPtr.m_map, 1)         
}

func (handPtr *hand) isThreeOfAKind() bool {
  return containsKeyInMap(handPtr.m_map, 3)
}

func (handPtr *hand) isTwoPairs() bool {
  return containsKeyInMap(handPtr.m_map, 2) && (handPtr.m_map[2].Len() == 2)
}

func (handPtr *hand) isOnePair() bool {
  return containsKeyInMap(handPtr.m_map, 2)
}

func (leftHand hand) CompareWith(compareTo  ComparableHand) (theResult int) {
  compare := 0
  rightHand, ok := compareTo.(hand)

  if ok {
    for iterator := leftHand.m_cards.Front(); iterator != nil;
        iterator = iterator.Next() {
      card := iterator.Value.(card.Card)
      if containsValueInList(rightHand.m_cards, card) {
        fmt.Println("overlaps: ", card)
        error.HandsOverlaps(card)
      }
    }

    if leftHand.m_rank != rightHand.m_rank {
      compare = leftHand.m_rank - rightHand.m_rank

    } else if leftHand.m_maxValue != rightHand.m_maxValue {
      compare = leftHand.m_maxValue - rightHand.m_maxValue

    } else if leftHand.m_minValue != rightHand.m_minValue {
      compare = leftHand.m_minValue - rightHand.m_minValue

    } else if leftHand.m_restValues != nil {
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

func (theHand hand) String() string {
  cardsBuffer := "{"
  for iterator := theHand.m_cards.Front(); iterator != nil;
      iterator = iterator.Next() {
    if iterator != theHand.m_cards.Front() {
      cardsBuffer += ", "
    }

    card := iterator.Value.(card.Card)
    cardsBuffer += card.String()
  }
  cardsBuffer += "}"

  rankArray := [...] string {"Nothing", "One Pair", "Two Pairs",
                     "Three Of A Kind", "Straight", "Flush", "Full House",
                     "Four Of A Kind", "Straight Flush", "Royal Flush"};
  rankBuffer := rankArray[theHand.m_rank]

  if theHand.m_maxValue != 0 {
    rankBuffer += ", max value " + strconv.Itoa(theHand.m_maxValue)
  }

  if theHand.m_minValue != 0 {
    rankBuffer += ", min value " + strconv.Itoa(theHand.m_minValue)
  }

  mapBuffer := "{"
  for size, list := range theHand.m_map {
    if len(mapBuffer) > 1 {
      mapBuffer += ", "
    }

    mapBuffer += strconv.Itoa(size) + ": ["

    for iterator := list.Front(); iterator != nil;
        iterator = iterator.Next() {
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