from typing import List, Optional, Dict, Any


def to_flat_dict(self) -> Dict:
    """Converts Context Table into flat dict where items in columns[0] = Keys, columns[1] = Values

    :return: Dict
    """
    result = {}

    if not self.table:
        return result

    result = {self.table.headings[0]: self.table.headings[1]}
    for row in self.table.rows:
        result[row.cells[0]] = row.cells[1]

    return result
