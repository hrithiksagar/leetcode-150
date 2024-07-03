class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 0:
            return []

        row = [1]  # Start with the first row
        for i in range(1, rowIndex + 1):
            new_row = [1]  # Start each row with 1
            for j in range(1, i):
                new_row.append(row[j-1] + row[j])
            new_row.append(1)  # End each row with 1
            row = new_row  # Update the row to the new row

        return row