from typing import Any

import threading


def singleton(cls: Any):
    """
    싱글톤 기능을 제공하는 애노테이션 함수

    :param Any cls:
    :return:
    """
    instances = {}

    # 멀티 스레드 환경에서 인스턴스에 접근하는 것을 고려
    lock = threading.Lock()

    def get_instance(*args, **kwargs):
        if cls not in instances:
            with lock:
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

