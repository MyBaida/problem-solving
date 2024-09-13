class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        output = []
        word1 = set(words[0])

        for letter in word1:
            frequency = min([word.count(letter) for word in words])
            output.extend(frequency*[letter])
        return output
