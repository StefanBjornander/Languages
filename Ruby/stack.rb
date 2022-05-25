class Cell
  :@m_value
  :@m_next

  def initialize value, n
    @m_value = value
    @m_next = n
  end

  def value
    @m_value
  end

  def next
    @m_next
  end

  public def to_s
    @m_value
  end
end

class Stack
  @m_first
  @m_size

  def initialize
    @m_first = nil
    @m_size = 0
  end

  def push value
    @m_first = Cell.new(value, @m_first)
    @m_size = @m_size + 1
  end

  def top
    if @m_first != nil
      @m_first.value
    else
      "Stack Empty"
    end
  end

  def pop
    if @m_first != nil
      firstvalue = @m_first.value
      @m_first = @m_first.next
      @m_size = @m_size - 1
      firstvalue
    else
      "Stack Empty"
    end
  end

  def size
    @m_size
  end

  def to_s
    "[#{to_sX @m_first, true}]"
  end

  private def to_sX current, first
    if current != nil
      "#{first ? "" : ","}#{current.value}#{to_sX current.next, false}"
    else
      ""
    end
  end
end

s = Stack.new
puts s
puts "Size: #{s.size}"
puts

s.push 1
puts s
puts "Top: #{s.top}"
puts "Size: #{s.size}"
puts

s.push 2
puts s
puts "Top: #{s.top}"
puts "Size: #{s.size}"
puts

s.push 3
puts s
puts "Top: #{s.top}"
puts "Size: #{s.size}"
puts

puts "Pop: #{s.pop}"
puts s
puts "Top: #{s.top}"
puts "Size: #{s.size}"
puts

puts "Pop: #{s.pop}"
puts s
puts "Top: #{s.top}"
puts "Size: #{s.size}"
puts

puts "Pop: #{s.pop}"
puts s
puts "Size: #{s.size}"
puts

puts "Top: #{s.top}"
puts "Pop: #{s.pop}"