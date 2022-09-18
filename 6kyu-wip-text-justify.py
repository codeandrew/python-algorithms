"""Your task in this Kata is to emulate text justification in monospace font. You will be given a single-lined text and the expected justification width. The longest word will never be greater than this width.

Here are the rules:

Use spaces to fill in the gaps between words.
Each line should contain as many words as possible.
Use '\n' to separate lines.
Gap between words can't differ by more than one space.
Lines should end with a word not a space.
'\n' is not included in the length of a line.
Large gaps go first, then smaller ones ('Lorem--ipsum--dolor--sit-amet,' (2, 2, 2, 1 spaces)).
Last line should not be justified, use only one space between words.
Last line should not contain '\n'
Strings with one word do not need gaps ('somelongword\n').
Example with width=30:

Lorem  ipsum  dolor  sit amet,
consectetur  adipiscing  elit.
Vestibulum    sagittis   dolor
mauris,  at  elementum  ligula
tempor  eget.  In quis rhoncus
nunc,  at  aliquet orci. Fusce
at   dolor   sit   amet  felis
suscipit   tristique.   Nam  a
imperdiet   tellus.  Nulla  eu
vestibulum    urna.    Vivamus
tincidunt  suscipit  enim, nec
ultrices   nisi  volutpat  ac.
Maecenas   sit   amet  lacinia
arcu,  non dictum justo. Donec
sed  quam  vel  risus faucibus
euismod.  Suspendisse  rhoncus
rhoncus  felis  at  fermentum.
Donec lorem magna, ultricies a
nunc    sit    amet,   blandit
fringilla  nunc. In vestibulum
velit    ac    felis   rhoncus
pellentesque. Mauris at tellus
enim.  Aliquam eleifend tempus
dapibus. Pellentesque commodo,
nisi    sit   amet   hendrerit
fringilla,   ante  odio  porta
lacus,   ut   elementum  justo
nulla et dolor.
Also you can always take a look at how justification works in your text editor or directly in HTML (css: text-align: justify).

Have fun :)

"""

"""
v1 
Works but only 80% on final submition tests
"""
def justify(text, width):
    print(text, width)
    print(len(text))
    format = [text[i:i+width].strip() for i in range(0, len(text), width)]
    
    new_format = []
    for i in format:
        if len(i) < width:
            print(f"{i} is less than {width}")
            wordlist = i.split(" ")
            print(wordlist)
            
            i = "  ".join(wordlist)
        new_format.append(i)
            
    string = "\n".join(new_format)
    print(string)
    return string

"""
V2 
"""
def justify(text, width):
    print(f"t :{text}",f"w: {width}")
    print(len(text))
    word_list = text.split(" ")[::-1] #reversed array

    format = []
    for i in range(0, len(text), width):
        print(f"line: {i}")
        
        new_string = ""
        next_word = ""
        
        while len(new_string) <= width+1:
            print('[!] test')   
            print(f"LEN: {len(word_list)}" )
            
            # When word list is out of range
            if len(word_list) == 0 : break
            
            if len(new_string) >= width:
                print('[+] string will be greater than width')
                break
            
            next_word = word_list.pop()
            print(f"next_word :{next_word}")
            print(f'word_list {word_list}')
            new_string += f"{next_word} "
            print(f'new_string {new_string} len {len(new_string)}  \n\n')
            
        
        format.append(new_string)
    print(f"format {format}")



"""
v3
"""
def justify(text, width):
    print(f"t :{text}",f"w: {width}")
    print(len(text))
    word_list = text.split(" ")[::-1] #reversed array

    format = []
    for i in range(0, len(text), width):
        print(f"line: {i}")
        
        new_string = ""
        next_word = ""
        
        while len(new_string) <= width+1:
            print('[!] test')   
            print(f"LEN: {len(word_list)}" )
            
            # When word list is out of range
            if len(word_list) == 0 : break
            
            if len(new_string) >= width:
                print('[+] string will be greater than width')
                break
            
            next_word = word_list.pop()
            print(f"next_word :{next_word}")
            print(f'word_list {word_list}')
            new_string += f"{next_word} "
            print(f'new_string {new_string} len {len(new_string)}  \n\n')
            
        
        format.append(new_string)
    print(f"Format {format}")
    
    
    # WORKING HERE 
    # NEW IDEA SORT STRING PER ARRAY FROM FORMAT TO NEW FORMAT
    new_format = []
    for i in format:
        print(len(i))
        if len(i.strip()) == width:
            
            
        small_list = i.strip().split(" ")
        
        print(small_list)
        
