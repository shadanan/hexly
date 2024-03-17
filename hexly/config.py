from dataclasses import dataclass


@dataclass
class Config:
    table_id: int = 0
    max_rows: int = 0x100

    def get_unique_table_id(self):
        self.table_id += 1
        return self.table_id


config = Config()


def set_max_rows(max_rows: int) -> None:
    config.max_rows = max_rows
