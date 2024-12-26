# Nonogram Guarantee Checker

A Python-based GUI application that calculates guaranteed cells in a row or column of a nonogram puzzle. WHAT IS A NONOGRAM PUZZLE, YOU MAY ASK??? CHECK IT OUT HERE: https://www.puzzle-nonograms.com/. GREAT FUN TO BE HAD! The application provides a user-friendly interface to input puzzle parameters and visualize guaranteed cells.

## Features

- Calculate guaranteed cells in nonogram rows or columns based on user input.
- Visual representation of guaranteed slots using black (`⬛`) and white (`⬜`) squares.
- Easy-to-use GUI built with Tkinter.
- Dropdown menu for selecting row/column lengths.
- Input validation with error feedback displayed in real time.

---

## Project Structure

```
nonogram-guarantee-checker/
│
├── nonogram_guarantee.py       # Core logic for calculating guaranteed cells
├── app.py                      # Tkinter-based GUI application
├── README.md                   # Documentation (this file)
├── tests/                      # Unit tests for the logic
    └── test_nonogram_logic.py
```

---

## Installation

### Prerequisites
- Python 3.7 or later
- `tkinter` installed (usually included with Python)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/hyperionao/NonogramGuaranteer.git
   cd NonogramGuaranteer
   ```

2. (Optional) Set up a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Run the application:
   ```bash
   python app.py
   ```

---

## Usage

1. **Select the Row/Column Length**:
   - Use the dropdown to select the total length of the row/column.

2. **Input the Runs**:
   - Enter the runs in the input field, separated by spaces (e.g., "4 5 2").

3. **Calculate**:
   - Click the "Submit!" button to calculate the guaranteed cells.

4. **View Results**:
   - The results are displayed below, including:
     - A count of guaranteed slots.
     - A visual representation using black (`⬛`) and white (`⬜`) squares.

---

## Example Screenshot
![Nonogram GUI Example](https://gcdnb.pbrd.co/images/3krcxqW1YGeI.png?o=1)

---

## Testing

Unit tests validate the core logic (`nonogram_guarantee.py`). Run the tests with:
```bash
python -m unittest discover tests
```

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a feature branch.
3. Add your changes and tests.
4. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

- **Developer**: Aaron Ordonez