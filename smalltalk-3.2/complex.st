Number subclass: #Complex
  instanceVariableNames: 'm_real m_imaginary'
  classVariableNames: ''
  poolDictionaries: ''
  category: nil !

!Complex class methodsFor: 'creating'!
  real: r imaginary: i
    ^(super new) setReal: r setImaginary: i
  !!

!Complex methodsFor: 'creating--private'!
  setReal: r setImaginary: i
    m_real := r.
    m_imaginary := i.
    ^self
  !!

!Complex methodsFor: 'calculating'!
  real
    ^m_real
  !
  imaginary
    ^m_imaginary
  !
"  absolute: value
    (value < 0)
      ifTrue: [^(0 - value)]
      ifFalse: [^value]
  !
  squareroot: value root: oldRoot
    | newRoot difference |
    'value: ' print.
    value printNl.
    'oldRoot: ' print.
    oldRoot printNl.
    newRoot := (value + (value / oldRoot)) / 2.0.
    difference := self absolute: (newRoot - oldRoot).
    (difference < 0.000001)
      ifTrue: [^newRoot]
      ifFalse: [^self squareroot: value root: newRoot]
  !"
  length
    ^((m_real * m_real) + (m_imaginary * m_imaginary))
  !
  + value
    ^Complex real: m_real + value real imaginary: m_imaginary + value imaginary
  !
  - value
    ^(Complex real: (m_real - (value real)) imaginary: (m_imaginary - (value imaginary)))
  !
  * value
    ^(Complex real: ((m_real * (value real)) - (m_imaginary * (value imaginary)))
              imaginary: ((m_real * (value imaginary)) + (m_imaginary * (value real))))
  !
  / value
    | d r i |
    d := ((value real) * (value real)) + ((value imaginary) * (value imaginary)).
    r := ((m_real * (value real)) + (m_imaginary * (value imaginary))) / d.
    i := ((m_imaginary * (value real)) - (m_real * (value imaginary))) / d.
    ^(Complex real: r imaginary: i)
  !
  = value
    ^((m_real = (value real)) and: [m_imaginary = (value imaginary)])
  !
  ~= value
    ^((self = value) not)
  !
  < value
    ^((self length) < (value length))
  !
  <= value
    ^((self < value) or: [self = value])
  !
  > value
    ^((self <= value) not)
  !
  >= value
    ^((self < value) not)
  !!

!Complex methodsFor: 'printing'!
  printOn: stream
    super printOn: stream.
    ':' printOn: stream.
    m_real printOn: stream.
    '+' printOn: stream.
    m_imaginary printOn: stream.
    'i' printOn: stream
  !!

Smalltalk at: #c put: (Complex real: 2 imaginary: 4) !
c printNl !
(c real) printNl !
(c imaginary) printNl !
(c length) printNl !

Smalltalk at: #d put: (Complex real: 3 imaginary: 5) !
d printNl !
(d real) printNl !
(d imaginary) printNl !
(d length) printNl !
