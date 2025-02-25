import pygame
import random
import time

# 初始化 pygame
pygame.init()

# 屏幕设置
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("点击小球游戏")

# 颜色定义
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 小球设置
ball_radius = 30
ball_x = random.randint(ball_radius, screen_width - ball_radius)
ball_y = random.randint(ball_radius, screen_height - ball_radius)
ball_speed = 5

# 游戏设置
score = 0
game_time = 30  # 游戏时间，单位：秒
start_time = time.time()

# 字体设置
font = pygame.font.SysFont(None, 36)

# 显示分数函数
def display_score():
    score_text = font.render(f"分数: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

# 显示剩余时间函数
def display_time():
    remaining_time = max(0, int(game_time - (time.time() - start_time)))
    time_text = font.render(f"剩余时间: {remaining_time}s", True, WHITE)
    screen.blit(time_text, (screen_width - 200, 10))
    return remaining_time

# 游戏主循环
running = True
while running:
    screen.fill((0, 0, 0))  # 填充背景色
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # 检查点击是否在小球上
            if (mouse_x - ball_x)**2 + (mouse_y - ball_y)**2 <= ball_radius**2:
                score += 1
                # 点击后重新设置小球位置
                ball_x = random.randint(ball_radius, screen_width - ball_radius)
                ball_y = random.randint(ball_radius, screen_height - ball_radius)

    # 显示小球
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    # 更新分数和时间
    display_score()
    remaining_time = display_time()

    # 游戏结束
    if remaining_time == 0:
        game_over_text = font.render(f"游戏结束! 你的得分是: {score}", True, WHITE)
        screen.blit(game_over_text, (screen_width // 2 - 150, screen_height // 2))
        pygame.display.update()
        pygame.time.wait(3000)  # 显示 3 秒钟结束信息
        running = False

    pygame.display.update()  # 更新屏幕

pygame.quit()
