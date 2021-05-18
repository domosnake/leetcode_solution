class Solution:
    # one pass, O(n) time
    # really don't need to store all paths since we only return max length
    def longestPath(self, s: str) -> int:
        entries = s.split('\n')
        # stack to track parent dir and level, root level is -1
        stack = [(-1, '')]
        # paths for all entries
        paths = []
        maxLen = -1
        for e in entries:
            level = self.countLevel(e)
            parent_level, parent_dir = stack[-1]
            # trim spaces
            e = e.strip()
            # popping until correct parent dir is found
            while level <= parent_level:
                stack.pop()
                parent_level, parent_dir = stack[-1]

            path = parent_dir + '/' + e
            paths.append(path)
            # dir
            if self.isDir(e):
                stack.append((level, path))
            # image file
            elif self.isImageFile(e):
                # update max path length for image files
                maxLen = max(maxLen, len(path))

        return maxLen

    def countLevel(self, s):
        space = 0
        for c in s:
            if c == ' ':
                space += 1
            else:
                break
        return space

    def isDir(self, s):
        return '.' not in s

    def isImageFile(self, s):
        return '.jpeg' in s or '.png' in s or '.gif' in s


filestr = '''dir1
 dir11
 dir12
  picture.jpeg
  dir121
   googleimage.png
 file1.txt
dir2
 verylongfilename2.gif'''
s = Solution()
a = s.longestPath(filestr)
# '/dir2/verylongfilename2.gif' = 27
print(a)
