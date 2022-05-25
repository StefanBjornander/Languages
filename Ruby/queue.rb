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

  def setNext n
    @m_next = n
  end

  public def to_s
    @m_value
  end
end

class Queue
  @m_first
  @m_last
  @m_size

  def initialize
    @m_first = nil
    @m_last = nil
    @m_size = 0
  end

  def add value
    if @m_last != nil
      @m_last.setNext (Cell.new value, nil)
      @m_last = @m_last.next
    else
      @m_first = Cell.new value, nil
      @m_last = @m_first
    end
    @m_size = @m_size + 1
  end

  def first
    if @m_first != nil
      @m_first.value
    else
      "Queue Empty"
    end
  end

  def remove
    if @m_first != nil
      firstvalue = @m_first.value
      @m_first = @m_first.next
      @m_size = @m_size - 1
      firstvalue
    else
      "Queue Empty"
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

s = Queue.new
puts s
puts "Size: #{s.size}"
puts

s.add 1
puts s
puts "first: #{s.first}"
puts "Size: #{s.size}"
puts

s.add 2
puts s
puts "first: #{s.first}"
puts "Size: #{s.size}"
puts

s.add 3
puts s
puts "first: #{s.first}"
puts "Size: #{s.size}"
puts

puts "remove: #{s.remove}"
puts s
puts "first: #{s.first}"
puts "Size: #{s.size}"
puts

puts "remove: #{s.remove}"
puts s
puts "first: #{s.first}"
puts "Size: #{s.size}"
puts

puts "remove: #{s.remove}"
puts s
puts "Size: #{s.size}"
puts

puts "first: #{s.first}"
puts "remove: #{s.remove}"
