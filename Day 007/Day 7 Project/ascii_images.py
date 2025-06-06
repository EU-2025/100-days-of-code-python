stages = [
    '''
     +---+
     |   |
         |
         |
         |
         |
    =========''',  # 0 errores

    '''
     +---+
     |   |
     O   |
         |
         |
         |
    =========''',  # 1 error

    '''
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========''',  # 2 errores

    '''
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========''',  # 3 errores

    '''
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========''',  # 4 errores

    '''
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========''',  # 5 errores

    '''
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========''',  # 6 errores (game over)
]

game_title = r'''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       '''
