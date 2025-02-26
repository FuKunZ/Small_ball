# -*- coding: utf-8 -*-

import pygame
import random
import time
import math

# 默认设置（新增设置参数）
SETTINGS = {
    'background_color': (0, 0, 0),
    'window_size': (800, 600),
    'ball_color': (255, 0, 0),
    'ball_count': 5,
    'ball_radius': 15,
    'speed_range': (1, 3),
    'transparent_bg': False,
    'game_time': 30  # 新增游戏时间设置
}

class Settings:
    def __init__(self):
        self.current = SETTINGS.copy()
        self.original = SETTINGS.copy()

    def reset(self):
        self.current = self.original.copy()

    def apply(self):
        global screen, screen_width, screen_height
        screen_width, screen_height = self.current['window_size']
        screen = pygame.display.set_mode((screen_width, screen_height))
        if self.current['transparent_bg']:
            screen.set_alpha(128)
        else:
            screen.set_alpha(255)

# 初始化 pygame
pygame.init()
screen_width, screen_height = SETTINGS['window_size']
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Click the Balls")

# 颜色定义（使用设置中的颜色）
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

# 使用默认字体
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 28)

class Game:
    def __init__(self):
        self.settings = SETTINGS  # 保存设置引用
        self.reset_game()
    
    def reset_game(self):
        """重置游戏状态"""
        BALL_RADIUS = self.settings['ball_radius']
        self.balls = []
        for _ in range(self.settings['ball_count']):
            while True:
                new_x = random.randint(BALL_RADIUS, screen_width - BALL_RADIUS)
                new_y = random.randint(BALL_RADIUS, screen_height - BALL_RADIUS)
                collision = False
                for ball in self.balls:
                    dx = new_x - ball['x']
                    dy = new_y - ball['y']
                    if dx**2 + dy**2 <= (2 * BALL_RADIUS)**2:
                        collision = True
                        break
                if not collision:
                    angle = random.uniform(0, 2 * math.pi)
                    speed = random.uniform(*self.settings['speed_range'])
                    self.balls.append({
                        'x': new_x,
                        'y': new_y,
                        'vx': speed * math.cos(angle),
                        'vy': speed * math.sin(angle)
                    })
                    break
        self.score = 0
        self.start_time = time.time()
        self.game_over = False
    
    def check_click(self, mouse_pos):
        """检查点击事件"""
        BALL_RADIUS = self.settings['ball_radius']
        for ball in self.balls:
            dx = mouse_pos[0] - ball['x']
            dy = mouse_pos[1] - ball['y']
            if dx**2 + dy**2 <= BALL_RADIUS**2:
                self.score += 1
                # 生成新位置并检查重叠
                while True:
                    new_x = random.randint(BALL_RADIUS, screen_width - BALL_RADIUS)
                    new_y = random.randint(BALL_RADIUS, screen_height - BALL_RADIUS)
                    collision = False
                    for other in self.balls:
                        if other is ball:
                            continue
                        dx_other = new_x - other['x']
                        dy_other = new_y - other['y']
                        if dx_other**2 + dy_other**2 <= (2 * BALL_RADIUS)**2:
                            collision = True
                            break
                    if not collision:
                        angle = random.uniform(0, 2 * math.pi)
                        speed = random.uniform(*self.settings['speed_range'])
                        ball['x'] = new_x
                        ball['y'] = new_y
                        ball['vx'] = speed * math.cos(angle)
                        ball['vy'] = speed * math.sin(angle)
                        break
                break
    
    def update(self, delta_time):
        """更新游戏状态"""
        BALL_RADIUS = self.settings['ball_radius']
        for ball in self.balls:
            # 更新位置
            ball['x'] += ball['vx'] * delta_time
            ball['y'] += ball['vy'] * delta_time
            
            # 边界碰撞检测
            if ball['x'] - BALL_RADIUS < 0 or ball['x'] + BALL_RADIUS > screen_width:
                ball['vx'] *= -1
            if ball['y'] - BALL_RADIUS < 0 or ball['y'] + BALL_RADIUS > screen_height:
                ball['vy'] *= -1
    
    def draw_balls(self):
        """绘制所有小球"""
        BALL_COLOR = self.settings['ball_color']
        BALL_RADIUS = self.settings['ball_radius']
        for ball in self.balls:
            pygame.draw.circle(screen, BALL_COLOR, (int(ball['x']), int(ball['y'])), BALL_RADIUS)
    
    def get_remaining_time(self):
        """获取剩余时间"""
        remaining = max(0, self.settings['game_time'] - (time.time() - self.start_time))
        if remaining == 0:
            self.game_over = True
        return int(remaining)

def show_text(text, y_offset=0, color=WHITE):
    """显示居中文本"""
    text_surface = font.render(text, True, color)
    x = screen_width // 2 - text_surface.get_width() // 2
    y = screen_height // 2 - text_surface.get_height() // 2 + y_offset
    screen.blit(text_surface, (x, y))

