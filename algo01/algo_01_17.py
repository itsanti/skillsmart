# https://skillsmart.ru/algo/lvl1/z75c.html

# string BastShoe(string command)
# command - 'N параметр', 1 <= N <= 5

editor = ''
undo_buff = []
redo_buff = []
undof = False
redof = False
prev = None

def BastShoe(command):
    global editor, undo_buff, redo_buff, undof, redof, prev
    
    if ' ' in command:
        N, s = command.split(' ', 1)
        if N.isdigit():
            N = int(N)
        else:
            return editor
    elif command.isdigit():
        N, s = int(command), ''
    else:
        return editor
        
    if N == 1:
        if not undof:
            if prev == 4 and not redof:
                undo_buff = []
                redo_buff = []
            undo_buff.append('2 ' + str(len(s)))
        editor += s
    elif N == 2:
        if s.isdigit():
            s = int(s)
            if s > len(editor):
                s = len(editor)
            if not undof:
                if prev == 4 and not redof:
                    undo_buff = []
                    redo_buff = []
                undo_buff.append('1 ' + editor[len(editor) - s:])
            editor = editor[:-s]
    elif N == 3:
        if s.isdigit():
            s = int(s)
            return editor[s] if s < len(editor) else ''
    elif N == 4:
        if len(undo_buff) > 0:
            undof = True
            command = undo_buff.pop()
            nu, su = command.split(' ', 1)
            if nu == '2':
                redo_buff.append('1 ' + editor[len(editor) - int(su):])
            else:
                redo_buff.append('2 ' + str(len(su)))
            BastShoe(command)
            undof = False
    elif N == 5:
        if len(redo_buff) > 0:
            redof = True
            command = redo_buff.pop()
            BastShoe(command)
            redof = False

    prev = N
    return editor
