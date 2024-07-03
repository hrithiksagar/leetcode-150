class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []

        result = [[1]]  # Start with the first row

        for i in range(1, numRows):
            prev_row = result[-1]
            new_row = [1]  # Start each row with 1
            print("Loop 1 end")
            for j in range(1, i):
                new_row.append(prev_row[j-1] + prev_row[j])
                print(new_row)
            new_row.append(1)  # End each row with 1
            print("Appended 1 in end",new_row)
            result.append(new_row)

        return result
