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

Person subclass: #Student
  instanceVariableNames: 'm_university'
  classVariableNames: ''
  poolDictionaries: ''
  category: nil !

!Student class methodsFor: 'instance creation'!
  name: n university: u
    | instance |
    instance := super new.
    instance init: n university: u.
    ^instance
  !!

!Student methodsFor: 'instance initialization'!
  init: n university: u
    m_university := u.
    super init: n
  !!

!Student methodsFor: 'printing'!
  printOn: stream
    super printOn: stream.
    ', university: ' printOn: stream.
    m_university printOn: stream
  !!

Smalltalk at: #s put: (Student name: 'Bertil' university: 'Umea') !
s printNl !

Person subclass: #Employee
  instanceVariableNames: 'm_company'
  classVariableNames: ''
  poolDictionaries: ''
  category: nil !

!Employee class methodsFor: 'instance creation'!
  name: n company: c
    | instance |
    instance := super new.
    instance init: n company: c.
    ^instance
  !!

!Employee methodsFor: 'instance initialization'!
  init: n company: c
    m_company := c.
    super init: n
  !!

!Employee methodsFor: 'printing'!
  printOn: stream
    super printOn: stream.
    ', company: ' printOn: stream.
    m_company printOn: stream
  !!

Smalltalk at: #e put: (Employee name: 'David' company: 'Volvo') !
e printNl !
