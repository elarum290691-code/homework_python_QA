

class StringUtils:
    def capitalize(self, string: str) -> str:
        return string.capitalize()

    def trim(self, string: str) -> str:
        return string.strip()

    def to_list(self, string: str, delimiter: str = ",") -> list:
        if not string:
            return []
        return string.split(delimiter)

    def contains(self, string: str, symbol: str) -> bool:
        return symbol in string

    def delete_symbol(self, string: str, symbol: str) -> str:
        return string.replace(symbol, "")

    def starts_with(self, string: str, symbol: str) -> bool:
        return string.startswith(symbol)

    def end_with(self, string: str, symbol: str) -> bool:
        return string.endswith(symbol)

    def is_empty(self, string: str) -> bool:
        return len(string.strip()) == 0

    def list_to_string(self, lst: list, joiner: str = ", ") -> str:
        return joiner.join(lst)
