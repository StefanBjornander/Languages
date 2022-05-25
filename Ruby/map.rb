class Pair
  :@m_key
  :@m_value

  def initialize key, value
    @m_key = key
    @m_value = value
  end

  def key
    @m_key
  end

  def value
    @m_value
  end

  def setValue value
    @m_value = value
  end

  public def to_s
    "(#{@m_key},#{@m_value})"
  end
end

class Cell
  :@m_pair
  :@m_next

  def initialize pair, n
    @m_pair = pair
    @m_next = n
  end

  def pair
    @m_pair
  end

  def next
    @m_next
  end

  def setNext n
    @m_next = n
  end

  public def to_s
    @m_pair.to_s
  end
end

class Map
  @m_first
  @m_last
  @m_size

  def initialize
    @m_first = nil
    @m_last = nil
    @m_size = 0
  end

  def put key, value
    putX @m_first, key, value, nil
  end

  private def putX current, key, value, last
    if current != nil
      if key == current.pair.key
        previousvalue = current.pair.value
        current.pair.setValue value
        previousvalue
      else
        putX current.next, key, value, current
      end
    else
      if last != nil
        last.setNext (Cell.new (Pair.new key, value), nil)
      else
        @m_first = (Cell.new (Pair.new key, value), nil)
      end

      @m_size = @m_size + 1
    end
  end

  def exists key
    existsX @m_first, key, nil
  end

  private def existsX current, key, last
    if current != nil
      if key == current.pair.key
        true
      else
        existsX current.next, key, current
      end
    else
      false
    end
  end

  def remove key
    removeX @m_first, key, nil
  end

  private def removeX current, key, last
    if current != nil
      if key == current.pair.key
        previousvalue = current.pair.value

        if last != nil
          last.setNext current.next
        else
          @m_first.setNext @m_first.next
        end

        @m_size = @m_size - 1
        previousvalue
      else
        removeX current.next, key, current
      end
    else
      nil
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
      "#{first ? "" : ","}#{current.pair}#{to_sX current.next, false}"
    else
      ""
    end
  end
end

m = Map.new
puts m
puts "Size: #{m.size}"
puts

m.put 1, "A"
puts m
puts "Size: #{m.size}"
puts

m.put 2, "B"
puts m
puts "Size: #{m.size}"
puts

m.put 3, "C"
puts m
puts "Size: #{m.size}"
puts

m.put 2, "D"
puts m
puts "Size: #{m.size}"
puts

puts "Exists 0: #{m.exists 0}"
puts "Exists 1: #{m.exists 1}"
puts "Exists 2: #{m.exists 2}"
puts "Exists 3: #{m.exists 3}"
puts "Exists 4: #{m.exists 4}"
puts

puts "remove 2: #{m.remove 2}"
puts m
puts "Size: #{m.size}"
puts

puts "remove 3: #{m.remove 3}"
puts m
puts "Size: #{m.size}"
puts

puts "remove 1: #{m.remove 1}"
puts m
puts "Size: #{m.size}"
puts

puts "remove 2: #{m.remove 2}"
puts m
puts "Size: #{m.size}"
