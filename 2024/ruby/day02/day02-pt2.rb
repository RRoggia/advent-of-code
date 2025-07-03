lines = File.read "input-test.txt"
lines = lines.split("\n")
lines = lines.map {|l| l.split(" ")}

answer = lines.reduce(0) do |sum, line|
  puts "#{line}"
  countDiff = []
  countInc = []

  for i in 0...line.length
    if i+1 < line.length
      diff = (line[i].to_i - line[i+1].to_i).abs
      if !diff.between?(1,3)
        countDiff << true 
      else
        countDiff << false
      end

      if countInc.length == 0
        countInc << (line[i].to_i > line[i+1].to_i)
      else
        countInc << countInc[i-1] == line[i].to_i > line[i+1].to_i
      end
    end
  end

  for i in 0...countDiff.length
    puts "#{countInc[i]} #{countDiff[i]}"
  end
  
end 
puts answer
