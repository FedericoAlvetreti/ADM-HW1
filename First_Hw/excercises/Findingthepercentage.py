if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    media=0
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for i in student_marks[query_name]:
        media+=i
    print(format(media/3,".2f"))
