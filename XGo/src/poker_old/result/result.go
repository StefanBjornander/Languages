package result

type Result int

const (
  Tie Result = iota
  Win
  Lose
)