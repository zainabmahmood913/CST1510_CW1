print ("hello world")

fruit = ['apple', 'banana', 'cherry', 'durian', 'elderberry']
list(range(0, 5))
fruit[-2] ## output 'durian' - negative index starts from the right
fruit[:2] ## output [apple , banana] index ends before 2
fruit[3:] ## output [durian, elderberry] index starts at 3 and goes to the end
fruit[1:4] ## output [banana, cherry, durian] index starts at 1 and ends before 4

fruit.append('fig') ## append adds fig to the end of the list
print(fruit)
fruit.pop() ## pop removes the last item from the list
print(fruit)
fruit.pop()
print(fruit)
fruit.extend(['melon' , 'grape'])
print(fruit)



df =pd.DataFrame(
    data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan', 'Fred'],
    'Age': [20, 21, 19, 22, 20, 32],
    'Grade': ['A', 'B', 'A', 'A', 'C', 'B'],
    'Score': [88, 75, 90, 95, 65, 70],
    'Enrolled': pd.to_datetime(
        ['2025-09-01', '2025-09-01', '2025-09-15', '2025-09-01', '2025-09-20', '2025-09-20']
    )
}
)