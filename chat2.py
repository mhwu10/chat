# to reformulate the chat

def read_file(input_file):
    talk = []
    with open(input_file, 'r', encoding = 'utf-8-sig') as f:
        for iline in f:
            talk.append(iline.strip())
    print(talk)
    return talk


def convert(talk):
    name = None # for avoiding crashing
    allen_word_count = 0
    viki_word_count = 0
    allen_sticker_count = 0
    viki_sticker_count = 0
    allen_image_count =0
    viki_image_count =0
    for line in talk:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count += 1
            elif s[2] == '圖片':
                allen_image_count += 1
            else:
                for m in s[2:]:
                    allen_word_count += len(m)
        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_sticker_count += 1
            elif s[2] == '圖片':
                viki_image_count += 1
            else:
                for m in s[2:]:
                    viki_word_count += len (m)
    print('Allen said', allen_word_count, 'words and sent', allen_sticker_count, 'stickers')
    print('Allen sent', allen_sticker_count, 'stickers')
    print('Allen sent', allen_image_count, 'images')
    print('Viki said', viki_word_count, 'words and sent', allen_sticker_count, 'stickers')
    print('Viki sent', viki_sticker_count, 'stickers')
    print('Viki sent', viki_image_count, 'images')


def write_file(output_file, talk):
    with open(output_file, 'w', encoding = 'utf-8') as f:
        for line in talk:
            f.write(line + '\n')
   
            
def main():
    r_input_file = 'LINE-Viki.txt'
    w_output_file = 'output.txt'

    talk = read_file(r_input_file)
    print(talk)
    talk = convert(talk)
    #write_file(w_output_file, talk)
    

main()
