student(101, arun).
student(102, priya).
student(103, kumar).

course(c101, python).
course(c102, java).

faculty(f1, ramesh).
faculty(f2, priya).

enrollment(101, c101, f1).
enrollment(102, c102, f2).
enrollment(103, c101, f1).

enrolled(X, Y) :-
    enrollment(X, Y, F).

student_course(X, Y) :-
    enrolled(S, Y),
    student(S, X).