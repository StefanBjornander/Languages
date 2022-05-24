Object subclass: #Person
  instanceVariableNames: 'm_name'
  classVariableNames: ''
  poolDictionaries: ''
  category: nil !

!Person class methodsFor: 'instance creation'!
  name: name
    | instance |
    instance := super new.
    instance init: name.
    ^instance
  !!

!Person methodsFor: 'instance initialization'!
  init: name
    m_name := name
  !!

!Person methodsFor: 'printing'!
  printOn: stream
    super printOn: stream.
    ', name:' printOn: stream.
    m_name printOn: stream
  !!

Smalltalk at: #p put: (Person name: 'Adam') !
p printNl !

Object subclass: #Student
  instanceVariableNames: 'm_university'
  classVariableNames: ''
  poolDictionaries: ''
  category: nil !

!Student methodsFor: 'instance initialization'!
  name: n university: u
    m_university := u
  !!

!Student methodsFor: 'printing'!
  printOn: stream
    super printOn: stream.
    ', university: ' printOn: stream.
    m_university printOn: stream
  !!

"Smalltalk at: #s put: (Student name: 'Bertil' university: 'Umea') !
s printNl !"

Person subclass: #Employee
  instanceVariableNames: 'm_company'
  classVariableNames: ''
  poolDictionaries: ''
  category: nil !

!Employee methodsFor: 'instance initialization'!
  name: n company: c
    m_company := c.
    ^super name: n
  !!

!Employee methodsFor: 'printing'!
  printOn: stream
    super printOn: stream.
    ', company: ' printOn: stream.
    m_company printOn: stream
  !!

"Smalltalk at: #e put: (Employee name: 'David' company: 'Volvo') !
e printNl !"

Number subclass: #Complex
  instanceVariableNames: 'm_real m_imaginary'
  classVariableNames: ''
  poolDictionaries: ''
  category: nil !

!Complex class methodsFor: 'creating'!
  new
    ^self error: 'use real: imaginary:'
  !
  new: ignore
    ^self new
  !
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

Smalltalk at: #c put: (Complex real: 3 imaginary: 4) !
Smalltalk at: #d put: (Complex real: 3 imaginary: 5) !
c print !
d print !

Object subclass: #Cell
  instanceVariableNames: 'm_value m_next'
  classVariableNames: ''
  poolDictionaries: ''
  category: nil !

!Cell class methodsFor: 'instance creation'!
  value: v next: n
    | instance |
    instance := super new.
    instance init: v n.
    ^instance
  !!

!Cell methodsFor: 'instance initialization'!
  value: v next: n
    m_value := v.
    m_next = n
  !!

!Complex methodsFor: 'inspection'!
  value
    ^m_value
  !
  next
    ^m_next
  !!

!Complex methodsFor: 'printing'!
  printOn: stream
    super printOn: stream.
    '(:' printOn: stream.
    m_value printOn: stream.
    ',' printOn: stream.
    m_next printOn: stream.
    ')' printOn: stream
  !!

Cell at: #c2 put: (Cell value: 456 next: nil) !
Cell at: #c1 put: (Cell value: 123 next: c1) !
c1 printNl !
(c1 value) printNl !
(c1 next) printNl !

c2 printNl !
(c2 value) printNl !
(c2 next) printNl !
