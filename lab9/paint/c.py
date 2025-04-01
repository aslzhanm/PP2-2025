import pygame as pg

pg.init()

width, height = 800 , 600
screen = pg.display.set_mode((width, height)) # окно орнату
pg.display.set_caption("paint sultan")

white, green, red, blue, black = (255, 255, 255), (0, 255, 0), (255, 0, 0), (0, 0, 255), (0, 0, 0)

curent_color = black

drawing = False
mode = "pen"

running = True
screen.fill(white) # Экранды ақ түспен бояу (таза күйде бастау)

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT: # Егер қолданушы Quit батырмасын басса
            running = False
        
        elif event.type == pg.KEYDOWN: # Пернетақтадағы батырмаларға жауап беру
            if event.key == pg.K_r:
                mode = "rect"
            if event.key == pg.K_c:
                mode = "circle"
            if event.key == pg.K_e:
                mode = "eraser" 
            if event.key == pg.K_p:
                mode = "pen"
            if event.key == pg.K_s:
                mode = "square"
            if event.key == pg.K_t:
                mode = "triangle"
            if event.key == pg.K_z:
                mode = "equilateral"
            if event.key == pg.K_x:
                mode = "rhombus"
            
            if event.key == pg.K_1:
                curent_color = black
            if event.key == pg.K_2:
                curent_color = red
            if event.key == pg.K_3:
                curent_color = blue
            if event.key == pg.K_4:
                curent_color = green
        
        elif event.type == pg.MOUSEBUTTONDOWN:  # Егер тінтуірдің сол жақ батырмасы басылса – сурет сала бастаймыз
            if event.button == 1:
                drawing = True
                basu_pos = event.pos
        
        elif event.type == pg.MOUSEMOTION: # Егер mouse қозғалып жатса
            if drawing:
                if mode == "pen":
                    pg.draw.line(screen, curent_color, basu_pos, event.pos, 5)
                    basu_pos = event.pos # Соңғы координатаны жаңарту
                if mode == "eraser":
                    pg.draw.circle(screen, white, event.pos, 10)
                    
        
                    
        elif event.type == pg.MOUSEBUTTONUP: # Егер тінтуір батырмасы жіберілсе – сызуды аяқтаймыз
            if event.button == 1:
                drawing = False  
                last_pos = event.pos # мышка жібергеннен кейінгі кордината
                x1, y1 = basu_pos
                x2, y2 = last_pos
                if mode == "rect":
                    
                    left = min(x1, x2)
                    top = min(y1, y2)
                    width = abs(x1-x2)
                    height = abs(y1-y2)
                    
                    # pos_dim = pg.Rect(basu_pos, ((last_pos[0] - basu_pos[0]), (last_pos[1] - basu_pos[1])))
                    pg.draw.rect(screen, curent_color, (left, top, width, height), 2)
                
                if mode == "circle":
                    radius = ((last_pos[0] - basu_pos[0])**2 + (last_pos[1] - basu_pos[1])**2 ) ** 0.5
                    pg.draw.circle(screen, curent_color, basu_pos, radius, 2)
                    
                if mode == "square":
                    side = min(abs(last_pos[0]-basu_pos[0]), abs(last_pos[1]-basu_pos[1]))
                    rect = pg.Rect(basu_pos, (side, side))
                    pg.draw.rect(screen, curent_color, rect, 2)
                    
                if mode == "triangle":
                    triangle_points = [(x1, y1), (x2, y2), (x1, y2)]
                    pg.draw.polygon(screen, curent_color, triangle_points, 2)
                
                if mode == "equilateral":
                    side = abs(x2 - x1)  # қабырғасын есептеу
                    height = int(side * (3 ** 0.5) / 2)  # Биіктігін есептеу
                    triangle_points = [(x1, y1), (x1 + side, y1), (x1 + side // 2, y1 - height)]  # Үшбұрыштың нүктесі
                    pg.draw.polygon(screen, curent_color, triangle_points, 2)
                    
                if mode == "rhombus":
                    width = abs(x2-x1)
                    height = abs(y2-y1)
                    centerx = (x1+x2) // 2
                    centery = (y1+y2) // 2
                    
                    rhombus_p = [
                        (centerx, y1),
                        (x1, centery),
                        (centerx, y2),
                        (x2, centery)
                    ]
                    pg.draw.polygon(screen, curent_color, rhombus_p, 2)
                    
                    
                     
    pg.display.flip() # Экранды жаңарту барлық өзгерістерді көрсету
pg.quit()