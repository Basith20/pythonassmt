def exceptionhanding(n):
    try:
        return float(input(f'{n}'))
    except ArithmeticError:
        print("ArithmeticError Occurred and Handled")
    except KeyboardInterrupt:
        print("KeyboardInterrupt Occurred and Handled")
    except NameError:
        print("NameError Occurred and Handled")
    finally:
        return 0;