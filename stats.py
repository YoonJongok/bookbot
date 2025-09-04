from collections import defaultdict
from typing import Dict, List, Any

def get_num_words(text:str) -> int:
    words_count: list[str] = text.split()
    return len(words_count)


def get_charactor_frequency(text:str) -> Dict[str, int]:
    lower_text = text.lower()
    frequency_dict: defaultdict[str, int]  = defaultdict(int)

    for letter in lower_text:
        frequency_dict[letter] += 1

    return dict(frequency_dict)



# 헬퍼 함수: 딕셔너리의 'num' 키 값을 반환
def sort_on(d: Dict[str, Any]) -> int:
    """정렬을 위한 헬퍼 함수로, 딕셔너리에서 'num' 키의 값을 반환합니다."""
    return d["num"]

def sort_characters(char_count_dict: Dict[str, int]) -> List[Dict[str, Any]]:
    """
    문자 빈도수 딕셔너리를 'num' 값에 따라 내림차순으로 정렬된 리스트로 반환합니다.

    Args:
        char_count_dict: 각 문자의 빈도수를 담고 있는 딕셔너리입니다.

    Returns:
        정렬된 딕셔너리 리스트입니다. 각 딕셔너리는 {"char": 문자, "num": 빈도수} 형태입니다.
    """
    # 1. 빈도수가 0이 아닌 알파벳 문자만 필터링하여 리스트에 담습니다.
    #    각 항목은 {"char": 문자, "num": 빈도수} 형태의 딕셔너리입니다.
    #    문자열의 .isalpha() 메서드를 사용해 알파벳인지 확인합니다.
    char_list: List[Dict[str, Any]] = [
        {"char": char, "num": count}
        for char, count in char_count_dict.items()
        if char.isalpha()
    ]

    # 2. 리스트를 `sort_on` 헬퍼 함수를 기준으로 내림차순 정렬합니다.
    #    reverse=True를 사용해 가장 큰 값부터 오게 만듭니다.
    char_list.sort(key=sort_on, reverse=True)
    

    return char_list