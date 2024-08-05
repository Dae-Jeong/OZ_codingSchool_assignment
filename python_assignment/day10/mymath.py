import math

def triangle_area(base, height):
    """
    삼각형의 넓이를 계산하는 함수
    
    :param base: 밑변의 길이
    :param height: 높이
    :return: 삼각형의 넓이
    """
    area = 0.5 * base * height
    return area

def circle_area(radius):
    """
    원의 넓이를 계산하는 함수
    
    :param radius: 원의 반지름
    :return: 원의 넓이
    """
    area = math.pi * radius ** 2
    return area

def rectangular_prism_area(length, width, height):
    """
    직육면체의 넓이를 계산하는 함수
    
    :param length: 직육면체의 길이
    :param width: 직육면체의 폭
    :param height: 직육면체의 높이
    :return: 직육면체의 넓이
    """
    area = 2 * (length * width + width * height + height * length)
    return area