# Настройки игры
GAME_CONFIG = {
    "min_number": 1,
    "max_number": 100,
    "max_attempts": 20,
    "language": "ru"
}

DIFFICULTY_LEVELS = {
    "easy": {"min": 1, "max": 50},
    "medium": {"min": 1, "max": 100},
    "hard": {"min": 1, "max": 200}
}

def get_difficulty_settings(level):
    """Возвращает настройки для выбранного уровня сложности"""
    return DIFFICULTY_LEVELS.get(level, DIFFICULTY_LEVELS["medium"])