Object subclass: #Person
  instanceVariableNames: 'name balance'
  classVariableNames: ''
  poolDictionaries: ''
  category: nil !

!Person class methodsFor: 'instance creation'!
  new
    | instance |
    instance := super new.
    instance init.
    ^instance
  !!

!Person methodsFor: 'instance initialization'!
  init
    name := 'John Smith'.
    balance := 0
  !!

!Person methodsFor: 'moving money'!
  withdraw: amount
    balance := balance - amount
  !
  deposit: amount
    balance := balance + amount
  !!

!Person methodsFor: 'printing'!
  printOn: stream
    super printOn: stream.
    ', name: ' printOn: stream.
    name printOn: stream.
    ', balance: ' printOn: stream.
    balance printOn: stream
  !!

Smalltalk at: #p put: (Person new) !
p deposit: 250 !
p withdraw: 100 !
p printNl !

Person subclass: #Student
  instanceVariableNames: 'university'
  classVariableNames: ''
  poolDictionaries: ''
  category: nil !

!Student methodsFor: 'instance initialization'!
  init
    university := 'Umeå'.
    ^super init
  !!

!Student methodsFor: 'printing'!
  printOn: stream
    super printOn: stream.
    ', university: ' printOn: stream.
    university printOn: stream
  !!

Smalltalk at: #s put: (Student new) !
s printNl !

Person subclass: #Employee
  instanceVariableNames: 'company'
  classVariableNames: ''
  poolDictionaries: ''
  category: nil !

!Employee methodsFor: 'instance initialization'!
  init
    company := 'Volvo'.
    ^super init
  !!

!Employee methodsFor: 'printing'!
  printOn: stream
    super printOn: stream.
    ', company: ' printOn: stream.
    company printOn: stream
  !!

Smalltalk at: #e put: (Employee new) !
e printNl !
