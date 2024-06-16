# fuel.py
def convert(fraction):
    try:
        X, Y = map(int, fraction.split('/'))
        if X > Y:
            raise ValueError("X should not be greater than Y")
        return round((X / Y) * 100)
    except ZeroDivisionError:
        raise ZeroDivisionError("Denominator should not be zero")
    except ValueError:
        raise ValueError("Both X and Y should be integers")

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

def main():
    pass

if __name__ == "__main__":
    main()
