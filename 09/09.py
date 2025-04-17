"""
Kotitehtävät 9

"""

from __future__ import annotations
from typing import List, Optional


class Keppihevonen:
    """Simple model of a hobby‑horse (stick horse)."""

    def __init__(self, name: str, color: str, owner: str, age: int):
        self.name = name
        self.color = color
        self.owner = owner
        self.age = age

    # ------------------------
    # Homework 9 – task 1
    # ------------------------
    def save(self, file):
        """Write this horse in CSV form to *file*.

        Parameters
        ----------
        file : TextIO
            Must be **open for writing**. The method uses an assert
            to ensure that and **does not close** the file.
        """
        # Verify caller obeys contract
        assert not file.closed and file.writable(), "File must be open for writing"

        # CSV on one line; newline handled here, not in caller
        record = f"{self.name},{self.color},{self.owner},{self.age}\n"
        file.write(record)

    # ------------------------
    # Homework 9 – task 2
    # ------------------------
    @staticmethod
    def load(file) -> Optional["Keppihevonen"]:
        """Read **one** horse from *file* and return it.

        Returns None on EOF.

        Parameters
        ----------
        file : TextIO
            Must be **open for reading**. Uses assert and
            **does not close** the file.
        """
        assert not file.closed and file.readable(), "File must be open for reading"

        line = file.readline()
        if line == "":  # EOF
            return None

        parts = [p.strip() for p in line.rstrip("\n").split(",")]
        if len(parts) != 4:
            raise ValueError("Invalid horse record: " + line)

        name, color, owner, age_str = parts
        try:
            age = int(age_str)
        except ValueError as e:
            raise ValueError(f"Invalid age in record: {line}") from e

        return Keppihevonen(name, color, owner, age)

    def __repr__(self) -> str:  # pragma: no cover
        return (
            f"Keppihevonen(name={self.name!r}, color={self.color!r}, "
            f"owner={self.owner!r}, age={self.age})"
        )


class Kepparitalli:
    """A stable that holds multiple *Keppihevonen* instances."""

    def __init__(self, name: str):
        self.name = name
        self.horses: List[Keppihevonen] = []

    def add_horse(self, horse: Keppihevonen) -> None:
        """Add *horse* to this stable."""
        self.horses.append(horse)

    # ------------------------
    # Homework 10 – task 1
    # ------------------------
    def save(self, filename: str) -> None:
        """Write this stable (and all its horses) to *filename*.

        The file is opened *inside* the method and automatically closed.
        """
        with open(filename, "w", encoding="utf-8") as f:
            # Stable header
            f.write(self.name + "\n")
            f.write(f"{len(self.horses)}\n")

            # Each horse uses the method from homework 9
            for horse in self.horses:
                horse.save(f)

    # ------------------------
    # Homework 10 – task 2
    # ------------------------
    @staticmethod
    def load(filename: str) -> "Kepparitalli":
        """Create and return a *Kepparitalli* populated from *filename*."""
        with open(filename, "r", encoding="utf-8") as f:
            stable_name = f.readline().rstrip("\n")

            count_line = f.readline()
            if count_line == "":
                raise ValueError("Missing horse count in file")
            try:
                horse_count = int(count_line.strip())
            except ValueError as e:
                raise ValueError("Invalid horse count") from e

            stable = Kepparitalli(stable_name)

            for i in range(horse_count):
                horse = Keppihevonen.load(f)
                if horse is None:
                    raise ValueError(
                        f"Unexpected EOF after {i} horses (expected {horse_count})"
                    )
                stable.add_horse(horse)

        return stable

    def __repr__(self) -> str:  # pragma: no cover
        return f"Kepparitalli(name={self.name!r}, horses={self.horses})"


# ----------------------------------------------------------------------
# Quick self‑test when run as a script
# ----------------------------------------------------------------------
if __name__ == "__main__":  # pragma: no cover
    stable = Kepparitalli("Aamu‑Talli")
    stable.add_horse(Keppihevonen("Storm", "brown", "Helmi", 4))
    stable.add_horse(Keppihevonen("Blaze", "black", "Oskari", 3))

    demo_file = "demo_stable.txt"
    stable.save(demo_file)
    print("Saved", stable, "to", demo_file)

    loaded = Kepparitalli.load(demo_file)
    print("Loaded", loaded)
