Object subclass: #Cell
  instanceVariableNames: 'm_value m_next'
  classVariableNames: ''
  poolDictionaries: ''
  category: nil !

!Cell class methodsFor: 'instance creation'!
  value: value next: next
    | instance |
    instance := super new.
    instance init: value next: next.
    ^instance
  !!

!Cell methodsFor: 'instance initialization'!
  init: value next: next
    m_value := value.
    m_next := next
  !!

!Cell methodsFor: 'inspection'!
  value
    ^m_value
  !
  next
    ^m_next
  !!

!Cell methodsFor: 'printing'!
  printOn: stream
    super printOn: stream.
    '(' printOn: stream.
    m_value printOn: stream.
    ',' printOn: stream.
    m_next printOn: stream.
    ')' printOn: stream
  !!

Smalltalk at: #c3 put: (Cell value: 789 next: nil) !
c3 printNl !
Smalltalk at: #c2 put: (Cell value: 456 next: c3) !
c2 printNl !
Smalltalk at: #c1 put: (Cell value: 123 next: c2) !
c1 printNl !
'' printNl !

Object subclass: #Stack
  instanceVariableNames: 'm_first m_size'
  classVariableNames: ''
  poolDictionaries: ''
  category: nil !

!Stack class methodsFor: 'instance creation'!
  new
    | instance |
    instance := super new.
    instance init.
    ^instance
  !!

!Stack methodsFor: 'instance initialization'!
  init
    m_first := nil.
    m_size := 0
  !!

!Stack methodsFor: 'modification'!
  push: value
    m_first := (Cell value: value next: m_first).
    m_size := m_size + 1
  !
  top
    (m_first ~= nil) ifFalse: [^self error: 'Empty stack.'].
    ^(m_first value)
  !
  pop
    | firstvalue |
    (m_first ~= nil) ifFalse: [^self error: 'Empty stack.'].
    firstvalue := (m_first value).
    m_first := (m_first next).
    m_size := m_size - 1.
    ^firstvalue
  !
  size
    ^m_size
  !!

!Stack methodsFor: 'printing'!
  printStack: stream current: current first: first
    (current ~= nil)
      ifTrue: [
        first ifFalse: [',' printOn: stream].
        (current value) printOn: stream.
        self printStack: stream current: (current next) first: false
      ]
  !
  printOn: stream
    super printOn: stream.
    ' [' printOn: stream.
    self printStack: stream current: m_first first: true.
    ']' printOn: stream.
  !!

Smalltalk at: #s put: (Stack new) !
s printNl !
'Size: ' print !
(s size) printNl !

(s push: 1) !
s printNl !
'Size: ' print !
(s size) printNl !

(s push: 2) !
s printNl !
'Size: ' print !
(s size) printNl !

(s push: 3) !
s printNl !
'Size: ' print !
(s size) printNl !

'Pop: ' print !
(s pop) printNl !
s printNl !
'Size: ' print !
(s size) printNl !

'Pop: ' print !
(s pop) printNl !
s printNl !
'Size: ' print !
(s size) printNl !
