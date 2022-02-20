package result

type Result int

const (
  Tie Result = iota
  Win
  Lose
)

func (result Result) String() string {
  switch result:
    case Tie:
      return "Tie"

    case Win:
      return "Win"

    case Lose:
      return "Lose"
  }
}