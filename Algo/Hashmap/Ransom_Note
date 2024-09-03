def canConstruct(self, ransomNote, magazine):
      """
      :type ransomNote: str
      :type magazine: str
      :rtype: bool
      """
      dict = {}

      for char in magazine:
          if char in dict:
              dict[char] +=1
          else:
              dict[char] = 1
      
      for char in ransomNote:
          if char in dict and dict[char] > 0:
              dict[char] -= 1
          else:
              return False
      
      return True
print(canConstruct("ab","aab"))
