import pygame, math, keyboard, time, random, threading, json

pygame.init()

pygame.mixer.init()

#Initializing Color variables

black = (0, 0, 0)
purple_bg = (68, 110, 87)  #(255, 0, 0)
purple_walls = (255, 175, 230)#(50, 11, 34)  #(0, 255, 0)
purple_level = (0, 255, 200)  #(81, 60, 172)#(0, 0, 255)
white = (255, 255, 255)
bg_color_start_min = (160, 140, 111)
bg_color_start = (160, 160, 160)
bg_color_start_max = (230, 180, 180)
font_color = (0, 0, 0)

#Initializing Screen Args

og_w = 1280
og_h = 720

min_w = og_w * .5
min_h = og_h * .5

#Initializing the screen and clock variables

# screen = pygame.display.set_mode((og_w, og_h), pygame.FULLSCREEN | pygame.DOUBLEBUF)
screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN | pygame.DOUBLEBUF)

clock = pygame.time.Clock()

game_fps = 60

fps = 60
delta_time = 1 / fps

fps_ratio = game_fps / fps

#Font Path

doto_font_path = 'C:/Users/nilit/OneDrive/Documents/FBLA Game/Doto Font/Doto-SemiBold.ttf'

#Sound Path

menu_music_path = 'C:/Users/nilit/OneDrive/Documents/FBLA Game/europa-tecnosine.mp3'
ingame_music_path = 'C:/Users/nilit/OneDrive/Documents/FBLA Game/digital-dreams.mp3'

single_bounce_path = 'C:/Users/nilit/OneDrive/Documents/FBLA Game/single_bounce.mp3'

click_path = 'C:/Users/nilit/OneDrive/Documents/FBLA Game/click.mp3'

#Levels Images

levels_image = {
    'Level 1' : pygame.image.load('C:/Users/nilit/OneDrive/Documents/FBLA Game/level_1.jpg'),
    'Level 2' : pygame.image.load('C:/Users/nilit/OneDrive/Documents/FBLA Game/level_2.jpg'),
    'Level 3' : pygame.image.load('C:/Users/nilit/OneDrive/Documents/FBLA Game/level_3.jpg'),
    'Level 4' : pygame.image.load('C:/Users/nilit/OneDrive/Documents/FBLA Game/level_4.jpg'),
    'Level 5' : pygame.image.load('C:/Users/nilit/OneDrive/Documents/FBLA Game/level_5.jpg'),
    'Level 6' : pygame.image.load('C:/Users/nilit/OneDrive/Documents/FBLA Game/level_6.jpg'),
    'Level 7' : pygame.image.load('C:/Users/nilit/OneDrive/Documents/FBLA Game/level_7.jpg'),
    'Level 8' : pygame.image.load('C:/Users/nilit/OneDrive/Documents/FBLA Game/level_8.jpg'),
    'Level 9' : pygame.image.load('C:/Users/nilit/OneDrive/Documents/FBLA Game/level_9.jpg')
}

#Sound effects Load

sfx = {
        'bounce' : pygame.mixer.Sound(single_bounce_path)
}

#Interface Sounds

interface_sound = {
        'click' : pygame.mixer.Sound(click_path)
}


#Keybinds

typing_keybinds = {
    'a': pygame.K_a,
    'b': pygame.K_b,
    'c': pygame.K_c,
    'd': pygame.K_d,
    'e': pygame.K_e,
    'f': pygame.K_f,
    'g': pygame.K_g,
    'h': pygame.K_h,
    'i': pygame.K_i,
    'j': pygame.K_j,
    'k': pygame.K_k,
    'l': pygame.K_l,
    'm': pygame.K_m,
    'n': pygame.K_n,
    'o': pygame.K_o,
    'p': pygame.K_p,
    'q': pygame.K_q,
    'r': pygame.K_r,
    's': pygame.K_s,
    't': pygame.K_t,
    'u': pygame.K_u,
    'v': pygame.K_v,
    'w': pygame.K_w,
    'x': pygame.K_x,
    'y': pygame.K_y,
    'z': pygame.K_z,
    '0': pygame.K_0,
    '1': pygame.K_1,
    '2': pygame.K_2,
    '3': pygame.K_3,
    '4': pygame.K_4,
    '5': pygame.K_5,
    '6': pygame.K_6,
    '7': pygame.K_7,
    '8': pygame.K_8,
    '9': pygame.K_9
}

posible_keybinds = {
    'a': pygame.K_a,
    'b': pygame.K_b,
    'c': pygame.K_c,
    'd': pygame.K_d,
    'e': pygame.K_e,
    'f': pygame.K_f,
    'g': pygame.K_g,
    'h': pygame.K_h,
    'i': pygame.K_i,
    'j': pygame.K_j,
    'k': pygame.K_k,
    'l': pygame.K_l,
    'm': pygame.K_m,
    'n': pygame.K_n,
    'o': pygame.K_o,
    'p': pygame.K_p,
    'q': pygame.K_q,
    'r': pygame.K_r,
    's': pygame.K_s,
    't': pygame.K_t,
    'u': pygame.K_u,
    'v': pygame.K_v,
    'w': pygame.K_w,
    'x': pygame.K_x,
    'y': pygame.K_y,
    'z': pygame.K_z,
    '0': pygame.K_0,
    '1': pygame.K_1,
    '2': pygame.K_2,
    '3': pygame.K_3,
    '4': pygame.K_4,
    '5': pygame.K_5,
    '6': pygame.K_6,
    '7': pygame.K_7,
    '8': pygame.K_8,
    '9': pygame.K_9,
    'space': pygame.K_SPACE,
    'left_shift': pygame.K_LSHIFT,
    'left_arrow': pygame.K_LEFT,
    'right_arrow': pygame.K_RIGHT,
    'down_arrow': pygame.K_DOWN,
    'up_arrow': pygame.K_UP,
    'enter': pygame.K_RETURN,
    'escape' : pygame.K_ESCAPE,
    'unbinded': pygame.K_UNKNOWN
}

actual_keybinds = {
    'gravity_switch': [posible_keybinds['space'], 'space'],
    'ability_slot_1': [posible_keybinds['2'], '2'],
    'ability_slot_2': [posible_keybinds['3'], '3'],
    'ability_slot_3': [posible_keybinds['4'], '4'],
    'ability_slot_4': [posible_keybinds['5'], '5'],
    'ability_slot_5': [posible_keybinds['6'], '6'],
    'ability_slot_up': [posible_keybinds['right_arrow'], 'right_arrow'],
    'ability_slot_down': [posible_keybinds['left_arrow'], 'left_arrow'],
    'ability_activate': [posible_keybinds['enter'], 'enter'],
    'grid_y_0': [posible_keybinds['1'], '1'],
    'grid_y_1': [posible_keybinds['q'], 'q'],
    'grid_y_2': [posible_keybinds['a'], 'a'],
    'grid_y_3': [posible_keybinds['z'], 'z'],
    'grid_x_0': [posible_keybinds['x'], 'x'],
    'grid_x_1': [posible_keybinds['c'], 'c'],
    'grid_x_2': [posible_keybinds['v'], 'v'],
    'grid_x_3': [posible_keybinds['b'], 'b'],
    'grid_x_4': [posible_keybinds['n'], 'n'],
    'grid_x_5': [posible_keybinds['m'], 'm']
}

main_keybinds = ['gravity_switch']

ability_keybinds = ['ability_slot_1', 'ability_slot_2', 'ability_slot_3', 'ability_slot_4', 'ability_slot_5']

ability_direccion_keybinds = ['ability_slot_up', 'ability_slot_down']
ability_activation = ['ability_activate']

grid_y = ['grid_y_0', 'grid_y_1', 'grid_y_2', 'grid_y_3']
grid_x = ['grid_x_0', 'grid_x_1', 'grid_x_2', 'grid_x_3', 'grid_x_4', 'grid_x_5']

possible_abilities = {
    'blocks': {
        0: 'solid',
        1: 'bouncy_1',
        2: 'planet'
    },
    'change_gravity': {
        0: 'invert',
        1: 'zero_gravity',
        2: 'side_ways',
        3: 'gravity_up',
        4: 'gravity_down'
    },
    'wind': {
        0: 'swirl',
        1: 'inverse',
        2: 'swirl_left',
        3: 'swirl_right'
    }
}


for key in possible_abilities:
    for x in range(len(possible_abilities[key])):
        actual_keybinds[f"{possible_abilities[key][x]}"] = [posible_keybinds['unbinded'], 'unbinded']

abilities_txt = {
        'gravity_switch' : 'Gravity Switch',
        'ability_slot_1' : 'Ability Slot 1',
        'ability_slot_2' : 'Ability Slot 2',
        'ability_slot_3' : 'Ability Slot 3',
        'ability_slot_4' : 'Ability Slot 4',
        'ability_slot_5' : 'Ability Slot 5',
        'ability_slot_up' : 'Ability Slot Up',
        'ability_slot_down' : 'Ability Slot Down',
        'ability_activate' : 'Activate Ability',
        'grid_y_0' : 'Grid Y 0',
        'grid_y_1' : 'Grid Y 1',
        'grid_y_2' : 'Grid Y 2',
        'grid_y_3' : 'Grid Y 3',
        'grid_x_0' : 'Grid X 0',
        'grid_x_1' : 'Grid X 1',
        'grid_x_2' : 'Grid X 2',
        'grid_x_3' : 'Grid X 3',
        'grid_x_4' : 'Grid X 4',
        'grid_x_5' : 'Grid X 5',
        'solid' : 'Solid Block',
        'bouncy_1' : 'Bouncy Block',
        'invert' : 'Invert Gravity',
        'zero_gravity' : 'Zero Gravity',
        'side_ways' : 'Side Ways Gravity',
        'gravity_up' : 'Gravity Increment',
        'gravity_down' : 'Gravity Decrement',
        'swirl_left' : 'Blow Air Left',
        'swirl_right' : 'Blow Air Right'
}

#Main Game Display Functions

def reset_fbla_file():
    
    #DONT TOUCH THIS FUNCTION
    
    with open('fbla_game_save_files.json', 'r') as file:
        
        data = json.load(file)
        
    data['Save Files']['Save File 1'] = 'TBS'
    data['Save Files']['Save File 2'] = 'TBS'
    data['Save Files']['Save File 3'] = 'TBS'
    data['Save Files']['Test File'] = data['Save Files']['Reset File']
    
    with open('fbla_game_save_files.json', 'w') as file:
        
        json.dump(data, file, indent=4)

def Background_Animation():
    global main_x_val, secondary_x_val, angles_cycles, current_angles, current_distance_for_lines
    
    if main_x_val < 2500:
        main_x_val += 1
    else:
        main_x_val = -2000
    if secondary_x_val < 2500:
        secondary_x_val += 1
    else:
        secondary_x_val = -2000
        
    main_graph = getting_graph(main_x_val)
    secondary_graph = getting_graph(secondary_x_val)
    
    # for i in range(len(current_angles) - 1):
        # if angles_cycles[i] == 0 and current_angles[i] < angles_max[i]:
            # current_angles[i] += .5
        # else:
            # angles_cycles[i] = 1
        # if angles_cycles[i] == 1 and current_angles[i] > angles_min[i]:
            # current_angles[i] -= .5
        # else:
            # angles_cycles[i] = 0
    
    color_cycle = [(111, 111, 111), (120, 120, 120), (127, 127, 127), (134, 134, 134), (140, 140, 140)]
    cy = 0
    
    for p in triangles:
        point1 = main_graph[p[0]]
        point2 = main_graph[p[1]]
        point3 = main_graph[p[2]]
        pygame.draw.polygon(screen, color_cycle[cy], (point1, point2, point3))
        pygame.draw.polygon(screen, white, (point1, point2, point3), 2)
        point1 = secondary_graph[p[0]]
        point2 = secondary_graph[p[1]]
        point3 = secondary_graph[p[2]]
        pygame.draw.polygon(screen, color_cycle[cy], (point1, point2, point3))
        pygame.draw.polygon(screen, white, (point1, point2, point3), 2)
        cy += 1
        if cy > 4:
            cy = 0
            
    if main_x_val < secondary_x_val:
        extra_trigs = [
            [main_graph['point_44'], secondary_graph['point_25'], secondary_graph['point_12']],
            [main_graph['point_43'], main_graph['point_44'], secondary_graph['point_12']],
            [main_graph['point_43'], secondary_graph['point_25'], secondary_graph['point_14']],
            [main_graph['point_43'], secondary_graph['point_14'], main_graph['point_42']],
            [main_graph['point_42'], secondary_graph['point_14'], secondary_graph['point_15']],
            [main_graph['point_42'], secondary_graph['point_23'], secondary_graph['point_15']],
            [main_graph['point_44'], secondary_graph['point_12'], secondary_graph['point_9']],
            [main_graph['point_42'], main_graph['point_41'], secondary_graph['point_15']],
            [main_graph['point_41'], secondary_graph['point_23'], secondary_graph['point_15']]
        ]
        for p in extra_trigs:
            pygame.draw.polygon(screen, color_cycle[cy], p)
            pygame.draw.polygon(screen, white, p, 2)
            cy += 1
            if cy > 4:
                cy = 0
                
    if main_x_val > secondary_x_val:
        extra_trigs = [
            [secondary_graph['point_44'], main_graph['point_25'], main_graph['point_12']],
            [secondary_graph['point_43'], secondary_graph['point_44'], main_graph['point_12']],
            [secondary_graph['point_43'], main_graph['point_25'], main_graph['point_14']],
            [secondary_graph['point_43'], main_graph['point_14'], secondary_graph['point_42']],
            [secondary_graph['point_42'], main_graph['point_14'], main_graph['point_15']],
            [secondary_graph['point_42'], main_graph['point_23'], main_graph['point_15']],
            [secondary_graph['point_44'], main_graph['point_12'], main_graph['point_9']],
            [secondary_graph['point_42'], secondary_graph['point_41'], main_graph['point_15']],
            [secondary_graph['point_41'], main_graph['point_23'], main_graph['point_15']]
        ]
        for p in extra_trigs:
            pygame.draw.polygon(screen, color_cycle[cy], p)
            pygame.draw.polygon(screen, white, p, 2)
            cy += 1
            if cy > 4:
                cy = 0
        
