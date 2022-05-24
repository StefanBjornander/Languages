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
  !
  setNext: next
    m_next := next
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

Object subclass: #Queue
  instanceVariableNames: 'm_first m_last m_size'
  classVariableNames: ''
  poolDictionaries: ''
  category: nil !

!Queue class methodsFor: 'instance creation'!
  new
    | instance |
    instance := super new.
    instance init.
    ^instance
  !!

!Queue methodsFor: 'instance initialization'!
  init
    m_first := nil.
    m_last := nil.
    m_size := 0
  !!

!Queue methodsFor: 'modification'!
  add: value
    | newLink |
    newLink := (Cell value: value next: nil).

    (m_last == nil)
      ifTrue: [m_first := newLink]
      ifFalse: [m_last setNext: newLink].
    m_last := newLink.
    m_size := m_size + 1
  !
  first
    (m_first ~= nil) ifFalse: [^self error: 'Empty Queue.'].
    ^(m_first value)
  !
  last
    (m_last ~= nil) ifFalse: [^self error: 'Empty Queue.'].
    ^(m_last value)
  !
  remove
    | firstvalue |
    firstvalue := (m_first value).
    m_first := (m_first next).
    (m_first == nil) ifTrue: [m_last := nil].
    m_size := m_size - 1.
    ^firstvalue
  !
  size
    ^m_size
  !!

!Queue methodsFor: 'printing'!
  printQueue: stream current: current first: first
    (current ~= nil)
      ifTrue: [
        first ifFalse: [',' printOn: stream].
        (current value) printOn: stream.
        self printQueue: stream current: (current next) first: false
      ]
  !
  printOn: stream
    super printOn: stream.
    ' [' printOn: stream.
    self printQueue: stream current: m_first first: true.
    ']' printOn: stream.
  !!

Smalltalk at: #q put: (Queue new) !
q printNl !

(q add: 1) !
q printNl !
'First: ' print !
(q first) printNl !
'Last: ' print !
(q last) printNl !
'Size: ' print !
(q size) printNl !

(q add: 2) !
q printNl !
'First: ' print !
(q first) printNl !
'Last: ' print !
(q last) printNl !
'Size: ' print !
(q size) printNl !

(q add: 3) !
q printNl !
'First: ' print !
(q first) printNl !
'Last: ' print !
(q last) printNl !
'Size: ' print !
(q size) printNl !

(q remove) !
q printNl !
'First: ' print !
(q first) printNl !
'Last: ' print !
(q last) printNl !
'Size: ' print !
(q size) printNl !

(q remove) !
q printNl !
'First: ' print !
(q first) printNl !
'Last: ' print !
(q last) printNl !
'Size: ' print !
(q size) printNl !
