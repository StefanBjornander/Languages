Class = {}
Class.new = function(self, object)
  object = object or {}
  setmetatable(object, self)
  self.__index = self
  return object
end

Cell = {}
Cell.construct = function(self, value, next)
  return Class.new(self, {m_value = value, m_next = next})
end

Cell.value = function(self)
  return self.m_value
end

Cell.next = function(self)
  return self.m_next
end

Cell.__tostring = function(self)
  return tostring(self.m_value)
end

Stack = {}
Stack.construct = function(self)
  return Class.new(self, {m_first = nil, m_size = 0})
end

Stack.push = function(self, value)
  self.m_first = Cell:construct(value, self.m_first)
end

Stack.top = function(self)
  assert(self.m_first ~= nil, "Top: Stack Empty.")
  return self.m_first:value()
end

Stack.pop = function(self)
  assert(self.m_first ~= nil, "Pop: Stack Empty.")
  top_value = self.m_first:value()
  self.m_first = self.m_first:next()
  return top_value
end

Stack.size = function(self)
  return self.m_size
end

Stack.__tostring = function(self)
  return "[" .. Stack.__tostringX(self.m_first, true) .. "]"
end

Stack.__tostringX = function(current, first)
  if current ~= nil then
    return ((first and "") or ",") .. current:value()
           .. Stack.__tostringX(current:next(), false)
  else
    return ""
  end
end

s = Stack:construct()
print(s)
print("Size: " .. s:size())
print()

s:push(1)
print(s)
print("Top: " .. s:top())
print("Size: " .. s:size())
print()

s:push(2)
print(s)
print("Top: " .. s:top())
print("Size: " .. s:size())
print()

s:push(3)
print(s)
print("Top: " .. s:top())
print("Size: " .. s:size())
print()

print("Pop: " .. s:pop())
print(s)
print("Top: " .. s:top())
print("Size: " .. s:size())
print()

print("Pop: " .. s:pop())
print(s)
print("Top: " .. s:top())
print("Size: " .. s:size())
print()

print("Pop: " .. s:pop())
print(s)
print("Size: " .. s:size())
--print("Top: " .. s:top())
--print("Pop: " .. s:pop())
