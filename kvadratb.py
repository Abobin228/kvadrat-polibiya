

kvadrat =  [['а','б','в','г','д','е','ё','ж','з'],
           ['и','й','к','л','м','н','о','п','р'],
           ['с','т','у','ф','х','ц','ч','ш','щ'],
           ['ъ','ы','ь','э','ю','я','.',',',' '],
           ['А','Б','В','Г','Д','Е','Ё','Ж','З'],
           ['И','Й','К','Л','М','Н','О','П','Р'],
           ['С','Т','У','Ф','Х','Ц','Ч','Ш','Щ'],
           ['Ъ','Ы','Ь','Э','Ю','Я','?','-','1'],
           ['2','3','4','5','6','7','8','9','0']]

text = list(input())
shivr = []
for i in text:
    for yind, row in enumerate(kvadrat):
        for xind, col in enumerate(row):
            if i == col:
                print(yind + 1,end='')
                print(xind+1, end=' ')
