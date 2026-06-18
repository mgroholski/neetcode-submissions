class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        return 'π' + 'π'.join(strs)


    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []

        return s.split('π')[1:]
