numbers = [1,2,4,3,2,5,6,77,0,9]

srt_up = sorted(numbers)
print(srt_up)
srt_down = sorted(numbers, reverse=True)
print(srt_down)
srt_down = sorted(numbers)[::-1]
print(srt_down)

print(numbers)
numbers.sort(reverse=True)
print(numbers)
