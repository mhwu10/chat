# to reformulate the chat

def read_file(input_file):
    talk = []
    with open(input_file, 'r', encoding = 'utf-8-sig') as f:
        for iline in f:
            talk.append(iline.strip())
    print(talk)
    return talk

def convert(talk):
    new = []
    name = None # for avoiding crashing 
    for line in talk:
        if line == 'Allen' or line == 'Tom':
        #if 'Allen' in oline or 'Tom' in oline:
            name = line
            print(name)
            continue
        print(name, ':', line)
            
        if name: # it means it is true if name is something
            new.append(name + ': ' + line)
    print(new)
    return new

def write_file(output_file, talk):
    with open(output_file, 'w', encoding = 'utf-8') as f:
        for line in talk:
            f.write(line + '\n')
            
def main():
    r_input_file = 'input.txt'
    w_output_file = 'output.txt'

    talk = read_file(r_input_file)
    print(talk)
    talk = convert(talk)
    write_file(w_output_file, talk)
    

main()
