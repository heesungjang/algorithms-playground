def isPalindrome(s: str) -> bool:
    target_str = []

    for char in s:
        # if character is not alphabet or number
        if char.isalnum():
            target_str.append(char.lower())

    left_pointer = 0
    right_pointer = len(target_str) - 1

    while left_pointer < right_pointer:
        if target_str[left_pointer] != target_str[right_pointer]:
            return False
        left_pointer += 1
        right_pointer -= 1

    return True


s = "A man, a plan, a canal: Panama"
isPalindrome(s)
