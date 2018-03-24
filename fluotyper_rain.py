keys = []
keys_x = []
keys_y = []
keys_col = []

def setup():
    size(600, 600)
    background(220)
    textSize(32)
    
    keys.append('a')
    keys_x.append(width/2)
    keys_y.append(0)
    keys_col.append(color(0, 0, 255))
    
    keys.append('b')
    keys_x.append(width/3)
    keys_y.append(-100)
    keys_col.append(color(0, 255, 0))
    
def draw():
    background(220)
    # first element: 'a'
    fill(keys_col[0])
    text(keys[0], keys_x[0], keys_y[0])

    keys_y[0] += 1
    
    if (keys_y[0] > height):
        keys_y[0] = 0
        
        
    # second element: 'b'
    fill(keys_col[1])
    text(keys[1], keys_x[1], keys_y[1])

    keys_y[1] += 1
    
    if (keys_y[1] > height):
        keys_y[1] = 0
        
    fill(255, 0, 0)
    text(str(keys_y[0]), width - 100, 32)
    

def keyTyped():
    print(keys)
    print(keys_x)
    print(keys_y)
    print(keys_col)
     #global ch
    #fill(random(256), random(256), random(256))
    #ch = key
    
