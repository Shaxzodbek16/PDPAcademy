# https://leetcode.com/problems/zigzag-conversion/description/


class Solution:
	def convert(self, s: str, rows: int) -> str:
		pass


def convert(s: str, rows: int) -> str:
	for i in range(0, (int(len(s)/3)), rows):
		print(s[i])
		print(s[i+1])
		print(s[i+2])


if __name__ == '__main__':
	convert("PAYPALISHIRING", 3)
