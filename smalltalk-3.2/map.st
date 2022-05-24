Object subclass: #Pair
  instanceVariableNames: 'm_key m_value'
  classVariableNames: ''
  poolDictionaries: ''
  category: nil !

!Pair class methodsFor: 'instance creation'!
  key: key value: value
    | instance |
    instance := super new.
    instance init: key value: value.
    ^instance
  !!

!Pair methodsFor: 'instance initialization'!
  init: key value: value
    m_key := key.
    m_value := value
  !!

!Pair methodsFor: 'inspection'!
  key
    ^m_key
  !
  value
    ^m_value
  !
  setValue: value
    m_value := value
  !!

!Pair methodsFor: 'printing'!
  printOn: stream
    super printOn: stream.
    '(' printOn: stream.
    m_key printOn: stream.
    ',' printOn: stream.
    m_value printOn: stream.
    ')' printOn: stream
  !!

Object subclass: #Cell
  instanceVariableNames: 'm_pair m_next'
  classVariableNames: ''
  poolDictionaries: ''
  category: nil !

!Cell class methodsFor: 'instance creation'!
  pair: pair next: next
    | instance |
    instance := super new.
    instance init: pair next: next.
    ^instance
  !!

!Cell methodsFor: 'instance initialization'!
  init: pair next: next
    m_pair := pair.
    m_next := next
  !!

!Cell methodsFor: 'inspection'!
  pair
    ^m_pair
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
    m_pair printOn: stream.
    ',' printOn: stream.
    m_next printOn: stream.
    ')' printOn: stream
  !!

Object subclass: #Map
  instanceVariableNames: 'm_first m_size'
  classVariableNames: ''
  poolDictionaries: ''
  category: nil !

!Map class methodsFor: 'instance creation'!
  new
    | instance |
    instance := super new.
    instance init.
    ^instance
  !!

!Map methodsFor: 'instance initialization'!
  init
    m_first := nil.
    m_size := 0
  !!

!Map methodsFor: 'modification'!
  key: key value: value
    ^(self keyX: key value: value current: m_first)
  !
  keyX: key value: value current: current
    (current ~= nil)
      ifTrue: [
        (key = ((current pair) key))
          ifTrue: [
            | lastvalue |
            lastvalue := (current pair) value.
            (current pair) setValue: value.
            ^lastvalue
          ]
          ifFalse: [^(self keyX: key value: value current: (current next))]
        ]
      ifFalse: [
        m_first := Cell pair: (Pair key: key value: value) next: m_first.
        ^nil
      ].
  !
  exists: key
    ^(self existsX: key current: m_first)
  !
  existsX: key current: current
    (current ~= nil)
      ifTrue: [
        (key = ((current pair) key))
          ifTrue: [^true]
          ifFalse: [^(self existsX: key current: (current next))]
        ]
      ifFalse: [^false]
  !
  get: key
    ^(self getX: key current: m_first)
  !
  getX: key current: current
    (current ~= nil)
      ifTrue: [
        (key = ((current pair) key))
          ifTrue: [^((current pair) value)]
          ifFalse: [^(self getX: key current: (current next))]
        ]
      ifFalse: [^nil]
  !
  remove: key
    ^(self removeX: key current: m_first last: nil)
  !
  removeX: key current: current last: last
    (current ~= nil)
      ifTrue: [
        (key = ((current pair) key))
          ifTrue: [
            (last == nil)
              ifTrue: [m_first := (current next)]
              ifFalse: [last setNext: (current next)].
            ^((current pair) value)
          ]
          ifFalse: [^(self removeX: key current: (current next) last: current)]
      ]
      ifFalse: [^nil]
  !
  size
    ^m_size
  !!

!Map methodsFor: 'printing'!
  printQueue: stream current: current first: first
    (current ~= nil)
      ifTrue: [
        first ifFalse: [',' printOn: stream].
        (current pair) printOn: stream.
        self printQueue: stream current: (current next) first: false
      ]
  !
  printOn: stream
    super printOn: stream.
    ' [' printOn: stream.
    self printQueue: stream current: m_first first: true.
    ']' printOn: stream.
  !!

Smalltalk at: #m put: (Map new) !
m printNl !

(m key: 1 value: 'A') !
m printNl !

(m key: 2 value: 'B') !
m printNl !

(m key: 3 value: 'C') !
m printNl !

'exists 0: ' print !
(m exists: 0) printNl !
'exists 1: ' print !
(m exists: 1) printNl !
'exists 2: ' print !
(m exists: 2) printNl !
'exists 3: ' print !
(m exists: 3) printNl !
'exists 4: ' print !
(m exists: 4) printNl !

'get 0: ' print !
(m get: 0) printNl !
'get 1: ' print !
(m get: 1) printNl !
'get 2: ' print !
(m get: 2) printNl !
'get 3: ' print !
(m get: 3) printNl !
'get 4: ' print !
(m get: 4) printNl !

'remove 0: ' print !
(m remove: 0) printNl !
m printNl !
'remove 2: ' print !
(m remove: 2) printNl !
m printNl !
'remove 1: ' print !
(m remove: 1) printNl !
m printNl !
'remove 3: ' print !
(m remove: 3) printNl !
m printNl !
'remove 4: ' print !
(m remove: 4) printNl !
m printNl !