def Start_Screen_Display():
    
    global bg_color_start, cycle
    
    screen_sur = pygame.Surface((pygame.Surface.get_width(screen), pygame.Surface.get_height(screen)), pygame.SRCALPHA)
    t = 255
    screen_sur.fill((0, 0, 0, 255))
    
    while True:
    
        ratio()
        
        setting_audio('start')
        
        
        if bg_color_start[0] < bg_color_start_max[0] and cycle == 0:
            bg_color_start = (bg_color_start[0] + 1, bg_color_start[0] + 1, bg_color_start[0] + 1)
        else:
            cycle = 1
            
        if bg_color_start[0] > bg_color_start_min[0] and cycle == 1:
            bg_color_start = (bg_color_start[0] - 1, bg_color_start[0] - 1, bg_color_start[0] - 1)
        else:
            cycle = 0
        
        game_title_txt = doto_font_1(int(110 * h_ratio)).render('Path of Momentum', False, black)
        
        start_with_any_button_txt = doto_font_1(int(38 * h_ratio)).render('Press anything to continue', False, bg_color_start)
        
        screen.fill((80, 80, 80))
        
        Background_Animation()
        
        screen.blit(game_title_txt, game_title_txt.get_rect(center=(pygame.Surface.get_width(screen) // 2, 200 * h_ratio)))
        screen.blit(start_with_any_button_txt, start_with_any_button_txt.get_rect(center=(pygame.Surface.get_width(screen) // 2, 695 * h_ratio)))
        
        if t > 0:
            screen.blit(screen_sur, (0,0))
            t -= 5
            screen_sur.fill((0, 0, 0, int(t)))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return False
                if t <= 0:
                    interface_sound['click'].play()
                    return True
            if event.type == pygame.MOUSEBUTTONDOWN and t <= 0:
                if event.button == 1:
                    interface_sound['click'].play()
                    return True
                
        pygame.display.flip()
        
        clock.tick(60)

def Choose_Your_Save_File_Screen_Display():
    global loaded_file
    
    with open('fbla_game_save_files.json', 'r') as file:
        
        data = json.load(file)
    
    while True:
        
        ratio()
        
        setting_audio('start')
        
        save_file_rect_sur = pygame.Surface((600, 150), pygame.SRCALPHA)
        save_file_rect_sur.fill((0, 0, 0, 0))
        
        screen.fill((80, 80, 80))
        
        Background_Animation()
        
        choose_your_file_txt = doto_font_1(int(90 * h_ratio)).render('Choose your save file', False, black)
        
        screen.blit(choose_your_file_txt, choose_your_file_txt.get_rect(center=(pygame.Surface.get_width(screen) // 2, 100 * h_ratio)))
        
        new_file_txt = doto_font_1(int(40 * h_ratio)).render('Create New File', False, white)
        
        lvl_txt = doto_font_1(int(48 * h_ratio)).render('LVL', False, white)
            
        first_save_file_button = pygame.Rect(pygame.Surface.get_width(screen) // 2 - ((495//2) * w_ratio), 300 * h_ratio - (150//2), 495 * w_ratio, 125  * h_ratio)    
        second_save_file_button = pygame.Rect(pygame.Surface.get_width(screen) // 2 - ((495//2) * w_ratio), 460 * h_ratio - (150//2), 495 * w_ratio, 125 * h_ratio)
        third_save_file_button = pygame.Rect(pygame.Surface.get_width(screen) // 2 - ((495//2) * w_ratio), 620 * h_ratio - (150//2), 495 * w_ratio, 125 * h_ratio)
        
        test_txt = doto_font_1(int(36 * h_ratio)).render('Test', False, white)
        
        test_save_file_button = pygame.Rect(10 * w_ratio, 670 * h_ratio, 200 * w_ratio, 40 * h_ratio)
        test_save_file_sur = pygame.Surface((200 * w_ratio, 40 * h_ratio), pygame.SRCALPHA)
        test_save_file_sur.fill((0, 0, 0, 0))
        
        pygame.draw.rect(test_save_file_sur, (160, 160, 160, 130), test_save_file_sur.get_rect(center=(pygame.Surface.get_width(test_save_file_sur) // 2, pygame.Surface.get_height(test_save_file_sur) // 2)), border_radius=30)
        pygame.draw.rect(test_save_file_sur, (255, 255, 255, 255), test_save_file_sur.get_rect(center=(pygame.Surface.get_width(test_save_file_sur) // 2, pygame.Surface.get_height(test_save_file_sur) // 2)), int(2 * w_ratio), border_radius=30)
        
        screen.blit(test_save_file_sur, test_save_file_sur.get_rect(center=(110 * w_ratio, 690 * h_ratio)))
        screen.blit(test_txt, test_txt.get_rect(center=(110 * w_ratio, 690 * h_ratio)))
        
        #pygame.draw.rect(screen, (255, 0, 0), test_save_file_button)
        
        pygame.draw.rect(save_file_rect_sur, (160, 160, 160, 130), save_file_rect_sur.get_rect(), border_radius=20)
        pygame.draw.rect(save_file_rect_sur, (160, 160, 160, 130), save_file_rect_sur.get_rect(), border_radius=20)
        pygame.draw.rect(save_file_rect_sur, (160, 160, 160, 130), save_file_rect_sur.get_rect(), border_radius=20)
        
        screen.blit(save_file_rect_sur, save_file_rect_sur.get_rect(center=(pygame.Surface.get_width(screen) // 2, 300 * h_ratio)))
        screen.blit(save_file_rect_sur, save_file_rect_sur.get_rect(center=(pygame.Surface.get_width(screen) // 2, 460 * h_ratio)))
        screen.blit(save_file_rect_sur, save_file_rect_sur.get_rect(center=(pygame.Surface.get_width(screen) // 2, 620 * h_ratio)))   
        
        if data['Save Files']['Save File 1'] == 'TBS':
        
            screen.blit(new_file_txt, new_file_txt.get_rect(center=(pygame.Surface.get_width(screen) // 2, 300 * h_ratio)))
            
        else:
            
            name_txt = doto_font_1(int(36 * h_ratio)).render(f"{data['Save Files']['Save File 1']['User Preference']['Name']}", False, white)
            screen.blit(name_txt, name_txt.get_rect(center=(pygame.Surface.get_width(screen) // 2, (300 - 40) * h_ratio)))
            #screen.blit(lvl_txt, lvl_txt.get_rect(center=((pygame.Surface.get_width(screen) - 450) // 2, (300) * h_ratio)))
            
            lvl_num_txt = doto_font_1(int(40 * h_ratio)).render(f"{data['Save Files']['Save File 1']['User Account']['Exp Level']}", False, white)
            
            exp_needed_txt = doto_font_1(int(24 * h_ratio)).render(f"{data['Save Files']['Save File 1']['User Account']['Exp Amount']} / {data['Save Files']['Exp Per Level'][f'{data['Save Files']['Save File 1']['User Account']['Exp Level']}'][1]}", False, black)
            
            stars_num_txt = doto_font_1(int(46 * h_ratio)).render(f"{data['Save Files']['Save File 1']['User Account']['Stars']}", False, white)
            
            stars_txt = doto_font_1(int(40 * h_ratio)).render('STARS', False, white)
            
            exp_bar = pygame.Surface((400, 28), pygame.SRCALPHA)
            
            exp_progress_bar = pygame.Surface((400 * (data['Save Files']['Save File 1']['User Account']['Exp Amount'] / data['Save Files']['Exp Per Level'][f"{data['Save Files']['Save File 1']['User Account']['Exp Level']}"][1]), 28), pygame.SRCALPHA)
            
            
            exp_progress_bar.fill(white)
            exp_bar.fill((0, 0, 0, 0))
            
            pygame.draw.rect(exp_bar, white, exp_bar.get_rect(), 2)
            
            #screen.blit(lvl_num_txt, lvl_num_txt.get_rect(center=((pygame.Surface.get_width(screen) - 310) // 2, (300) * h_ratio)))
            screen.blit(stars_num_txt, stars_num_txt.get_rect(topleft=((pygame.Surface.get_width(screen) - 205) // 2, (300 + 12) * h_ratio)))
            screen.blit(stars_txt, stars_txt.get_rect(center=((pygame.Surface.get_width(screen) - 400) // 2, (300 + 40) * h_ratio)))
            #screen.blit(exp_bar, exp_bar.get_rect(center=((pygame.Surface.get_width(screen) + 150) // 2, (300) * h_ratio)))
            #screen.blit(exp_progress_bar, exp_progress_bar.get_rect(topleft=((pygame.Surface.get_width(screen) - 248) // 2, (289) * h_ratio)))
            #screen.blit(exp_needed_txt, exp_needed_txt.get_rect(center=((pygame.Surface.get_width(screen) + 150) // 2, (300) * h_ratio)))
            
        if data['Save Files']['Save File 2'] == 'TBS':
            
            screen.blit(new_file_txt, new_file_txt.get_rect(center=(pygame.Surface.get_width(screen) // 2, 460 * h_ratio)))
            
        else:
            
            name_txt = doto_font_1(int(36 * h_ratio)).render(f"{data['Save Files']['Save File 2']['User Preference']['Name']}", False, white)
            screen.blit(name_txt, name_txt.get_rect(center=(pygame.Surface.get_width(screen) // 2, (460 - 40) * h_ratio)))
            #screen.blit(lvl_txt, lvl_txt.get_rect(center=((pygame.Surface.get_width(screen) - 450) // 2, (460) * h_ratio)))
            
            lvl_num_txt = doto_font_1(int(40 * h_ratio)).render(f"{data['Save Files']['Save File 1']['User Account']['Exp Level']}", False, white)
            
            exp_needed_txt = doto_font_1(int(24 * h_ratio)).render(f"{data['Save Files']['Save File 1']['User Account']['Exp Amount']} / {data['Save Files']['Exp Per Level'][f"{data['Save Files']['Save File 1']['User Account']['Exp Level']}"][1]}", False, black)
            
            stars_num_txt = doto_font_1(int(46 * h_ratio)).render(f"{data['Save Files']['Save File 1']['User Account']['Stars']}", False, white)
            
            stars_txt = doto_font_1(int(40 * h_ratio)).render('STARS', False, white)
            
            exp_bar = pygame.Surface((400, 28), pygame.SRCALPHA)
            
            exp_progress_bar = pygame.Surface((400 * (data['Save Files']['Save File 2']['User Account']['Exp Amount'] / data['Save Files']['Exp Per Level'][f'{data['Save Files']['Save File 2']['User Account']['Exp Level']}'][1]), 28), pygame.SRCALPHA)
            
            
            exp_progress_bar.fill(white)
            exp_bar.fill((0, 0, 0, 0))
            
            pygame.draw.rect(exp_bar, white, exp_bar.get_rect(), 2)
            
            #screen.blit(lvl_num_txt, lvl_num_txt.get_rect(center=((pygame.Surface.get_width(screen) - 310) // 2, (460) * h_ratio)))
            screen.blit(stars_num_txt, stars_num_txt.get_rect(topleft=((pygame.Surface.get_width(screen) - 205) // 2, (460 + 12) * h_ratio)))
            screen.blit(stars_txt, stars_txt.get_rect(center=((pygame.Surface.get_width(screen) - 400) // 2, (460 + 40) * h_ratio)))
            #screen.blit(exp_bar, exp_bar.get_rect(center=((pygame.Surface.get_width(screen) + 150) // 2, (460) * h_ratio)))
            #screen.blit(exp_progress_bar, exp_progress_bar.get_rect(topleft=((pygame.Surface.get_width(screen) - 248) // 2, (460 - 11) * h_ratio)))
            #screen.blit(exp_needed_txt, exp_needed_txt.get_rect(center=((pygame.Surface.get_width(screen) + 150) // 2, (460) * h_ratio)))
        
        if data['Save Files']['Save File 3'] == 'TBS':
            
            screen.blit(new_file_txt, new_file_txt.get_rect(center=(pygame.Surface.get_width(screen) // 2, 620 * h_ratio)))
        
        else:
        
            name_txt = doto_font_1(int(36 * h_ratio)).render(f"{data['Save Files']['Save File 3']['User Preference']['Name']}", False, white)
            screen.blit(name_txt, name_txt.get_rect(center=(pygame.Surface.get_width(screen) // 2, (620 - 40) * h_ratio)))
            #screen.blit(lvl_txt, lvl_txt.get_rect(center=((pygame.Surface.get_width(screen) - 450) // 2, (620) * h_ratio)))
            
            lvl_num_txt = doto_font_1(int(40 * h_ratio)).render(f"{data['Save Files']['Save File 1']['User Account']['Exp Level']}", False, white)
            
            exp_needed_txt = doto_font_1(int(24 * h_ratio)).render(f"{data['Save Files']['Save File 1']['User Account']['Exp Amount']} / {data['Save Files']['Exp Per Level'][f"{data['Save Files']['Save File 1']['User Account']['Exp Level']}"][1]}", False, black)
            
            stars_num_txt = doto_font_1(int(46 * h_ratio)).render(f"{data['Save Files']['Save File 1']['User Account']['Stars']}", False, white)
            
            stars_txt = doto_font_1(int(40 * h_ratio)).render('STARS', False, white)
            
            exp_bar = pygame.Surface((400, 28), pygame.SRCALPHA)
            
            exp_progress_bar = pygame.Surface((400 * (data['Save Files']['Save File 3']['User Account']['Exp Amount'] / data['Save Files']['Exp Per Level'][f"{data['Save Files']['Save File 3']['User Account']['Exp Level']}"][1]), 28), pygame.SRCALPHA)
            
            
            exp_progress_bar.fill(white)
            exp_bar.fill((0, 0, 0, 0))
            
            pygame.draw.rect(exp_bar, white, exp_bar.get_rect(), 2)
            
            #screen.blit(lvl_num_txt, lvl_num_txt.get_rect(center=((pygame.Surface.get_width(screen) - 310) // 2, (620) * h_ratio)))
            screen.blit(stars_num_txt, stars_num_txt.get_rect(topleft=((pygame.Surface.get_width(screen) - 205) // 2, (620 + 12) * h_ratio)))
            screen.blit(stars_txt, stars_txt.get_rect(center=((pygame.Surface.get_width(screen) - 400) // 2, (620 + 40) * h_ratio)))
            #screen.blit(exp_bar, exp_bar.get_rect(center=((pygame.Surface.get_width(screen) + 150) // 2, (620) * h_ratio)))
            #screen.blit(exp_progress_bar, exp_progress_bar.get_rect(topleft=((pygame.Surface.get_width(screen) - 248) // 2, (620 - 11) * h_ratio)))
            #screen.blit(exp_needed_txt, exp_needed_txt.get_rect(center=((pygame.Surface.get_width(screen) + 150) // 2, (620) * h_ratio)))
            
        pygame.draw.rect(screen, (240, 240, 240), save_file_rect_sur.get_rect(center=(pygame.Surface.get_width(screen) // 2, 300 * h_ratio)), 2, border_radius=20)
        pygame.draw.rect(screen, (240, 240, 240), save_file_rect_sur.get_rect(center=(pygame.Surface.get_width(screen) // 2, 460 * h_ratio)), 2, border_radius=20)
        pygame.draw.rect(screen, (240, 240, 240), save_file_rect_sur.get_rect(center=(pygame.Surface.get_width(screen) // 2, 620 * h_ratio)), 2, border_radius=20)
        
        
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if first_save_file_button.collidepoint(event.pos):
                        interface_sound['click'].play()
                        loaded_file = 'Save File 1'
                        creating_file(loaded_file)
                        loading_keybinds()
                        return True
                    if second_save_file_button.collidepoint(event.pos):
                        interface_sound['click'].play()
                        loaded_file = 'Save File 2'
                        creating_file(loaded_file)
                        loading_keybinds()
                        return True
                    if third_save_file_button.collidepoint(event.pos):
                        interface_sound['click'].play()
                        loaded_file = 'Save File 3'
                        creating_file(loaded_file)
                        loading_keybinds()
                        return True
                    if test_save_file_button.collidepoint(event.pos):
                        interface_sound['click'].play()
                        loaded_file = 'Test File'
                        loading_keybinds()
                        return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return False
                
        pygame.display.flip()
        
        clock.tick(60)

def creating_file(target):
    
    with open('fbla_game_save_files.json', 'r') as file:
        
        data = json.load(file)
    
    if data['Save Files'][target] == 'TBS':
        
        data['Save Files'][target] = data['Save Files']['Reset File']
        
        with open('fbla_game_save_files.json', 'w') as file:
            
            json.dump(data, file, indent=4)
        
        return True
        
def loading_keybinds():
    global actual_keybinds
    
    with open('fbla_game_save_files.json', 'r') as file:
        
        data = json.load(file)
        
    for key in actual_keybinds:
        
        actual_keybinds[key] = [posible_keybinds[data['Save Files'][loaded_file]['Controls'][key]], data['Save Files'][loaded_file]['Controls'][key]]
    
def write_your_username():
    
    name = []
    
    with open('fbla_game_save_files.json', 'r') as file:
        
        data = json.load(file)
    
    if data['Save Files'][loaded_file]['User Preference']['Name'] == 'player_00000001':
        
        while True:
            
            screen.fill((80, 80, 80))
            
            Background_Animation()
            
            enter_your_name_txt = doto_font_1(int(63 * h_ratio)).render('Enter your Username', False, black)
            
            name_overlay = doto_font_1(int(38 * h_ratio)).render(f"{''.join(name)}", False, black)
            
            name_overlay_sur = pygame.Surface((500, 150), pygame.SRCALPHA)
            
            name_overlay_sur.fill((180, 180, 180, 120))
            
            screen.blit(enter_your_name_txt, enter_your_name_txt.get_rect(center=(pygame.Surface.get_width(screen) // 2, 150)))
            
            screen.blit(name_overlay_sur, name_overlay_sur.get_rect(center=(pygame.Surface.get_width(screen) // 2, pygame.Surface.get_height(screen) // 2)))
            
            screen.blit(name_overlay, name_overlay.get_rect(center=(pygame.Surface.get_width(screen) // 2, pygame.Surface.get_height(screen) // 2)))
            
            pygame.draw.rect(screen, white, name_overlay_sur.get_rect(center=(pygame.Surface.get_width(screen) // 2, pygame.Surface.get_height(screen) // 2)), 2)
            
            writing_the_username_rules = doto_font_1(int(45 * h_ratio)).render('No especial characters.\nOnly Letters and Number.\nFor capital, press shift\nand the last letter will\nbe capitalized.', False, black)
            
            screen.blit(writing_the_username_rules, writing_the_username_rules.get_rect(center=(pygame.Surface.get_width(writing_the_username_rules), 680)))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass
                if event.type == pygame.KEYDOWN:
                    for key in typing_keybinds:
                        if event.key == typing_keybinds[key] and len(name) < 10:
                            name.append(key)
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        return False
                    if event.key == pygame.K_RETURN:
                        with open('fbla_game_save_files.json', 'r') as file:
            
                            data = json.load(file)
                            
                        data['Save Files'][loaded_file]['User Preference']['Name'] = ''.join(name)
                        
                        with open('fbla_game_save_files.json', 'w') as file:
            
                            json.dump(data, file, indent=4)
                        return True
                    if event.key == pygame.K_BACKSPACE:
                        if len(name) > 0:
                            del name[len(name) - 1]
                    if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        if len(name) > 0:
                            name[len(name) - 1] = name[len(name) - 1].upper()
                    if event.key == pygame.K_SPACE and len(name) < 10:
                        name.append(' ')
                        
            pygame.display.flip()
            
            clock.tick(60)
        
def Main_Menu():
    global selected_level, grid, main
    
    selected = 'Levels'
    scroll = 0
    holding = [False, '', 0, 0]
    all_controls_surfaces = {}
    key_index = 0
    for key in abilities_txt:
        all_controls_surfaces[key] = [doto_font_1(int(30 * h_ratio)).render(abilities_txt[key], False, (0, 0, 0, 255)), key_index, doto_font_1(int(20 * h_ratio)).render(actual_keybinds[key][1].upper(), False, black)]
        key_index += 1
    changing = [False, 'key']
    
    listening_txt = ['Listening for key.  ', 'Listening for key.. ', 'Listening for key...']
    counter_txt = 0
    
    #Loading Settings Assets
    
    settings_txt = doto_font_1(int(98 * h_ratio)).render('Settings', False, font_color)
    audio_txt = doto_font_1(int(75 * h_ratio)).render('Audio', False, font_color)
    master_volume_txt = doto_font_1(int(51 * h_ratio)).render('Master Volume', False, font_color)
    sfx_volume_txt = doto_font_1(int(51 * h_ratio)).render('SFX Volume', False, font_color)
    music_volume_txt = doto_font_1(int(51 * h_ratio)).render('Music Volume', False, font_color)
    interface_volume_txt = doto_font_1(int(51 * h_ratio)).render('Interface Volume', False, font_color)
    slider_sur = pygame.Surface((575 * w_ratio, 50 * h_ratio), pygame.SRCALPHA)
    slider_sur.fill((0, 0, 0, 0))
    slider_diamond_sur = pygame.Surface((50 * w_ratio, 50 * h_ratio), pygame.SRCALPHA)
    slider_diamond_sur.fill((0, 191, 255, 255))
    controls_txt = doto_font_1(int(75 * h_ratio)).render('Controls', False, font_color)
    keybind_txt = doto_font_1(int(45 * h_ratio)).render('Keybinds', False, font_color)
    key_txt = doto_font_1(int(45 * h_ratio)).render('Key', False, font_color)
    
    stars_txt = doto_font_1(int(70 * h_ratio)).render('Stars', False, font_color)
    
    #Loading How to Play Assets
    
    how_to_play_txt = doto_font_1(int(75 * h_ratio)).render('How to Play', False, font_color)
    
    all_instructions = {
        0 : doto_font_1(int(26 * h_ratio)).render('Make the ball reach the objective by\nchanging the envieroment with your\nabilities.', False, font_color),
        1 : doto_font_1(int(26 * h_ratio)).render('The grid is divided\nin a 6 (Width) by 4\n(Height) and is\ncontroled with your\nkeyboard', False, font_color)
    }
    
    with open('fbla_game_save_files.json', 'r') as file:
            
        data = json.load(file)
    
    while True:
        
        ratio()
        
        setting_audio()
        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        setting_sur = pygame.Surface((pygame.Surface.get_width(screen) // 2, 3000), pygame.SRCALPHA)
        setting_sur.fill((0, 0, 0, 0))
        
        screen.fill((80, 80, 80))
            
        Background_Animation()
        
        name_txt = doto_font_1(int(98 * h_ratio)).render(f"{data['Save Files'][loaded_file]['User Preference']['Name']}", False, black)
        levels_txt = doto_font_1(int(68 * h_ratio)).render('Levels', False, black)
        setting_txt = doto_font_1(int(68 * h_ratio)).render('Setting', False, black)
        how_to_play_txt = doto_font_1(int(68 * h_ratio)).render('How to Play', False, black)
        exit_txt = doto_font_1(int(68 * h_ratio)).render('Exit', False, black)
        
        highlight_sur = pygame.Surface((pygame.Surface.get_width(levels_txt) + (30 * w_ratio), int(68 * h_ratio) + (10 * h_ratio)), pygame.SRCALPHA)
        highlight_sur.fill((0, 0, 0, 0))
        
        if 20 * w_ratio <= mouse_x <= 20 * w_ratio + pygame.Surface.get_width(levels_txt) and 305 * h_ratio <= mouse_y <= 305 * h_ratio + (68 * h_ratio):
            
            pygame.draw.rect(highlight_sur, (200, 200, 200, 160), highlight_sur.get_rect(topleft=(0, 0)), border_radius=30)
            
            screen.blit(highlight_sur, highlight_sur.get_rect(topleft=(5 * w_ratio, 305 * h_ratio)))
        
        highlight_sur = pygame.Surface((pygame.Surface.get_width(setting_txt) + (30 * w_ratio), int(68 * h_ratio) + (10 * h_ratio)), pygame.SRCALPHA)
        highlight_sur.fill((0, 0, 0, 0))
        
        if 20 * w_ratio <= mouse_x <= 20 * w_ratio + pygame.Surface.get_width(setting_txt) and 405 * h_ratio <= mouse_y <= 405 * h_ratio + (68 * h_ratio):
            
            pygame.draw.rect(highlight_sur, (200, 200, 200, 160), highlight_sur.get_rect(topleft=(0, 0)), border_radius=30)
            
            screen.blit(highlight_sur, highlight_sur.get_rect(topleft=(5 * w_ratio, 405 * h_ratio)))
        
        highlight_sur = pygame.Surface((pygame.Surface.get_width(how_to_play_txt) + (30 * w_ratio), int(68 * h_ratio) + (10 * h_ratio)), pygame.SRCALPHA)
        highlight_sur.fill((0, 0, 0, 0))
        
        if 20 * w_ratio <= mouse_x <= 20 * w_ratio + pygame.Surface.get_width(how_to_play_txt) and 505 * h_ratio <= mouse_y <= 505 * h_ratio + (68 * h_ratio):
            
            pygame.draw.rect(highlight_sur, (200, 200, 200, 160), highlight_sur.get_rect(topleft=(0, 0)), border_radius=30)
            
            screen.blit(highlight_sur, highlight_sur.get_rect(topleft=(5 * w_ratio, 505 * h_ratio)))
        
        highlight_sur = pygame.Surface((pygame.Surface.get_width(exit_txt) + (30 * w_ratio), int(68 * h_ratio) + (10 * h_ratio)), pygame.SRCALPHA)
        highlight_sur.fill((0, 0, 0, 0))
        
        if 20 * w_ratio <= mouse_x <= 20 * w_ratio + pygame.Surface.get_width(exit_txt) and 605 * h_ratio <= mouse_y <= 605 * h_ratio + (68 * h_ratio):
            
            pygame.draw.rect(highlight_sur, (200, 200, 200, 160), highlight_sur.get_rect(topleft=(0, 0)), border_radius=30)
            
            screen.blit(highlight_sur, highlight_sur.get_rect(topleft=(5 * w_ratio, 605 * h_ratio)))
        
        screen.blit(name_txt, name_txt.get_rect(topleft=(20 * w_ratio, 30 * h_ratio)))
        screen.blit(stars_txt, stars_txt.get_rect(topleft=(20 * w_ratio, 175 * h_ratio)))
        
        stars_num_txt = doto_font_1(int(70 * h_ratio)).render(f"{data['Save Files'][loaded_file]['User Account']['Stars']}", False, black)
        
        screen.blit(stars_num_txt, stars_num_txt.get_rect(topleft=(250 * w_ratio, 175 * h_ratio)))
        
        screen.blit(levels_txt, levels_txt.get_rect(topleft=(20 * w_ratio, 300 * h_ratio)))
        screen.blit(setting_txt, setting_txt.get_rect(topleft=(20 * w_ratio, 400 * h_ratio)))
        screen.blit(how_to_play_txt, how_to_play_txt.get_rect(topleft=(20 * w_ratio, 500 * h_ratio)))
        screen.blit(exit_txt, exit_txt.get_rect(topleft=(20 * w_ratio, 600 * h_ratio)))
        
        pygame.draw.line(screen, black, (pygame.Surface.get_width(screen) // 2, 0), (pygame.Surface.get_width(screen) // 2, pygame.Surface.get_height(screen)), 4)
        
        if selected == 'Levels':
            
            levels_txt = doto_font_1(int(98 * h_ratio)).render('Levels', False, black)
            
            setting_sur.blit(levels_txt, levels_txt.get_rect(center=(pygame.Surface.get_width(setting_sur) // 2, 75 * h_ratio)))
            
            size = (160 * w_ratio, 90 * h_ratio)
            
            
            level_rect_1 = pygame.Surface(size, pygame.SRCALPHA)
            level_rect_1.fill((255, 255, 255, 255))
            level_rect_2 = pygame.Surface(size, pygame.SRCALPHA)
            level_rect_2.fill((255, 255, 255, 255))
            level_rect_3 = pygame.Surface(size, pygame.SRCALPHA)
            level_rect_3.fill((255, 255, 255, 255))
            level_rect_4 = pygame.Surface(size, pygame.SRCALPHA)
            level_rect_4.fill((255, 255, 255, 255))
            level_rect_5 = pygame.Surface(size, pygame.SRCALPHA)
            level_rect_5.fill((255, 255, 255, 255))
            level_rect_6 = pygame.Surface(size, pygame.SRCALPHA)
            level_rect_6.fill((255, 255, 255, 255))
            level_rect_7 = pygame.Surface(size, pygame.SRCALPHA)
            level_rect_7.fill((255, 255, 255, 255))
            level_rect_8 = pygame.Surface(size, pygame.SRCALPHA)
            level_rect_8.fill((255, 255, 255, 255))
            level_rect_9 = pygame.Surface(size, pygame.SRCALPHA)
            level_rect_9.fill((255, 255, 255, 255))
            
            
            setting_sur.blit(level_rect_1, level_rect_1.get_rect(center=(125 * w_ratio, 185 * h_ratio)))
            setting_sur.blit(pygame.transform.scale(levels_image['Level 1'], size), pygame.transform.scale(levels_image['Level 1'], size).get_rect(center=(125 * w_ratio, 185 * h_ratio)))
            setting_sur.blit(level_rect_2, level_rect_2.get_rect(center=(pygame.Surface.get_width(setting_sur) // 2, 185 * h_ratio)))
            setting_sur.blit(pygame.transform.scale(levels_image['Level 2'], size), pygame.transform.scale(levels_image['Level 2'], size).get_rect(center=(pygame.Surface.get_width(setting_sur) // 2, 185 * h_ratio)))
            setting_sur.blit(level_rect_3, level_rect_3.get_rect(center=(pygame.Surface.get_width(setting_sur) - (125 * w_ratio), 185 * h_ratio)))
            setting_sur.blit(pygame.transform.scale(levels_image['Level 3'], size), pygame.transform.scale(levels_image['Level 3'], size).get_rect(center=(pygame.Surface.get_width(setting_sur) - (125 * w_ratio), 185 * h_ratio)))
            
            setting_sur.blit(level_rect_4, level_rect_4.get_rect(center=(125 * w_ratio, 385 * h_ratio)))
            setting_sur.blit(pygame.transform.scale(levels_image['Level 4'], size), pygame.transform.scale(levels_image['Level 4'], size).get_rect(center=(125 * w_ratio, 385 * h_ratio)))
            setting_sur.blit(level_rect_5, level_rect_5.get_rect(center=(pygame.Surface.get_width(setting_sur) // 2, 385 * h_ratio)))
            setting_sur.blit(pygame.transform.scale(levels_image['Level 5'], size), pygame.transform.scale(levels_image['Level 5'], size).get_rect(center=(pygame.Surface.get_width(setting_sur) // 2, 385 * h_ratio)))
            setting_sur.blit(level_rect_6, level_rect_6.get_rect(center=(pygame.Surface.get_width(setting_sur) - (125 * w_ratio), 385 * h_ratio)))
            setting_sur.blit(pygame.transform.scale(levels_image['Level 6'], size), pygame.transform.scale(levels_image['Level 6'], size).get_rect(center=(pygame.Surface.get_width(setting_sur) - (125 * w_ratio), 385 * h_ratio)))
            
            setting_sur.blit(level_rect_7, level_rect_7.get_rect(center=(125 * w_ratio, 585 * h_ratio)))
            setting_sur.blit(pygame.transform.scale(levels_image['Level 7'], size), pygame.transform.scale(levels_image['Level 7'], size).get_rect(center=(125 * w_ratio, 585 * h_ratio)))
            setting_sur.blit(level_rect_8, level_rect_8.get_rect(center=(pygame.Surface.get_width(setting_sur) // 2, 585 * h_ratio)))
            setting_sur.blit(pygame.transform.scale(levels_image['Level 8'], size), pygame.transform.scale(levels_image['Level 8'], size).get_rect(center=(pygame.Surface.get_width(setting_sur) // 2, 585 * h_ratio)))
            setting_sur.blit(level_rect_9, level_rect_9.get_rect(center=(pygame.Surface.get_width(setting_sur) - (125 * w_ratio), 585 * h_ratio)))
            setting_sur.blit(pygame.transform.scale(levels_image['Level 9'], size), pygame.transform.scale(levels_image['Level 9'], size).get_rect(center=(pygame.Surface.get_width(setting_sur) - (125 * w_ratio), 585 * h_ratio)))
            
        if selected == 'Settings':
            
            setting_sur.blit(settings_txt, settings_txt.get_rect(topleft=(30 * w_ratio, 0 * h_ratio)))
            
            setting_sur.blit(audio_txt, audio_txt.get_rect(topleft=((30 * w_ratio, 110 * h_ratio))))
            
            setting_sur.blit(master_volume_txt, master_volume_txt.get_rect(topleft=((70 * w_ratio, 210 * h_ratio))))
            
            setting_sur.blit(sfx_volume_txt, sfx_volume_txt.get_rect(topleft=((70 * w_ratio, 335 * h_ratio))))
            
            setting_sur.blit(music_volume_txt, music_volume_txt.get_rect(topleft=((70* w_ratio, 460 * h_ratio))))
            
            setting_sur.blit(interface_volume_txt, interface_volume_txt.get_rect(topleft=((70 * w_ratio, 585 * h_ratio))))
            
            pygame.draw.rect(slider_sur, (255, 255, 255, 255), slider_sur.get_rect(topleft=(0, 0)), 4, border_radius=30)
            
            pygame.draw.rect(slider_diamond_sur, (240, 248, 255, 255), slider_diamond_sur.get_rect(topleft=(0, 0)), 5)
            
            setting_sur.blit(slider_sur, slider_sur.get_rect(topleft=(25 * w_ratio, 270 * h_ratio)))
            setting_sur.blit(pygame.transform.rotate(slider_diamond_sur, 45), pygame.transform.rotate(slider_diamond_sur, 45).get_rect(center=(((50 + data['Save Files'][loaded_file]['Audio']['Master Volume'] * (525/100)) * w_ratio), 295 * h_ratio)))
            
            setting_sur.blit(slider_sur, slider_sur.get_rect(topleft=(25 * w_ratio, 395 * h_ratio)))
            setting_sur.blit(pygame.transform.rotate(slider_diamond_sur, 45), pygame.transform.rotate(slider_diamond_sur, 45).get_rect(center=(((50 + data['Save Files'][loaded_file]['Audio']['SFX Volume'] * (525/100)) * w_ratio), 420 * h_ratio)))
            
            setting_sur.blit(slider_sur, slider_sur.get_rect(topleft=(25 * w_ratio, 520 * h_ratio)))
            setting_sur.blit(pygame.transform.rotate(slider_diamond_sur, 45), pygame.transform.rotate(slider_diamond_sur, 45).get_rect(center=(((50 + data['Save Files'][loaded_file]['Audio']['Music Volume'] * (525/100)) * w_ratio), 545 * h_ratio)))
            
            setting_sur.blit(slider_sur, slider_sur.get_rect(topleft=(25 * w_ratio, 645 * h_ratio)))
            setting_sur.blit(pygame.transform.rotate(slider_diamond_sur, 45), pygame.transform.rotate(slider_diamond_sur, 45).get_rect(center=(((50 + data['Save Files'][loaded_file]['Audio']['Interface Volume'] * (525/100))) * w_ratio, 670 * h_ratio)))
            
            setting_sur.blit(controls_txt, controls_txt.get_rect(topleft=(30 * w_ratio, 700 * h_ratio)))
            
            setting_sur.blit(keybind_txt, keybind_txt.get_rect(center=(235 * w_ratio, 815 * h_ratio)))
            
            setting_sur.blit(key_txt, key_txt.get_rect(center=(515 * w_ratio, 815 * h_ratio)))
            
            for key in abilities_txt:
                pygame.draw.rect(setting_sur, (160, 160, 160, 160), (30 * w_ratio, (850 + (50 * all_controls_surfaces[key][1])) * h_ratio, 410 * w_ratio, 50 * h_ratio))
                pygame.draw.rect(setting_sur, (160, 160, 160, 160), (437 * w_ratio, (850 + (50 * all_controls_surfaces[key][1])) * h_ratio, 150 * w_ratio, 50 * h_ratio))
                pygame.draw.rect(setting_sur, white, (30 * w_ratio, (850 + (50 * all_controls_surfaces[key][1])) * h_ratio, 410 * w_ratio, 50 * h_ratio), 3)
                pygame.draw.rect(setting_sur, white, (437 * w_ratio, (850  + (50 * all_controls_surfaces[key][1])) * h_ratio, 150 * w_ratio, 50 * h_ratio), 3)
                setting_sur.blit(all_controls_surfaces[key][0], all_controls_surfaces[key][0].get_rect(center=(235 * w_ratio, (875 + (50 * all_controls_surfaces[key][1])) * h_ratio)))
                setting_sur.blit(all_controls_surfaces[key][2], (all_controls_surfaces[key][2].get_rect(center=(515 * w_ratio, (875 + (50 * all_controls_surfaces[key][1])) * h_ratio))))
            
        if selected == 'How to Play':
            
            pygame.draw.rect(setting_sur, (200, 200, 200, 200), (15 * w_ratio, 140 * h_ratio, 600 * w_ratio, 2000 * h_ratio), border_radius=30)
            setting_sur.blit(how_to_play_txt, how_to_play_txt.get_rect(center=(pygame.Surface.get_width(setting_sur) // 2, 75 * h_ratio)))
            #pygame.draw.rect(setting_sur, (
            setting_sur.blit(all_instructions[0], all_instructions[0].get_rect(topleft=(30 * w_ratio, 150 * h_ratio)))
            setting_sur.blit(all_instructions[1], all_instructions[1].get_rect(topleft=(30 * w_ratio, 275 * h_ratio)))
            
        screen.blit(setting_sur, (pygame.Surface.get_width(screen) // 2, scroll * h_ratio))
        
        if changing[0]:
            
            listening_for_key = doto_font_1(int(60 * h_ratio)).render(listening_txt[counter_txt // 10], False, white)
            back_space_to_cancel = doto_font_1(int(32 * h_ratio)).render('(Backspace to cancel)', False, white)
            counter_txt += 1
            if counter_txt >= 30:
                counter_txt = 0
            cover_screen_sur = pygame.Surface((pygame.Surface.get_width(screen), pygame.Surface.get_height(screen)), pygame.SRCALPHA)
            cover_screen_sur.fill((0, 0, 0, 200))
            screen.blit(cover_screen_sur, (0, 0))
            screen.blit(listening_for_key, listening_for_key.get_rect(center=(pygame.Surface.get_width(screen) // 2, pygame.Surface.get_height(screen) // 2)))
            screen.blit(back_space_to_cancel, back_space_to_cancel.get_rect(center=(pygame.Surface.get_width(screen) // 2, (pygame.Surface.get_height(screen) // 2) + 100)))
        
        if holding[0] == True:
            percent = mouse_x - holding[2]
            total_value = percent // ((525/100) * w_ratio)
            data['Save Files'][loaded_file]['Audio'][holding[1]] = holding[3] + total_value
            if holding[3] + total_value > 100:
                data['Save Files'][loaded_file]['Audio'][holding[1]] = 100
            if holding[3] + total_value < 0:
                data['Save Files'][loaded_file]['Audio'][holding[1]] = 0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main = False
                pygame.quit()
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if changing[0] == False and event.button == 1 and selected == 'Settings':
                    if abs(mouse_x - ((pygame.Surface.get_width(screen) // 2) + ((50 + (data['Save Files'][loaded_file]['Audio']['Master Volume'] * (525/100))) * w_ratio))) + (abs(mouse_y - ((scroll + 295) * h_ratio))) <= math.sqrt(((25 ** 2) * w_ratio) + ((25 ** 2) * h_ratio)):
                        holding = [True, 'Master Volume', mouse_x, data['Save Files'][loaded_file]['Audio']['Master Volume']]
                        interface_sound['click'].play()
                    if abs(mouse_x - ((pygame.Surface.get_width(screen) // 2) + ((50 + (data['Save Files'][loaded_file]['Audio']['SFX Volume'] * (525/100))) * w_ratio))) + (abs(mouse_y - ((scroll + 420) * h_ratio))) <= math.sqrt(((25 ** 2) * w_ratio) + ((25 ** 2) * h_ratio)):
                        holding = [True, 'SFX Volume', mouse_x, data['Save Files'][loaded_file]['Audio']['SFX Volume']]
                        interface_sound['click'].play()
                    if abs(mouse_x - ((pygame.Surface.get_width(screen) // 2) + ((50 + (data['Save Files'][loaded_file]['Audio']['Music Volume'] * (525/100))) * w_ratio))) + (abs(mouse_y - ((scroll + 545) * h_ratio))) <= math.sqrt(((25 ** 2) * w_ratio) + ((25 ** 2) * h_ratio)):
                        holding = [True, 'Music Volume', mouse_x, data['Save Files'][loaded_file]['Audio']['Music Volume']]
                        interface_sound['click'].play()
                    if abs(mouse_x - ((pygame.Surface.get_width(screen) // 2) + ((50 + (data['Save Files'][loaded_file]['Audio']['Interface Volume'] * (525/100))) * w_ratio))) + (abs(mouse_y - ((scroll + 670) * h_ratio))) <= math.sqrt(((25 ** 2) * w_ratio) + ((25 ** 2) * h_ratio)):
                        holding = [True, 'Interface Volume', mouse_x, data['Save Files'][loaded_file]['Audio']['Interface Volume']]
                        interface_sound['click'].play()
                        
                if 20 * w_ratio <= mouse_x <= 20 * w_ratio + pygame.Surface.get_width(levels_txt) and 305 * h_ratio <= mouse_y <= 305 * h_ratio + (68 * h_ratio):
                    
                    selected = 'Levels'
                    scroll = 0
                    
                if 20 * w_ratio <= mouse_x <= 20 * w_ratio + pygame.Surface.get_width(setting_txt) and 405 * h_ratio <= mouse_y <= 405 * h_ratio + (68 * h_ratio):
                    
                    selected = 'Settings'
                    scroll = 0
                    
                if 20 * w_ratio <= mouse_x <= 20 * w_ratio + pygame.Surface.get_width(how_to_play_txt) and 505 * h_ratio <= mouse_y <= 505 * h_ratio + (68 * h_ratio):
                    
                    selected = 'How to Play'
                    scroll = 0
                    
                if 20 * w_ratio <= mouse_x <= 20 * w_ratio + pygame.Surface.get_width(exit_txt) and 605 * h_ratio <= mouse_y <= 605 * h_ratio + (68 * h_ratio):
                    
                    main = False
                    pygame.quit()
                    return False
                
                if loaded_file != 'Test File' and changing[0] == False and event.button == 1 and selected == 'Settings':    
                    for key in all_controls_surfaces:
                        if (pygame.Surface.get_width(screen) // 2) + (440 * w_ratio) <= mouse_x <= (pygame.Surface.get_width(screen) // 2) + (590 * w_ratio) and ((850 + scroll) + (50 * all_controls_surfaces[key][1])) * h_ratio <= mouse_y <= ((900 + scroll) + (50 * all_controls_surfaces[key][1])) * h_ratio:
                            changing = [True, key]
                            
                if event.button == 1 and selected == 'Levels':
                    
                    if (pygame.Surface.get_width(screen) // 2) + (45 * w_ratio) <= mouse_x <= (pygame.Surface.get_width(screen) // 2) + (205 * w_ratio) and 140 * h_ratio <= mouse_y <= 230 * h_ratio:
                        selected_level = 'Level 1'
                        grid = Making_Level(selected_level)
                        return True
                        
                    if (pygame.Surface.get_width(screen) // 2) + (pygame.Surface.get_width(setting_sur) // 2) - (80 * w_ratio) <= mouse_x <= (pygame.Surface.get_width(screen) // 2) + (pygame.Surface.get_width(setting_sur) // 2) + (80 * w_ratio) and 140 * h_ratio <= mouse_y <= 230 * h_ratio:
                        selected_level = 'Level 2'
                        grid = Making_Level(selected_level)
                        return True
                        
                    if pygame.Surface.get_width(screen) - (125 * w_ratio) - (80 * w_ratio) <= mouse_x <= pygame.Surface.get_width(screen) - (125 * w_ratio) + (80 * w_ratio) and 140 * h_ratio <= mouse_y <= 230 * h_ratio:
                        selected_level = 'Level 3'
                        grid = Making_Level(selected_level)
                        return True
                        
                    if (pygame.Surface.get_width(screen) // 2) + (45 * w_ratio) <= mouse_x <= (pygame.Surface.get_width(screen) // 2) + (205 * w_ratio) and 340 * h_ratio <= mouse_y <= 430 * h_ratio:
                        selected_level = 'Level 4'
                        grid = Making_Level(selected_level)
                        return True
                        
                    if (pygame.Surface.get_width(screen) // 2) + (pygame.Surface.get_width(setting_sur) // 2) - (80 * w_ratio) <= mouse_x <= (pygame.Surface.get_width(screen) // 2) + (pygame.Surface.get_width(setting_sur) // 2) + (80 * w_ratio) and 340 * h_ratio <= mouse_y <= 430 * h_ratio:
                        selected_level = 'Level 5'
                        grid = Making_Level(selected_level)
                        return True
                        
                    if pygame.Surface.get_width(screen) - (125 * w_ratio) - (80 * w_ratio) <= mouse_x <= pygame.Surface.get_width(screen) - (125 * w_ratio) + (80 * w_ratio) and 340 * h_ratio <= mouse_y <= 430 * h_ratio:
                        selected_level = 'Level 6'
                        grid = Making_Level(selected_level)
                        return True
                        
                    if (pygame.Surface.get_width(screen) // 2) + (45 * w_ratio) <= mouse_x <= (pygame.Surface.get_width(screen) // 2) + (205 * w_ratio) and 540 * h_ratio <= mouse_y <= 630 * h_ratio:
                        selected_level = 'Level 7'
                        grid = Making_Level(selected_level)
                        return True
                        
                    if (pygame.Surface.get_width(screen) // 2) + (pygame.Surface.get_width(setting_sur) // 2) - (80 * w_ratio) <= mouse_x <= (pygame.Surface.get_width(screen) // 2) + (pygame.Surface.get_width(setting_sur) // 2) + (80 * w_ratio) and 540 * h_ratio <= mouse_y <= 630 * h_ratio:
                        selected_level = 'Level 8'
                        grid = Making_Level(selected_level)
                        return True
                        
                    if pygame.Surface.get_width(screen) - (125 * w_ratio) - (80 * w_ratio) <= mouse_x <= pygame.Surface.get_width(screen) - (125 * w_ratio) + (80 * w_ratio) and 540 * h_ratio <= mouse_y <= 630 * h_ratio:
                        selected_level = 'Level 9'
                        grid = Making_Level(selected_level)
                        return True
                
            if event.type == pygame.MOUSEBUTTONUP:
                if loaded_file != 'Test File' and changing[0] == False and event.button == 1 and holding[0] == True:
                    if mouse_x > holding[2]:
                        percent = mouse_x - holding[2]
                    if holding[2] > mouse_x:
                        percent = holding[2] - mouse_x
                    else:
                        percent = 0
                    total_value = percent // (525/100)
                    data['Save Files'][loaded_file]['Audio'][holding[1]]
                    with open('fbla_game_save_files.json', 'w') as file:
                        
                        json.dump(data, file, indent=4)
                    
                    with open('fbla_game_save_files.json', 'r') as file:
            
                        data = json.load(file)
                    
                if event.button == 1:    
                
                    holding = [False, '', 0, 0]
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main = False
                    pygame.quit()
                    return False
                if loaded_file != 'Test File' and changing[0]:
                    for key, value in posible_keybinds.items():
                        if event.key == value:
                            if assigning_keybinds(changing[1], key):
                                
                                data['Save Files'][loaded_file]['Controls'][changing[1]] = key
                                
                                with open('fbla_game_save_files.json', 'w') as file:
                                    
                                    json.dump(data, file, indent=4)
                                
                                with open('fbla_game_save_files.json', 'r') as file:
                        
                                    data = json.load(file)
                                    
                                loading_keybinds()
                                
                                all_controls_surfaces[changing[1]][2] = doto_font_1(int(20 * h_ratio)).render(actual_keybinds[changing[1]][1].upper(), False, black)
                                
                            changing = [False, 'key']
                        if event.key == pygame.K_BACKSPACE:
                            changing = [False, 'key']
                        
            if (selected == 'Settings' or selected == 'How to Play') and event.type == pygame.MOUSEWHEEL and pygame.Surface.get_width(screen) // 2 < pygame.mouse.get_pos()[0]:
                if selected == 'Settings':
                    scroll_max = -1650
                if selected == 'How to Play':
                    scroll_max = -2000
                if event.y > 0:
                    #Scroll Up
                    scroll += 75
                    if scroll > 0:
                        scroll = 0
                elif event.y < 0:
                    #Scroll Down
                    scroll -= 75
                    if scroll < scroll_max * 1:
                        scroll = scroll_max * 1
                        
        pygame.display.flip()
            
        clock.tick(60)    

def Drawing_Envieroment(obstacles):
    global object_overlay, level_screen

    ratio()

    screen.fill(purple_bg)

    walls_w_val = 1200 * w_ratio
    walls_h_val = (int(500 / 3) * 3) * h_ratio

    walls_screen = pygame.Surface((walls_w_val, walls_h_val))

    walls_screen.fill(purple_walls)
    
    walls_w_val = 1200 * w_ratio
    walls_h_val = (int(500 / 3) * 3) * h_ratio
    
    object_overlay = pygame.Surface((walls_w_val, walls_h_val), pygame.SRCALPHA)
    object_overlay.fill((111, 111, 111, 255))
    object_overlay.set_colorkey((111, 111, 111, 255))
    
    level_w_val = int((int(1150 / 6) * 6) * w_ratio)
    level_h_val = int((int(450 / 3) * 3) * h_ratio)
    
    level_screen = pygame.Surface((level_w_val, level_h_val))
    
    level_screen.fill(purple_level)
    
    rate()
    
    for obj in obstacles:
        obj.drawing_polygon()
        obj.drawing_lines()
        
    main_object_group.draw(object_overlay)
    
    for obj in obstacles:
        obj.drawing()
    
    #grid_rect_walls = pygame.Surface((200 * w_ratio, 400 / 3 * h_ratio))
    #grid_rect_level = pygame.Surface((1150 / 6 * w_ratio, 375 / 3 * h_ratio))

    screen.blit(walls_screen, (40 * w_ratio, 40 * h_ratio))
    screen.blit(level_screen, (65 * w_ratio, 62 * h_ratio))

    pygame.draw.line(screen, black, (40 * w_ratio, 40 * h_ratio), (65 * w_ratio, 62 * h_ratio), int(5 * w_ratio))
    pygame.draw.line(screen, black, (40 * w_ratio, 40 * h_ratio + walls_h_val),(65 * w_ratio, 62 * h_ratio + level_h_val), int(5 * w_ratio))
    pygame.draw.line(screen, black, (40 * w_ratio + walls_w_val, 40 * h_ratio), (65 * w_ratio + level_w_val, 62 * h_ratio), int(5 * w_ratio))
    pygame.draw.line(screen, black, (40 * w_ratio + walls_w_val, 40 * h_ratio + walls_h_val), (65 * w_ratio + level_w_val, 62 * h_ratio + level_h_val), int(5 * w_ratio))

    pygame.draw.line(screen, black, (40 * w_ratio, 40 * h_ratio), (40 * w_ratio, 40 * h_ratio + walls_h_val), int(5 * w_ratio))
    pygame.draw.line(screen, black, (40 * w_ratio, 40 * h_ratio), (40 * w_ratio + walls_w_val, 40 * h_ratio), int(5 * w_ratio))
    pygame.draw.line(screen, black, (40 * w_ratio + walls_w_val, 40 * h_ratio), (40 * w_ratio + walls_w_val, 40 * h_ratio + walls_h_val), int(5 * w_ratio))
    pygame.draw.line(screen, black, (40 * w_ratio + walls_w_val, 40 * h_ratio + walls_h_val), (40 * w_ratio, 40 * h_ratio + walls_h_val), int(5 * w_ratio))

    pygame.draw.line(screen, black, (65 * w_ratio, 62 * h_ratio), (65 * w_ratio, 62 * h_ratio + level_h_val), int(5 * w_ratio))
    pygame.draw.line(screen, black, (65 * w_ratio, 62 * h_ratio), (65 * w_ratio + level_w_val, 62 * h_ratio), int(5 * w_ratio))
    pygame.draw.line(screen, black, (65 * w_ratio + level_w_val, 62 * h_ratio), (65 * w_ratio + level_w_val, 62 * h_ratio + level_h_val), int(5 * w_ratio))
    pygame.draw.line(screen, black, (65 * w_ratio + level_w_val, 62 * h_ratio + level_h_val), (65 * w_ratio, 62 * h_ratio + level_h_val), int(5 * w_ratio))

    ability_rect_height = 560 * h_ratio
    ability_rect_size = (100 * w_ratio, 100 * h_ratio)

    pygame.draw.rect(screen, black, (40 * w_ratio, ability_rect_height, ability_rect_size[0], ability_rect_size[1]), max(int(2 * w_ratio), 1))
    pygame.draw.rect(screen, black, (170 * w_ratio, ability_rect_height, ability_rect_size[0], ability_rect_size[1]), max(int(2 * w_ratio), 1))
    pygame.draw.rect(screen, black, (300 * w_ratio, ability_rect_height, ability_rect_size[0], ability_rect_size[1]), max(int(2 * w_ratio), 1))
    pygame.draw.rect(screen, black, (430 * w_ratio, ability_rect_height, ability_rect_size[0], ability_rect_size[1]), max(int(2 * w_ratio), 1))
    pygame.draw.rect(screen, black, (560 * w_ratio, ability_rect_height, ability_rect_size[0], ability_rect_size[1]), max(int(2 * w_ratio), 1))
    
    screen.blit(object_overlay, (40 * w_ratio, 40 * h_ratio))


def Making_Level(level):
    global obstacles_group, main_object_group, main_object, width, height, end_point
    
    with open('fbla_game_save_files.json', 'r') as file:
        
        data = json.load(file)
    
    #Grid will hold a list, Index 0 If solid, index 1 air direccion depending on the direccion, 
    #it will act accordinly, index 2 gravity, index 3 if solid then object, index 4 if changeble
    #And index 5 the key
    
    grid_img = data['Save Files']['Levels Layout'][level]
    
    width = 6
    height = 4
    
    grid = []
    
    obstacles_group = pygame.sprite.Group()
    
    for y in range(height):
        grid.append([])
        for x in range(width):
            if grid_img[y][x] == 'a':
                grid[y].append([0, pygame.Vector2(0, 0), pygame.Vector2(0, 10 * h_ratio), None, True, 'a'])
            if grid_img[y][x] == 'x':
                obj = Blocks((x, y), 'hard')
                obstacles_group.add(obj)
                grid[y].append([1, pygame.Vector2(0, 0), pygame.Vector2(0, 0), obj, False, 'x'])
            if grid_img[y][x] == 'k':
                obj = Blocks((x, y), 'kill_zone')
                obstacles_group.add(obj)
                grid[y].append([0, pygame.Vector2(0, 0), pygame.Vector2(0, 0), obj, False, 'k'])
            if grid_img[y][x] == 'b':
                obj = Blocks((x, y), 'hard_bouncy')
                obstacles_group.add(obj)
                grid[y].append([1, pygame.Vector2(0, 0), pygame.Vector2(0, 0), obj, False, 'b'])
            if grid_img[y][x] == 'o':
                obj = Blocks((x, y), 'normal')
                obstacles_group.add(obj)
                grid[y].append([1, pygame.Vector2(0, 0), pygame.Vector2(0, 10 * h_ratio), obj, True, 'o'])
            if grid_img[y][x] == 'i':
                grid[y].append([0, pygame.Vector2(0, 0), pygame.Vector2(0, -10 * h_ratio), None, True, 'i'])
            if grid_img[y][x] == 's':
                main_object = Player('Circle', (x * outer_per_x, (y * outer_per_y) + 120), (0, 0))
                grid[y].append([0, pygame.Vector2(0, 0), pygame.Vector2(0, 10 * h_ratio), None, True, 's'])
            if grid_img[y][x] == 'e':
                end_point = (x, y)
                end_point_object = Blocks(end_point, 'end_block')
                obstacles_group.add(end_point_object)
                grid[y].append([0, pygame.Vector2(0, 0), pygame.Vector2(0, 10 * h_ratio), end_point_object, True, 'e'])
    
    main_object_group = pygame.sprite.Group()
    main_object_group.add(main_object)
    
    return grid


def Core_Game_Display():

    pass


#Gameplay functions


def assigning_keybinds(selected_slot, new_key) -> str:

    # for key, value in actual_keybinds.items():
    # if selected_slot == key:
    # save_key = value
    # for key, value in posible_keybinds.items():
    # if save_key == value:
    # selected_key = key

    selected_key = actual_keybinds[selected_slot][1]
    
    if selected_key == new_key:
        return False#'This is the same key'
    elif f"{new_key}" not in posible_keybinds:
        return False#'This key is not available'
    for key, value in actual_keybinds.items():
        if posible_keybinds[f"{new_key}"] == value[0]:
            return False#f'This key is already assigned to {key}'
    actual_keybinds[selected_slot] = [posible_keybinds[f'{new_key}'], f'{new_key}']
    return True#f'{new_key} as been assigned to {selected_slot}'


#print(assigning_keybinds('gravity_switch', 'space'))


def pressing_keybind(button) -> bool:

    keys = pygame.key.get_pressed()

    if keys[button]:
        return True

    return False


def activating_grid():

    main_pressed = []
    ability_pressed = []
    x_pressed = []
    y_pressed = []
    ability_direccion_pressed = []
    ability_activation_pressed = []

    for key in actual_keybinds:
        if pressing_keybind(actual_keybinds[key][0]):
            if key in main_keybinds:
                main_pressed.append(key)
            elif key in ability_keybinds:
                ability_pressed.append(key)
            elif key in grid_x:
                x_pressed.append(key)
            elif key in grid_y:
                y_pressed.append(key)
            elif key in ability_direccion_keybinds:
                ability_direccion_pressed.append(key)
            elif key in ability_activation:
                ability_activation_pressed.append(key)

    return [main_pressed, ability_pressed, x_pressed, y_pressed, ability_direccion_pressed, ability_activation_pressed]


def selecting_ability(direct=None, direction=None):

    global ability_index

    if direct:

        ability_index = int(extract_first_digit(direct[0])) - 1

    elif direction and 2 > 3:

        if direction[0] == 'ability_slot_up':

            ability_index += 1

            if ability_index >= num_of_abilities:

                ability_index = 0

        elif direction[0] == 'ability_slot_down':

            ability_index -= 1

            if ability_index < 0:

                ability_index = num_of_abilities - 1


#Needed Functions


def ratio():
    global w_ratio, h_ratio, res_scale
    w_ratio = pygame.Surface.get_width(screen) / og_w
    h_ratio = pygame.Surface.get_height(screen) / og_h
    res_scale = og_w / og_h

def rate():
    global outer_per_x, outer_per_y, inner_per_x, inner_per_y, center_x, center_y
    
    outer_per_x = int(pygame.Surface.get_width(object_overlay) / width)
    outer_per_y = int(pygame.Surface.get_height(object_overlay) / height)
    inner_per_x = int(pygame.Surface.get_width(level_screen) / width)
    inner_per_y = int(pygame.Surface.get_height(level_screen) / height)
    center_x = pygame.Surface.get_width(object_overlay) / 2
    center_y = pygame.Surface.get_height(object_overlay) / 2

def setting_audio(when=None):
    global sfx, interface_sound, loaded_file
    
    with open('fbla_game_save_files.json', 'r') as file:
        
        data = json.load(file)
    
    if when == 'start':
        
        loaded_file = 'Reset File'
    
    pygame.mixer.music.set_volume(data['Save Files'][loaded_file]['Audio']['Master Volume'] / 100 * data['Save Files'][loaded_file]['Audio']['Music Volume'] / 100)
    
    for key in sfx:
        sfx[key].set_volume(data['Save Files'][loaded_file]['Audio']['Master Volume'] / 100 * data['Save Files'][loaded_file]['Audio']['SFX Volume'] / 100)
    
    for key in interface_sound:
        interface_sound[key].set_volume((data['Save Files'][loaded_file]['Audio']['Master Volume'] / 100) * (data['Save Files'][loaded_file]['Audio']['Interface Volume'] / 100))
    
def polar_coordinate(reference, distance, angle, side_angle):
    
    x = (reference.x + distance * math.cos((angle + side_angle) / (180 / math.pi)))
    y = (reference.y + distance * math.sin((angle + side_angle) / (180 / math.pi)))
    
    return pygame.Vector2(x, y)

def sine_func(x):
    
    return (math.sin(x/90) * 45) + 500
    
def getting_graph(main_x_value):
    
    points = {'point_1' : pygame.Vector2(main_x_value, sine_func(main_x_value))}
    points['point_2'] = polar_coordinate(points['point_1'], current_distance_for_lines, current_angles[0], 0)
    points['point_3'] = polar_coordinate(points['point_1'], current_distance_for_lines, current_angles[1], 0)
    points['point_4'] = polar_coordinate(points['point_2'], current_distance_for_lines, current_angles[2], 0)
    points['point_5'] = polar_coordinate(points['point_1'], current_distance_for_lines, current_angles[3], 0)
    points['point_6'] = polar_coordinate(points['point_3'], current_distance_for_lines, current_angles[4], 0)
    points['point_7'] = polar_coordinate(points['point_2'], current_distance_for_lines, current_angles[5], 0)
    points['point_8'] = polar_coordinate(points['point_4'], current_distance_for_lines, current_angles[6], 0)
    points['point_9'] = polar_coordinate(points['point_7'], current_distance_for_lines, current_angles[7], 0)
    points['point_10'] = polar_coordinate(points['point_3'], current_distance_for_lines, current_angles[8], 0)
    points['point_11'] = polar_coordinate(points['point_3'], current_distance_for_lines, current_angles[9], 0)
    points['point_12'] = polar_coordinate(points['point_9'], current_distance_for_lines, current_angles[10], 0)
    points['point_13'] = polar_coordinate(points['point_6'], current_distance_for_lines, current_angles[11], 0)
    points['point_14'] = polar_coordinate(points['point_10'], current_distance_for_lines, current_angles[12], 0)
    points['point_15'] = polar_coordinate(points['point_10'], current_distance_for_lines, current_angles[13], 0)
    points['point_16'] = polar_coordinate(points['point_15'], current_distance_for_lines, current_angles[14], 0)
    points['point_17'] = polar_coordinate(points['point_16'], current_distance_for_lines, current_angles[15], 0)
    points['point_18'] = polar_coordinate(points['point_5'], current_distance_for_lines, current_angles[16], 0)
    points['point_19'] = polar_coordinate(points['point_4'], current_distance_for_lines, current_angles[17], 0)
    points['point_20'] = polar_coordinate(points['point_5'], current_distance_for_lines, current_angles[18], 0)
    points['point_21'] = polar_coordinate(points['point_19'], current_distance_for_lines, current_angles[19], 0)
    points['point_22'] = polar_coordinate(points['point_18'], current_distance_for_lines, current_angles[20], 0)
    points['point_23'] = polar_coordinate(points['point_16'], current_distance_for_lines, current_angles[21], 0)
    points['point_24'] = polar_coordinate(points['point_20'], current_distance_for_lines, current_angles[22], 0)
    points['point_25'] = polar_coordinate(points['point_13'], current_distance_for_lines, current_angles[23], 0)
    points['point_26'] = polar_coordinate(points['point_20'], current_distance_for_lines, current_angles[24], 0)
    points['point_27'] = polar_coordinate(points['point_21'], current_distance_for_lines, current_angles[25], 0)
    points['point_28'] = polar_coordinate(points['point_27'], current_distance_for_lines, current_angles[26], 0)
    points['point_29'] = polar_coordinate(points['point_21'], current_distance_for_lines, current_angles[27], 0)
    points['point_30'] = polar_coordinate(points['point_24'], current_distance_for_lines, current_angles[28], 0)
    points['point_31'] = polar_coordinate(points['point_26'], current_distance_for_lines, current_angles[29], 0)
    points['point_32'] = polar_coordinate(points['point_29'], current_distance_for_lines, current_angles[30], 0)
    points['point_33'] = polar_coordinate(points['point_32'], current_distance_for_lines, current_angles[31], 0)
    points['point_34'] = polar_coordinate(points['point_30'], current_distance_for_lines, current_angles[32], 0)
    points['point_35'] = polar_coordinate(points['point_31'], current_distance_for_lines, current_angles[33], 0)
    points['point_36'] = polar_coordinate(points['point_8'], current_distance_for_lines, current_angles[34], 0)
    points['point_37'] = polar_coordinate(points['point_28'], current_distance_for_lines, current_angles[35], 0)
    points['point_38'] = polar_coordinate(points['point_33'], current_distance_for_lines, current_angles[36], 0)
    points['point_39'] = polar_coordinate(points['point_33'], current_distance_for_lines, current_angles[37], 0)
    points['point_40'] = polar_coordinate(points['point_35'], current_distance_for_lines, current_angles[38], 0)
    points['point_41'] = polar_coordinate(points['point_35'], current_distance_for_lines, current_angles[39], 0)
    points['point_42'] = polar_coordinate(points['point_40'], current_distance_for_lines, current_angles[40], 0)
    points['point_43'] = polar_coordinate(points['point_39'], current_distance_for_lines, current_angles[41], 0)
    points['point_44'] = polar_coordinate(points['point_38'], current_distance_for_lines, current_angles[42], 0)
                
    return points

def doto_font_1(size):
    return pygame.font.Font(doto_font_path, size)

def Updating_Screen():
    global screen
    w = pygame.Surface.get_width(screen)
    h = w / h_ratio
    screen = pygame.display.set_mode((w, h), pygame.DOUBLEBUF | pygame.FULLSCREEN)
    # elif All_Display_Modes[FullScreen_Loop]:
        # screen = pygame.display.set_mode((Current_Resolution_X, Current_Resolution_Y), pygame.FULLSCREEN | pygame.DOUBLEBUF)

def extract_first_digit(s):
    for char in s:
        if char.isdigit():
            return char  # Return the first digit found
    return None


def select_grid(key_1=None, key_2=None):

    if key_1 != None:
        x = int(extract_first_digit(key_1))
    else:
        x = None
    if key_2 != None:
        y = int(extract_first_digit(key_2))
    else:
        y = None

    return [x, y]


def deciding_grid(x_list, y_list):

    if x_list and y_list:
        return [x_list[0], y_list[0]]

    elif x_list and not y_list:
        return [x_list[0], None]

    elif y_list and not x_list:
        return [None, y_list[0]]

    else:
        return [None, None]

def calculate_centroid(coords):
    x_coords = [coord[0] for coord in coords]
    y_coords = [coord[1] for coord in coords]
    centroid = (sum(x_coords) / len(coords), sum(y_coords) / len(coords))
    return centroid

def angle_from_center(center, point):
    return math.atan2(point[1] - center[1], point[0] - center[0])

def sort_vertices(coords):
    centroid = calculate_centroid(coords)
    
    sorted_coords = sorted(coords, key=lambda point: angle_from_center(centroid, point))
    
    return sorted_coords
    
def updating_exp_level():
    
    with open('fbla_game_save_files.json', 'r') as file:
        
        data = json.load(file)
    
    while data['Save Files'][loaded_file]['User Account']['Exp Amount'] > data['Save Files']['Exp Per Level'][f"{data['Save Files'][loaded_file]['User Account']['Exp Level']}"][1]:
        data['Save Files'][loaded_file]['User Account']['Exp Level'] += 1
    
    with open('fbla_game_save_files.json', 'w') as file:
        
        json.dump(data, file, indent=4)
        
def victory_screen():
    global main
    
    while True:
        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        screen.fill((181, 101, 29))
        
        winning_sur = pygame.Surface((16 * 55 * w_ratio, 9 * 55 * h_ratio), pygame.SRCALPHA)
        winning_sur.fill((173, 255, 47, 255))
        
        screen.blit(winning_sur, winning_sur.get_rect(center=(pygame.Surface.get_width(screen) // 2, (pygame.Surface.get_height(screen) // 2) + (75 * h_ratio))))
        
        victory_txt = doto_font_1(int(150 * h_ratio)).render('Victory', False, (255, 255, 51))
        screen.blit(victory_txt, victory_txt.get_rect(center=(pygame.Surface.get_width(screen) // 2, (pygame.Surface.get_height(screen) // 2) - (275 * h_ratio))))
        
        try_again_txt = doto_font_1(int(47 * h_ratio)).render('Retry?', False, black)
        screen.blit(try_again_txt, try_again_txt.get_rect(center=((pygame.Surface.get_width(screen) // 4) + (40 * w_ratio), (pygame.Surface.get_height(screen) // 2) + (100 * h_ratio))))
        
        main_menu_txt = doto_font_1(int(47 * h_ratio)).render('Main Menu', False, black)
        screen.blit(main_menu_txt, main_menu_txt.get_rect(center=((pygame.Surface.get_width(screen) // 4) * 3 - (55 * w_ratio), (pygame.Surface.get_height(screen) // 2) + (100 * h_ratio))))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main = False
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main = False
                    pygame.quit()
                    return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    
                    if (mouse_x - ((pygame.Surface.get_width(screen) // 4) * 3 - (55 * w_ratio))) ** 2 + (mouse_y - (pygame.Surface.get_height(screen) // 2) + (100 * h_ratio)) ** 2 <= 47 ** 2:
                        print('pressed')
                        interface_sound['click'].play()
                        return True
                    
        pygame.display.flip()
        
        clock.tick(fps)

def loser_screen():
    global main
    
    while True:
        
        screen.fill((181, 101, 29))
        
        winning_sur = pygame.Surface((16 * 55 * w_ratio, 9 * 55 * h_ratio), pygame.SRCALPHA)
        winning_sur.fill((255, 195, 47, 255))
        
        screen.blit(winning_sur, winning_sur.get_rect(center=(pygame.Surface.get_width(screen) // 2, (pygame.Surface.get_height(screen) // 2) + (75 * h_ratio))))
        
        victory_txt = doto_font_1(int(150 * h_ratio)).render('You Lost', False, (255, 255, 51))
        screen.blit(victory_txt, victory_txt.get_rect(center=(pygame.Surface.get_width(screen) // 2, (pygame.Surface.get_height(screen) // 2) - (275 * h_ratio))))
        
        try_again_txt = doto_font_1(int(47 * h_ratio)).render('Try Again?', False, black)
        screen.blit(try_again_txt, try_again_txt.get_rect(center=((pygame.Surface.get_width(screen) // 4) + (65 * w_ratio), (pygame.Surface.get_height(screen) // 2) + (100 * h_ratio))))
        
        main_menu_txt = doto_font_1(int(47 * h_ratio)).render('Main Menu', False, black)
        screen.blit(main_menu_txt, main_menu_txt.get_rect(center=((pygame.Surface.get_width(screen) // 4) * 3 - 55, (pygame.Surface.get_height(screen) // 2) + (100 * h_ratio))))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main = False
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main = False
                    pygame.quit()
                    return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    interface_sound['click'].play()
                    return True
                    
        pygame.display.flip()
        
        clock.tick(fps)

#Objects


class Player(pygame.sprite.Sprite):

    def __init__(self, shape, position, a):
        pygame.sprite.Sprite.__init__(self)
        self.position = pygame.Vector2(position)

        if shape == 'Circle':
            self.image = pygame.Surface((75, 75))
            self.image.fill((0, 255, 0))

            pygame.draw.circle(self.image, (0, 0, 255), (37.5, 37.5), 37.5)
            pygame.draw.circle(self.image, black, (37.5, 37.5), 37.5, 2)
            self.image.set_colorkey((0, 255, 0))
            self.loss_energy = -.75

        if shape == 'Rectangle':
            self.image = pygame.Surface((75, 75))
            self.image.fill((111, 50, 81))
            pygame.draw.rect(self.image, black, (0, 0, 75, 75), 2)
            self.loss_energy = -0.25

        if shape == 'Triangle':
            self.image = pygame.Surface((75, 75))
            self.image.fill((0, 255, 0))
            pygame.draw.polygon(self.image, (111, 50, 81), ((0, 75), (75, 75), (37.5, 10.05)))
            pygame.draw.polygon(self.image, black, ((0, 73), (73, 73), (37.5, 10.05)), 2)
            self.image.set_colorkey((0, 255, 0))
            self.loss_energy = -0.25

        self.image_set = self.image
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.acceleration = pygame.Vector2(a)
        self.falling_bool = True
        self.bouncy_bool = True
        self.time = 0
        self.angle = 0
        self.side_momentum = 0

    def falling(self):
        x_val, y_val = self.return_position()
        if self.falling_bool:
            #Gravity
            self.acceleration += (grid[y_val][x_val][gravity_index].x * delta_time, grid[y_val][x_val][gravity_index].y * delta_time)
        #Air Resistance
        self.acceleration += (grid[y_val][x_val][air_resistance_index].x * delta_time, grid[y_val][x_val][air_resistance_index].y * delta_time)

    def updating_position(self):
        self.position += self.acceleration
    
    def return_position(self):
        x_val = int(self.position.x // outer_per_x)
        y_val = int(self.position.y // outer_per_y)
        if y_val < 0:
            y_val = 0
        if y_val > len(grid) - 1:
            y_val = len(grid) - 1
        if x_val < 0:
            x_val = 0
        if x_val > len(grid[y_val]) - 1:
            x_val = len(grid[y_val]) - 1  
        return (x_val, y_val)
    
    def detecting_collition(self):
        
        bounced = False
        
        x_val, y_val = self.return_position()
        
        if y_val + 1 <= len(grid) - 1:
            if grid[y_val + 1][x_val][solid_bool_index] == 1:
                if grid[y_val + 1][x_val][key_grid_index] == 'b':
                    self.loss_energy = -0.95
                else:
                    self.loss_energy = -0.75
                if self.rect.bottom > outer_per_y * (y_val + 1) and (outer_per_x * x_val <= self.position.x <= (outer_per_x * x_val) + outer_per_x):
                    self.acceleration.y = self.acceleration.y * self.loss_energy
                    self.side_momentum = self.side_momentum - (self.side_momentum * 0.05)
                    self.position.y = ((y_val + 1) * outer_per_y) - (37.5 * h_ratio)
                    bounced = True
                    if grid[y_val][x_val][2].y > 0 and -2.5 * h_ratio < self.acceleration.y < 0:
                        self.acceleration.y = 0
                        self.falling_bool = False
        
        if y_val - 1 >= 0:
            if grid[y_val - 1][x_val][solid_bool_index] == 1:
                if grid[y_val - 1][x_val][key_grid_index] == 'b':
                    self.loss_energy = -0.95
                else:
                    self.loss_energy = -0.75
                if self.rect.top < (outer_per_y * (y_val - 1)) + outer_per_y and (outer_per_x * x_val <= self.position.x <= (outer_per_x * x_val) + outer_per_x):
                    self.acceleration.y = self.acceleration.y * self.loss_energy
                    self.position.y = (((y_val - 1) * outer_per_y) + outer_per_y) + (37.5 * h_ratio)
                    bounced = True
                    if grid[y_val][x_val][2].y < 0 and 0 < self.acceleration.y < 2.5 * w_ratio:
                        self.acceleration.y = 0
                        self.falling_bool = False
        
        if x_val + 1 <= len(grid[y_val]) - 1:
            if grid[y_val][x_val + 1][solid_bool_index] == 1:
                if grid[y_val][x_val + 1][key_grid_index] == 'b':
                    self.loss_energy = -0.95
                else:
                    self.loss_energy = -0.75
                if self.rect.right > outer_per_x * (x_val + 1) and (outer_per_y * y_val <= self.position.y <= (outer_per_y * y_val) + outer_per_y):
                    self.acceleration.x = self.acceleration.x * self.loss_energy
                    self.position.x = ((x_val + 1) * outer_per_x) - 37.5 * w_ratio
                    bounced = True
                    if grid[y_val][x_val][2].x > 0 and -2.5 * w_ratio < self.acceleration.x < 0:
                        self.acceleration.x = 0
                        self.falling_bool = False
                    
        if x_val - 1 >= 0:
            if grid[y_val][x_val - 1][solid_bool_index] == 1:
                if grid[y_val][x_val - 1][key_grid_index] == 'b':
                    self.loss_energy = -0.95
                else:
                    self.loss_energy = -0.75
                if self.rect.left < (outer_per_x * (x_val - 1)) + outer_per_x and (outer_per_y * y_val <= self.position.y <= (outer_per_y * y_val) + outer_per_y):
                    self.acceleration.x = self.acceleration.x * self.loss_energy
                    self.position.x = (outer_per_x * (x_val - 1)) + outer_per_x + (37.5 * w_ratio)
                    bounced = True
                    if grid[y_val][x_val][2].x < 0 and 0 < self.acceleration.x < 2.5 * h_ratio:
                        self.acceleration.x = 0
                        self.falling_bool = False
                    
        
        self.loss_energy = -0.75
        
        if self.rect.bottom > pygame.Surface.get_height(object_overlay):
            self.acceleration.y = self.acceleration.y * self.loss_energy
            self.side_momentum = self.side_momentum - (self.side_momentum * 0.05)
            self.position.y = pygame.Surface.get_height(object_overlay) - 37.5 * h_ratio
            bounced = True
            if grid[y_val][x_val][2].y > 0 and -2.5 * h_ratio < self.acceleration.y < 0:
                self.acceleration.y = 0
                self.falling_bool = False
        if self.rect.right > pygame.Surface.get_width(object_overlay):
            self.acceleration.x = self.acceleration.x * self.loss_energy
            self.position.x = pygame.Surface.get_width(object_overlay) - 37.5 * w_ratio
            bounced = True
            if grid[y_val][x_val][2].x > 0 and -2.5 * h_ratio < self.acceleration.x < 0:
                self.acceleration.x = 0
                self.falling_bool = False
        if self.rect.left < 0:
            self.acceleration.x = self.acceleration.x * self.loss_energy
            self.position.x = 37.5 * w_ratio
            bounced = True
            if grid[y_val][x_val][2].x < 0 and 0 < self.acceleration.x < 2.5 * h_ratio:
                self.acceleration.x = 0
                self.falling_bool = False
        if self.rect.top < 0:
            self.acceleration.y = self.acceleration.y * self.loss_energy
            self.position.y = 37.5 * h_ratio
            bounced = True
            if grid[y_val][x_val][2].y < 0 and 0 < self.acceleration.y < 2.5 * h_ratio:
                self.acceleration.y = 0
                self.falling_bool = False
                
        if bounced:
            sfx['bounce'].play()

    #First Friction Attempt

    # def friction(self):

        # if self.acceleration.y == 0 and self.acceleration.x > 0:
            # self.acceleration.x -= .01 * w_ratio
        # if self.acceleration.y == 0 and self.acceleration.x < 0:
            # self.acceleration.x += .01 * w_ratio
        # if -0.01 * w_ratio < self.acceleration.x < 0.01 * w_ratio:
            # self.acceleration.x = 0
    
    def friction(self):
        if self.acceleration.y == 0 and self.acceleration.x != 0:
            friction_force = 0.01 * w_ratio
            if self.acceleration.x > 0:
                self.acceleration.x -= friction_force
            else:
                self.acceleration.x += friction_force

            if abs(self.acceleration.x) < 1e-6:
                self.acceleration.x = 0


    def checking_surface(self, obstacles):
    
        x_val, y_val = self.return_position()
        
        if y_val + 1 <= len(grid) - 1:
            if grid[y_val + 1][x_val][solid_bool_index] == 0 and grid[y_val][x_val][gravity_index].y > 0:
                self.falling_bool = True
            
        if y_val - 1 >= 0:
            if grid[y_val - 1][x_val][solid_bool_index] == 0 and grid[y_val][x_val][gravity_index].y < 0:
                self.falling_bool = True
            
        if x_val + 1 <= len(grid[y_val]) - 1:
            if grid[y_val][x_val + 1][solid_bool_index] == 0 and grid[y_val][x_val][gravity_index].x < 0:
                self.falling_bool = True
            
        if x_val - 1 >= 0:
            if grid[y_val][x_val - 1][solid_bool_index] == 0 and grid[y_val][x_val][gravity_index].x > 0:
                self.falling_bool = True
            
    def updating_image(self):
        self.image = pygame.transform.scale(pygame.transform.rotate(self.image_set, self.angle), (pygame.Surface.get_width(self.image_set) * w_ratio, pygame.Surface.get_height(self.image_set) * h_ratio))
        self.rect = self.image.get_rect()
        #self.position = pygame.Vector2(self.position.x * w_ratio, self.position.y * h_ratio)
        self.rect.center = self.position
        self.update()

class Blocks(pygame.sprite.Sprite):

    def __init__(self, position, type_block):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((75 * w_ratio, 75 * h_ratio))
        self.set_image = self.image
        self.position = pygame.Vector2(position)
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.type_block = type_block
        if type_block == 'normal':
            self.block_color = (130, 130, 130, 255)
        if type_block == 'kill_zone':
            self.block_color = (255, 0, 0, 175)
        if type_block == 'hard':
            self.block_color = (50, 50, 50, 255)
        if type_block == 'hard_bouncy':
            self.block_color = (0, 255, 127, 255)
        if type_block == 'normal_bouncy':
            self.block_color = (0, 255, 127, 180)
        if type_block == 'end_block':
            self.block_color = (0, 255, 0, 255)

    def drawing(self):
        
        out_set = [(0, outer_per_y), (outer_per_x, 0), (outer_per_x, outer_per_y), (0, 0)]
        in_set = [(0, inner_per_y), (inner_per_x, 0), (inner_per_x, inner_per_y), (0, 0)]
        for z in range(4):
            point_out = (self.position.x * outer_per_x + out_set[z][0], self.position.y * outer_per_y + out_set[z][1])
            point_in = (self.position.x * inner_per_x + (25 * w_ratio) + in_set[z][0], self.position.y * inner_per_y + (22 * h_ratio) + in_set[z][1])
            
            # pygame.draw.line(object_overlay, black, point_out, point_in, 2)
                    
        pygame.draw.rect(object_overlay, self.block_color, (outer_per_x * self.position.x, outer_per_y * self.position.y, outer_per_x, outer_per_y))
        
        pygame.draw.rect(object_overlay, black, (outer_per_x * self. position.x, outer_per_y * self.position.y, outer_per_x, outer_per_y), 2)
        pygame.draw.rect(level_screen, black,(inner_per_x * self.position.x, inner_per_y * self.position.y, inner_per_x, inner_per_y), 2)
    
    def drawing_lines(self):
        
        main_frame_rect = []
        
        out_set = [(0, outer_per_y), (outer_per_x, 0), (outer_per_x, outer_per_y), (0, 0)]
        in_set = [(0, inner_per_y), (inner_per_x, 0), (inner_per_x, inner_per_y), (0, 0)]
        for z in range(4):
            point_out = (self.position.x * outer_per_x + out_set[z][0], self.position.y * outer_per_y + out_set[z][1])
            point_in = (self.position.x * inner_per_x + (25 * w_ratio) + in_set[z][0], self.position.y * inner_per_y + (22 * h_ratio) + in_set[z][1])
            
            pygame.draw.line(object_overlay, black, point_out, point_in, 2)
        
        
        #pygame.draw.rect(object_overlay, (0, 0, 111), (outer_per_x * self.position.x, outer_per_y * self.position.y, outer_per_x, outer_per_y))
        
        
        
        # pygame.draw.rect(object_overlay, black, (outer_per_x * self. position.x, outer_per_y * self.position.y, outer_per_x, outer_per_y), 2)
        # pygame.draw.rect(level_screen, black,(inner_per_x * self.position.x, inner_per_y * self.position.y, inner_per_x, inner_per_y), 2)
    
    def drawing_polygon(self):
        
        
        if self.position.x * outer_per_x <= center_x and self.position.y * outer_per_y <= center_y:
            
            main_frame_set = [[0, 1, 3], [0, 1, 2]]
            
        if self.position.x * outer_per_x >= center_x and self.position.y * outer_per_y <= center_y:
            
            main_frame_set = [[1, 2, 3], [0, 2, 3]]
            
        if self.position.x * outer_per_x <= center_x and self.position.y * outer_per_y >= center_y:
            
            main_frame_set = [[0, 2, 3], [1, 2, 3]]
            
        if self.position.x * outer_per_x >= center_x and self.position.y * outer_per_y + 5 >= center_y:
            
            main_frame_set = [[0, 1, 2], [0, 1, 3]]
            
        main_frame_rect = []
        
        out_set = [(0, outer_per_y), (outer_per_x, 0), (outer_per_x, outer_per_y), (0, 0)]
        in_set = [(0, inner_per_y), (inner_per_x, 0), (inner_per_x, inner_per_y), (0, 0)]
        for z in range(4):
            point_out = (self.position.x * outer_per_x + out_set[z][0], self.position.y * outer_per_y + out_set[z][1])
            point_in = (self.position.x * inner_per_x + (25 * w_ratio) + in_set[z][0], self.position.y * inner_per_y + (22 * h_ratio) + in_set[z][1])
        
            if z in main_frame_set[0]:
                main_frame_rect.append(point_out)
            if z in main_frame_set[1]:
                main_frame_rect.append(point_in)
        
        main_frame_rect_organized = sort_vertices(main_frame_rect)
        
        pygame.draw.polygon(object_overlay, self.block_color, main_frame_rect_organized)
        
#Stating Variables

main_pressed, ability_pressed, x_pressed, y_pressed, ability_direccion_pressed, ability_activation_pressed = [[], [], [], [], [], []]
ability_index = 0
num_of_abilities = len(ability_keybinds)

ratio()

gravity_earth = 9.81 * h_ratio

#Grid Start-up

width = 6
height = 4

#This is for the color cycles

cycle = 0

#Object Overlay

walls_w_val = 1200 * w_ratio
walls_h_val = (int(500 / 3) * 3) * h_ratio

object_overlay = pygame.Surface((walls_w_val, walls_h_val))
object_overlay.fill((111, 111, 111))
object_overlay.set_colorkey((111, 111, 111))

level_w_val = int((int(1150 / 6) * 6) * w_ratio)
level_h_val = int((int(450 / 3) * 3) * h_ratio)

level_screen = pygame.Surface((level_w_val, level_h_val))

level_screen.fill(purple_level)

rate()

#Animation cycles

main_x_val = -250
secondary_x_val = 2000
angles_cycles = [0] * 33
angles_min = [130, 200, 35, 330, 140, 100, 60, 125, 210, 280, 200, 160, 180, 230, 330, 330, 250, 340, 340, 350, 290, 200, 290, 170, 0, 70, 30, 350, 310, 340, 340, 70, 350, 340, 40, 90, 70, 340, 30, 310, 320, 340, 50]
current_angles = [130, 200, 35, 330, 140, 100, 60, 125, 210, 280, 200, 160, 180, 230, 330, 330, 250, 340, 340, 350, 290, 200, 290, 170, 0, 70, 30, 350, 310, 340, 340, 70, 350, 340, 40, 90, 70, 340, 30, 310, 320, 340, 50]
angles_max = [150, 220, 65, 360, 180, 150, 100, 155, 240, 320, 240, 200, 210, 300, 360, 360, 300, 370, 380, 370, 330, 230, 330, 190, 30, 100, 50, 370, 340, 370, 380, 90, 370, 380, 90, 120, 100, 380, 70, 350, 360, 380, 70]
min_distance_for_lines = 225
current_distance_for_lines = 225
max_distance_for_lines = 275

triangles = [
    ['point_1', 'point_2', 'point_3'],
    ['point_1', 'point_2', 'point_4'],
    ['point_1', 'point_3', 'point_5'],
    ['point_1', 'point_5', 'point_4'],
    ['point_3', 'point_2', 'point_6'],
    ['point_2', 'point_4', 'point_7'],
    ['point_2', 'point_7', 'point_6'],
    ['point_4', 'point_8', 'point_7'],
    ['point_7', 'point_8', 'point_9'],
    ['point_3', 'point_6', 'point_10'],
    ['point_3', 'point_11', 'point_10'],
    ['point_3', 'point_11', 'point_5'],
    ['point_7', 'point_12', 'point_9'],
    ['point_7', 'point_12', 'point_6'],
    ['point_6', 'point_13', 'point_12'],
    ['point_6', 'point_14', 'point_13'],
    ['point_6', 'point_14', 'point_10'],
    ['point_10', 'point_15', 'point_14'],
    ['point_10', 'point_15', 'point_16'],
    ['point_10', 'point_16', 'point_11'],
    ['point_11', 'point_17', 'point_16'],
    ['point_11', 'point_18', 'point_17'],
    ['point_11', 'point_5', 'point_18'],
    ['point_4', 'point_19', 'point_8'],
    ['point_4', 'point_5', 'point_19'],
    ['point_18', 'point_5', 'point_20'],
    ['point_19', 'point_21', 'point_8'],
    ['point_21', 'point_5', 'point_19'],
    ['point_5', 'point_20', 'point_21'],
    ['point_22', 'point_17', 'point_18'],
    ['point_20', 'point_22', 'point_18'],
    ['point_15', 'point_16', 'point_23'],
    ['point_16', 'point_23', 'point_17'],
    ['point_22', 'point_24', 'point_20'],
    ['point_13', 'point_14', 'point_25'],
    ['point_13', 'point_25', 'point_12'],
    ['point_20', 'point_26', 'point_21'],
    ['point_20', 'point_26', 'point_24'],
    ['point_21', 'point_27', 'point_8'],
    ['point_27', 'point_28', 'point_8'],
    ['point_21', 'point_29', 'point_27'],
    ['point_27', 'point_28', 'point_29'],
    ['point_29', 'point_21', 'point_26'],
    ['point_22', 'point_30', 'point_24'],
    ['point_26', 'point_31', 'point_24'],
    ['point_31', 'point_30', 'point_24'],
    ['point_29', 'point_31', 'point_26'],
    ['point_29', 'point_32', 'point_31'],
    ['point_29', 'point_32', 'point_33'],
    ['point_33', 'point_28', 'point_29'],
    ['point_30', 'point_34', 'point_31'],
    ['point_31', 'point_35', 'point_34'],
    ['point_31', 'point_35', 'point_32'],
    ['point_8', 'point_36', 'point_9'],
    ['point_8', 'point_36', 'point_28'],
    ['point_28', 'point_37',  'point_36'],
    ['point_33', 'point_38', 'point_28'],
    ['point_28', 'point_37', 'point_38'],
    ['point_32', 'point_33', 'point_39'],
    ['point_33', 'point_38', 'point_39'],
    ['point_39', 'point_40', 'point_32'],
    ['point_35', 'point_40', 'point_32'],
    ['point_35', 'point_41', 'point_34'],
    ['point_35', 'point_40', 'point_41'],
    ['point_40', 'point_42', 'point_41'],
    ['point_39', 'point_43', 'point_40'],
    ['point_40', 'point_42', 'point_43'],
    ['point_39', 'point_43', 'point_38'],
    ['point_38', 'point_44', 'point_37'],
    ['point_38', 'point_44', 'point_43']
]

#Grid will hold a list, Index 0 If solid, index 1 air direccion depending on the direccion, 
#it will act accordinly, index 2 gravity, index 3 if solid then object, index 4 if changeble.

solid_bool_index = 0
air_resistance_index = 1
gravity_index = 2
object_index = 3
changeble_index = 4
key_grid_index = 5

#Starting Main Loop

main = True

screen.fill(white)

obstacles_group = pygame.sprite.Group()

def main_loop():
    global ability_index, main
    
    selected_grid = [(0, 0)]
    selected_ability = None
    setting_audio()
    
    while True:

        Drawing_Envieroment(obstacles_group)

        main_object.falling()
        main_object.detecting_collition()
        main_object.updating_position()
        main_object.friction()
        main_object.checking_surface(obstacles_group)
        main_object.updating_image()
        
        main_object_group.update()
        obstacles_group.update()
        
        main_pressed, ability_pressed, x_pressed, y_pressed, ability_direccion_pressed, ability_activation_pressed = activating_grid()
        
        decision = deciding_grid(x_pressed, y_pressed)
        selecting_ability(ability_pressed, ability_direccion_pressed)
        
        if len(x_pressed) > 0 or len(y_pressed) > 0:
            
            decision = deciding_grid(x_pressed, y_pressed)
            
            if len(x_pressed) > 0 and not len(y_pressed) > 0:
                
                selected_grid = []
                
                for y in range(height):
                    selected_grid.append((select_grid(decision[0], decision[1])[0], y))
                    
            if len(y_pressed) > 0 and not len(x_pressed) > 0:
                
                selected_grid = []
                
                for x in range(width):
                    selected_grid.append((x, select_grid(decision[0], decision[1])[1]))
                    
            if len(y_pressed) > 0 and len(x_pressed) > 0:
                    
                selected_grid = [(select_grid(decision[0], decision[1])[0], select_grid(decision[0], decision[1])[1])]
                
        else:
            
            selected_grid = []
        
        if main_object.return_position() == end_point:
            
            if victory_screen():
                return True
        
        for obj in obstacles_group:
            if obj.position == main_object.return_position() and grid[int(obj.position.y)][int(obj.position.x)][key_grid_index] == 'k':
                
                if loser_screen():
                    return True
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main = False
                pygame.quit()
                return False
            if event.type == pygame.VIDEOEXPOSE or event.type == pygame.VIDEORESIZE:
                Updating_Screen()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main = False
                    pygame.quit()
                    return False
                if event.key == actual_keybinds['ability_slot_up'][0]:

                    ability_index += 1

                    if ability_index >= num_of_abilities:

                        ability_index = 0

                elif event.key == actual_keybinds['ability_slot_down'][0]:

                    ability_index -= 1

                    if ability_index < 0:

                        ability_index = num_of_abilities - 1
                
                if event.key == actual_keybinds['ability_activate'][0]:
                    for point in selected_grid:
                        if grid[point[1]][point[0]][changeble_index] == True:
                            if selected_ability == None:
                                pass
                            if selected_ability == 'gravity_switch':
                                grid[point[1]][point[0]][gravity_index] *= -1
                            if selected_ability == 'side_ways':
                                save_y = grid[point[1]][point[0]][gravity_index].y
                                grid[point[1]][point[0]][gravity_index].y = grid[point[1]][point[0]][gravity_index].x
                                grid[point[1]][point[0]][gravity_index].x = save_y
                            if selected_ability == 'gravity_up':
                                if 0 < grid[point[1]][point[0]][gravity_index].x < 10:
                                    grid[point[1]][point[0]][gravity_index].x += 1
                                if 0 < grid[point[1]][point[0]][gravity_index].y < 10:
                                    grid[point[1]][point[0]][gravity_index].y += 1
                            if selected_ability == 'gravity_down':
                                if 0 < grid[point[1]][point[0]][gravity_index].x < 10:
                                    grid[point[1]][point[0]][gravity_index].x -= 1
                                if 0 < grid[point[1]][point[0]][gravity_index].y < 10:
                                    grid[point[1]][point[0]][gravity_index].y -= 1
                            if selected_ability == 'solid' and point != main_object.return_position() and point != end_point:
                                if isinstance(grid[point[1]][point[0]][object_index], Blocks):
                                    grid[point[1]][point[0]][object_index].kill()
                                    grid[point[1]][point[0]][object_index] = None
                                    grid[point[1]][point[0]][solid_bool_index] = 0
                                else:
                                    obj = Blocks((point[0], point[1]), 'normal')
                                    obstacles_group.add(obj)
                                    grid[point[1]][point[0]][object_index] = obj
                                    grid[point[1]][point[0]][solid_bool_index] = 1
                            if selected_ability == 'bouncy_1' and point != main_object.return_position() and point != end_point:
                                if isinstance(grid[point[1]][point[0]][object_index], Blocks):
                                    grid[point[1]][point[0]][object_index].kill()
                                    grid[point[1]][point[0]][object_index] = None
                                    grid[point[1]][point[0]][solid_bool_index] = 0
                                else:
                                    obj = Blocks((point[0], point[1]), 'normal_bouncy')
                                    obstacles_group.add(obj)
                                    grid[point[1]][point[0]][object_index] = obj
                                    grid[point[1]][point[0]][solid_bool_index] = 1
                                
                
                if event.key == actual_keybinds['gravity_switch'][0]:

                    selected_ability = 'gravity_switch'
                    
                if event.key == actual_keybinds['side_ways'][0]:
                    
                    selected_ability = 'side_ways'
                    
                if event.key == actual_keybinds['gravity_up'][0]:
                    
                    selected_ability = 'gravity_up'
                    
                if event.key == actual_keybinds['gravity_down'][0]:
                    
                    selected_ability = 'gravity_down'
                    
                if event.key == actual_keybinds['swirl_left'][0]:
                    
                    selected_ability = 'swirl_left'
                    
                if event.key == actual_keybinds['swirl_right'][0]:
                    
                    selected_ability = 'swirl_right'
                    
                if event.key == actual_keybinds['swirl_left'][0]:
                    
                    selected_ability = 'swirl_left'
                    
                if event.key == actual_keybinds['solid'][0]:
                    
                    selected_ability = 'solid'
                    
                if event.key == actual_keybinds['bouncy_1'][0]:
                    
                    selected_ability = 'bouncy_1'
                    
                    

        pygame.display.flip()

        clock.tick(fps)

if __name__ == '__main__':
    pygame.mixer.music.load(menu_music_path)
    pygame.mixer.music.play(-1)
    if Start_Screen_Display():
        if Choose_Your_Save_File_Screen_Display():
            write_your_username()
            while main:
                if Main_Menu():
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(ingame_music_path)
                    pygame.mixer.music.play(-1)
                    setting_audio()
                    while main_loop():
                        pass
                    if main:
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load(menu_music_path)
                        pygame.mixer.music.play(-1)