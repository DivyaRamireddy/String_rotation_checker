# string_rotation_checker.py

def are_rotations(str1, str2):
    """
    Two strings are rotations if:
    str2 is a substring of str1+str1

    Example:
    str1 = "abcde"
    str2 = "cdeab"   (rotation)
    """
    if len(str1) != len(str2):
        return False

    # Key logic used in interviews
    combined = str1 + str1

    return str2 in combined


if __name__ == "__main__":
    print("🔄 String Rotation Checker 🔄")
    print("-----------------------------")

    s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")

    if are_rotations(s1, s2):
        print(f"'{s2}' IS a rotation of '{s1}' ✔️")
    else:
        print(f"'{s2}' is NOT a rotation of '{s1}' ❌")
