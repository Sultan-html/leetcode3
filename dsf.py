class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()


sol = Solution()
print(sol.toLowerCase("Hello"))  # Output: "hello"
print(sol.toLowerCase("here"))   # Output: "here"
print(sol.toLowerCase("LOVELY")) # Output: "lovely"