def main_menu():
    settings = Settings()
    selected = 0
    menu_items = ["Start Game", "Settings", "Exit"]
    
    while True:
        screen.fill(SETTINGS['background_color'])
        
        # 绘制标题
        title = font.render("BALL CLICKER", True, WHITE)
        screen.blit(title, (screen_width//2 - title.get_width()//2, 100))
        
        # 绘制菜单项
        for i, item in enumerate(menu_items):
            color = WHITE if i == selected else GRAY
            text = font.render(item, True, color)
            x = screen_width//2 - text.get_width()//2
            y = 250 + i * 60
            screen.blit(text, (x, y))
        
        pygame.display.update()
        
        # 事件处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = max(0, selected - 1)
                elif event.key == pygame.K_DOWN:
                    selected = min(len(menu_items)-1, selected + 1)
                elif event.key == pygame.K_RETURN:
                    if selected == 0:
                        game_loop()
                    elif selected == 1:
                        settings_menu(settings)
                    elif selected == 2:
                        pygame.quit()
                        return False

def settings_menu(settings):
    selected = 0
    settings_items = [
        "Background Color",
        "Window Size",
        "Ball Color",
        "Ball Count",
        "Ball Radius",
        "Speed Range",
        "Game Time",
        "Transparent BG",
        "Save & Back",
        "Cancel"
    ]
    
    while True:
        screen.fill(SETTINGS['background_color'])
        
        # 绘制设置标题
        title = font.render("SETTINGS", True, WHITE)
        screen.blit(title, (screen_width//2 - title.get_width()//2, 50))
        
        # 绘制设置项
        for i, item in enumerate(settings_items):
            color = WHITE if i == selected else GRAY
            text = small_font.render(item, True, color)
            
            # 显示当前设置值
            value = ""
            if item == "Background Color":
                value = str(settings.current['background_color'])
            elif item == "Window Size":
                value = str(settings.current['window_size'])
            elif item == "Ball Color":
                value = str(settings.current['ball_color'])
            elif item == "Ball Count":
                value = str(settings.current['ball_count'])
            elif item == "Ball Radius":
                value = str(settings.current['ball_radius'])
            elif item == "Speed Range":
                value = f"{settings.current['speed_range'][0]}-{settings.current['speed_range'][1]}"
            elif item == "Game Time":
                value = str(settings.current['game_time'])
            elif item == "Transparent BG":
                value = str(settings.current['transparent_bg'])
            
            value_text = small_font.render(value, True, GRAY)
            screen.blit(text, (100, 150 + i*40))
            screen.blit(value_text, (screen_width - 200, 150 + i*40))
        
        pygame.display.update()
        
        # 事件处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = max(0, selected - 1)
                elif event.key == pygame.K_DOWN:
                    selected = min(len(settings_items)-1, selected + 1)
                elif event.key == pygame.K_RETURN:
                    if selected == 8:  # Save & Back
                        SETTINGS.update(settings.current)
                        settings.apply()
                        return
                    elif selected == 9:  # Cancel
                        settings.reset()
                        return
                    else:
                        edit_setting(settings, settings_items[selected])
                elif event.key == pygame.K_ESCAPE:
                    settings.reset()
                    return

def edit_setting(settings, item):
    input_text = ""
    while True:
        screen.fill(SETTINGS['background_color'])
        
        # 绘制提示文本
        prompt = small_font.render(f"Enter new {item}:", True, WHITE)
        screen.blit(prompt, (100, 200))
        
        # 绘制输入框
        input_box = pygame.Rect(100, 240, 200, 40)
        pygame.draw.rect(screen, WHITE, input_box, 2)
        input_surface = small_font.render(input_text, True, WHITE)
        screen.blit(input_surface, (input_box.x + 5, input_box.y + 5))
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    try:
                        if item == "Background Color":
                            color = eval(input_text)
                            if len(color) == 3:
                                settings.current['background_color'] = color
                        elif item == "Window Size":
                            size = eval(input_text)
                            if len(size) == 2:
                                settings.current['window_size'] = size
                        elif item == "Ball Color":
                            color = eval(input_text)
                            if len(color) == 3:
                                settings.current['ball_color'] = color
                        elif item == "Ball Count":
                            count = int(input_text)
                            if count > 0:
                                settings.current['ball_count'] = count
                        elif item == "Ball Radius":
                            radius = int(input_text)
                            if radius > 0:
                                settings.current['ball_radius'] = radius
                        elif item == "Speed Range":
                            speed = eval(input_text)
                            if len(speed) == 2:
                                settings.current['speed_range'] = speed
                        elif item == "Game Time":
                            time = int(input_text)
                            if time > 0:
                                settings.current['game_time'] = time
                        elif item == "Transparent BG":
                            settings.current['transparent_bg'] = input_text.lower() == 'true'
                        return
                    except:
                        pass
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

def game_loop():
    game = Game()
    clock = pygame.time.Clock()
    FPS = 60
    
    while True:
        screen.fill(SETTINGS['background_color'])
        delta_time = clock.get_time() / 1000.0
        
        # 事件处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN and not game.game_over:
                game.check_click(pygame.mouse.get_pos())
            elif event.type == pygame.KEYDOWN and game.game_over:
                if event.key == pygame.K_SPACE:
                    game.reset_game()
                elif event.key == pygame.K_ESCAPE:
                    return False
        
        # 游戏逻辑更新
        if not game.game_over:
            game.update(delta_time)
        
        # 绘制界面
        if game.game_over:
            show_text("Game Over", -40)
            show_text(f"Final Score: {game.score}", 0)
            show_text("Press SPACE to restart", 40, GRAY)
            show_text("Press ESC to quit", 80, GRAY)
        else:
            game.draw_balls()
            
            # 显示分数和时间
            score_text = font.render(f"Score: {game.score}", True, WHITE)
            screen.blit(score_text, (10, 10))
            
            remaining_time = game.get_remaining_time()
            time_text = font.render(f"Time: {remaining_time}s", True, WHITE)
            screen.blit(time_text, (screen_width - 220, 10))
        
        pygame.display.update()
        clock.tick(FPS)
    
    return False

if __name__ == "__main__":
    main_menu()
