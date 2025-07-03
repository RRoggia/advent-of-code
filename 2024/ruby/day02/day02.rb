lines = File.read "input.txt"
lines = lines.split("\n")
lines = lines.map {|l| l.split(" ")}

answer = lines.reduce(0) do |sum, line|
  isSafe=true
  inc = 0
  for i in 0...line.length
    if i+1 < line.length
      diff = (line[i].to_i - line[i+1].to_i).abs
      if !(diff >= 1 && diff <=3)
        isSafe = false
        break
      end
      if line[i].to_i < line[i+1].to_i
        inc += 1
      else
        inc -= 1
      end
    end
  end
  
  isSafe && inc.abs == line.length - 1 ? sum + 1 : sum
  
end 
puts answer
