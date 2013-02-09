add(X,Y, Z) :- Z is  X + Y.
subtract(X, Y, Z) :- Z is X - Y.
pow(X, Z) :- Z is X * X.
%slice(Seq, Head, Tail) :-
%    [Head|Tail] = Seq.
%    slice(Tail, X, Y).

add_3_ble(X,Y) :- Y is (X + 3) * 2.

% leng - length of a list (top level only)
accLen([_|T],A,L) :- Anew is A+1, accLen(T, Anew, L).
accLen([],A,A).
leng(List, Length) :- accLen(List, 0, Length).

% Find number of all atoms in a list
%accLen(
%lengAll(List, Length).

% Find maximum value in a list (top level only)
accMax([H|T],A,Max) :-
    H > A,
    accMax(T,H,Max).
accMax([H|T],A,Max) :- 
    H =< A,
    accMax(T,A,Max).
accMax([],A,A).

% Find minimum value in a list (top level only)
accMin([H|T],A,Min) :-
    H < A,
    accMin(T,H,Min).
accMin([H|T],A,Min) :-
    H >= A,
    accMin(T,A,Min).
accMin([],A,A).

% Get the sum a list
accSumNums([H|T], Acc, Sum) :-
    NewAcc is Acc + H,
    accSumNums(T, NewAcc, Sum).
accSumNums([],Acc,Acc).
sumNums(List, Sum) :- accSumNums(List,0,Sum).

% Get the mean of a list
meanNums(List, Mean) :-
    leng(List, Length),
    sumNums(List, Sum),
    Mean is Sum / Length.

% Get squared deviation value
squaredDeviation(Number, Mean, SqDeviation) :-
    SqDeviation is (Number - Mean) ** 2.

% Get the sum of squared deviations
accSumSquares([H|T], Mean, Acc, SumSquares) :-
    squaredDeviation(H, Mean, SqDeviation),
    NewAcc is Acc + SqDeviation,
    accSumSquares(T, Mean, NewAcc, SumSquares).
accSumSquares([], _, Acc, Acc).
sumSquaredNums(List, SumSquares) :- 
    meanNums(List, Mean), 
    accSumSquares(List, Mean, 0, SumSquares).

% Variance (sample)
sampleVariance(List, SampleVariance) :-
    leng(List, Length),
    sumSquaredNums(List, SumSquares),
    SampleVariance is SumSquares / (Length - 1).

% Variance (population)
populationVariance(List, PopulationVariance) :-
    leng(List, Length),
    sumSquaredNums(List, SumSquares),
    PopulationVariance is SumSquares / Length.

% Standard deviation (sample)
sampleStdDev(List, SampleStdDev) :-
    sampleVariance(List, SampleVariance),
    SampleStdDev is sqrt(SampleVariance).

% Standard deviation (population)
populationStdDev(List, PopulationStdDev) :-
    populationVariance(List, PopulationVariance),
    PopulationStdDev is sqrt(PopulationVariance).

% Standard error
standardError(List, StandardError) :-
    leng(List, Length),
    Den is sqrt(Length),
    sampleStdDev(List, SampleStdDev),
    StandardError is SampleStdDev / Den.

% length flattened
% flatten list into vector



