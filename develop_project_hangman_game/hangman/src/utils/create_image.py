import os
from PIL import Image, ImageDraw

"""
본 프로젝트에서는 활용하지 않는 기능 및 파일입니다.
"""


# 디렉토리 생성
output_dir = './resources/imgs'
os.makedirs(output_dir, exist_ok=True)


def draw_hangman(stage):
    # 이미지 크기 설정
    width, height = 400, 270
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)

    # 그림 요소 그리기
    if stage > 0:
        draw.line((100, 250, 300, 250), fill='black', width=3)  # Base

    if stage > 1:
        draw.line((200, 250, 200, 50), fill='black', width=3)  # Pole

    if stage > 2:
        draw.line((200, 50, 300, 50), fill='black', width=3)  # Top Bar
        draw.line((300, 50, 300, 80), fill='black', width=3)  # Rope

    if stage > 3:
        draw.ellipse((290, 80, 310, 100), outline='black', width=3)  # Head

    if stage > 4:
        draw.line((300, 100, 300, 110), fill='black', width=3)  # Neck

    if stage > 5:
        draw.line((300, 110, 270, 160), fill='black', width=3)  # Left Arm

    if stage > 6:
        draw.line((300, 110, 330, 160), fill='black', width=3)  # Right Arm

    if stage > 7:
        draw.line((300, 110, 300, 180), fill='black', width=3)  # Body

    if stage > 8:
        draw.line((300, 180, 270, 230), fill='black', width=3)  # Left Leg

    if stage > 9:
        # 왼쪽 다리
        draw.line((300, 180, 270, 230), fill='black', width=3)

    if stage == 10:
        # 오른쪽 다리
        draw.line((300, 180, 330, 230), fill='black', width=3)

    return img


# Draw and save each stage
for i in range(11):
    img = draw_hangman(i)
    img.save(os.path.join(output_dir, f'hangman_{i}.jpg'))

print("Images saved successfully.")
